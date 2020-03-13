import pygame
from picamera import PiCamera
from time import sleep

red = (200,0,0)
lightred = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
X = 800
Y= 480
camera = PiCamera()

pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("yee")

bg = pygame.image.load('doge2.png').convert()
bgrect = bg.get_rect()
bgrect.center = (X/4+40,Y/2)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,msgz,action=None):
    mouse = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()
    
    if(x+w > mouse[0] > x and y+h > mouse[1] > y):
        pygame.draw.rect(screen, ac, (x,y,w,h))  #posx,posy,dimx,dimy
        
        if(clicked[0] == 1 and action != None):
            action()
    else:
        pygame.draw.rect(screen, ic, (x,y,w,h))
        
    btnText = pygame.font.SysFont("Quicksand Medium",msgz)
    textSurf, textRect = text_objects(msg, btnText)
    textRect.center = ( x+w/2, y+h/2 )
    screen.blit(textSurf, textRect)    

def takePic():
    camera.start_preview(alpha=192)
    sleep(3)
    camera.capture("/home/pi/Desktop/pic69.jpg")
    camera.stop_preview()

def kiosk_menu():
    run = True

    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
    
        largeText = pygame.font.SysFont("Quicksand",40)
        TextSurf, TextRect = text_objects("Welcome to Hilbert Hostel", largeText)
        TextRect.center = ((X/3),60)
        bg.set_alpha(128)
        infoText = pygame.font.SysFont("Quicksand",20)
        TextSurf2, TextRect2 = text_objects("Insert ID card here", infoText)
        TextRect2.center = (X-150,Y*3/4)
        
        screen.blit(bg,bgrect)
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf2, TextRect2)
        
        smileBtn = button("Smile!",X/5,Y-100,100,50,red,lightred,20,takePic)
    
        pygame.display.update() 

kiosk_menu()

pygame.quit()  # If we exit the loop this will execute and close our game
