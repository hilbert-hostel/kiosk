import pygame
from picamera import PiCamera
from time import sleep

red = (200,0,0)
lightred = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
X = 1280
Y= 720
resolution = (1280,720)
camera = PiCamera()

pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("yee")

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
        
    btnText = pygame.font.Font("freesansbold.ttf",msgz)
    textSurf, textRect = text_objects(msg, btnText)
    textRect.center = ( x+w/2, y+h/2 )
    screen.blit(textSurf, textRect)    

def takePic():
    camera.start_preview(alpha=192)
    sleep(3)
    camera.capture("/home/pi/Desktop/yed1.jpg")
    camera.stop_preview()

run = True

while run:

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop
    
    screen.fill(white)
    
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Hilbert boiz", largeText)
    TextRect.center = ((X/2),100)
    screen.blit(TextSurf, TextRect)
    
    smileBtn = button("Smile!",X/2-150,Y-200,300,100,red,lightred,50,takePic)
    
    pygame.display.update()

pygame.quit()  # If we exit the loop this will execute and close our game
