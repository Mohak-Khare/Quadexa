# Importing libraries for voice input, output and displaying images
import speech_recognition
import pyttsx3
import pygame

# Importing keyword dictionary
from Keyword_Dictionary import Keywords

# Initializing library for voice output
engine = pyttsx3.init()

# Setting the speed of the voice
engine.setProperty('rate', 150)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# Initializing library for displaying images
pygame.init()

#Create Screen with size 900x600 pixels
width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

#Set the Title of Screen
pygame.display.set_caption('Quadexa')

#Display the Background Image
bg=pygame.image.load("bg3.png")
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()

activate="none"
exitstatus="no"

# Looping Code
while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            
            # Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                exitstatus='yes'
                break
            
            # To Read whether 's' key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    activate = 's'
                    print("S pressed")
        if activate.lower() =='s':
            
            # Listening for command
            r = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print('Speak:')
                audio = r.listen(source)
            command = r.recognize_google(audio)

            # Change the background image to Listening Image
            listenImg = pygame.image.load("bg4.png")
            image1 = pygame.transform.scale(listenImg, (900, 600))
            screen.blit(image1, (0, 0))
            pygame.display.update()

            print(f"You said {command}")
            for Keyword in Keywords:
                
                # Checking for keyword in user input
                if Keyword in command:
                    
                    # Showing Image
                    image = pygame.image.load(Keywords[Keyword][1])
                    image1 = pygame.transform.scale(image, (400, 200))
                    screen.blit(image1, (300, 250))

                    pygame.display.update()

                    # Saying Text
                    engine.say(Keywords[Keyword][0])
                    engine.runAndWait()
                
                # Checking if the user wants to stop
                elif command == 'stop' or command == 'Stop':
                    print('Thank you for using Quadexa. Have a good one!')
                    engine.say('Thank you for using Quadexa. Have a good one!')
                    engine.runAndWait()
                    
                    # Terminating the script
                    pygame.quit()
                    break
                    
            if exitstatus == "yes":
                pygame.quit()
                break
                
            # Reset the UI to get further inputs (if user doesn't want to stop)
            activate = "none"
            bg = pygame.image.load("bg3.png").convert_alpha()
            image1 = pygame.transform.scale(bg, (900, 600))
            screen.blit(image1, (0, 0))

    # Handling errors
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
