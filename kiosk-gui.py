import pygame
from picamera import PiCamera
from time import sleep

red = (200,0,0)
lightred = (255,0,0)
green = (0,200,0)
lightgreen = (0,255,0)
blue = (0,0,200)
lightblue = (0,0,255)
white = (255,255,255)
grey = (224,224,224)
black = (0,0,0)
X = 800
Y= 480
camera = PiCamera()
clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("yee")

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text(des,font,size,posx,posy):
    largeText = pygame.font.SysFont(font,size)
    TextSurf, TextRect = text_objects(des, largeText)
    TextRect.center = (posx,posy)
    screen.blit(TextSurf, TextRect)

def picture(name,posx,posy,alpha):
    bg = pygame.image.load(name).convert()
    bgrect = bg.get_rect()
    bgrect.center = (posx,posy)
    bg.set_alpha(alpha)   
    screen.blit(bg,bgrect)

class Button(object):
    def __init__(self,msg,x,y,w,h,ic,ac,msgz):
        self.msg = msg
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.msgz = msgz
    
    def place(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        if(self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y):
            pygame.draw.rect(screen, self.ac, (self.x,self.y,self.w,self.h))  #posx,posy,dimx,dimy
        
        else:
            pygame.draw.rect(screen, self.ic, (self.x,self.y,self.w,self.h))
        
        btnText = pygame.font.SysFont("Quicksand Medium",self.msgz)
        textSurf, textRect = text_objects(self.msg, btnText)
        textRect.center = ( self.x+self.w/2, self.y+self.h/2 )
        screen.blit(textSurf, textRect)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if(self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y):
            if(clicked[0] == 1):
                return True
        
        return False

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
        doge = picture('doge2.png',X/4+40,Y/2,128)
        title = text("Welcome to Hilbert Hostel","Quicksand",40,(X/3),60)
        insert = text("Insert ID card here","Quicksand",20,X-150,Y*3/4)
        smileBtn = Button("Smile!",X/5,Y-100,100,50,red,lightred,20)
        smileBtn.place()
        if(smileBtn.is_clicked()):
            takePic()
        cardBtn = Button("Book",X-200,Y/2+50,100,50,blue,lightblue,20)
        cardBtn.place()
        if(cardBtn.is_clicked()):
            book_detail()

        pygame.display.update() 
        clock.tick(60)

def book_detail():
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)   
        
        tom = picture('tomnews.jpeg',X/3,Y/2-50,128)
        title = text("Here is your booking detail","Quicksand",30,(X/4),50)
        add_on = text("Add-on","Quicksand",30,X-150,Y/3-50)
        info = text("Bluh bluh bluh bluh","Quicksand",15,X/3,Y*3/4)
        OTPBtn = Button("Request OTP",X-200,Y-80,100,50,green,lightgreen,20)
        OTPBtn.place()
        if(OTPBtn.is_clicked()):
            enter_OTP()
            run = False
        
        pygame.display.update() 
        clock.tick(60)

def enter_OTP():
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
        
        slide = 0
        screen.fill(white)
        title = text("Enter your OTP","Quicksand",30,125,50)
        ref = text("OTP ref no.","Quicksand",25,95,Y/3+50)
        tom = picture('tomnews.jpeg',X-150,Y/4,128)
        info = text("Bluh bluh bluh bluh","Quicksand",15,X-150,Y/2)
        submitBtn = Button("Submit",X/2-50,Y-80,100,50,green,lightgreen,20)
        submitBtn.place()
        if(submitBtn.is_clicked()):
            check_in_complete()
            run = False

        for i in range(6):
            pygame.draw.rect(screen,grey,(50+slide,Y/4-20,50,50))
            slide += 70
        
        pygame.display.update() 
        clock.tick(60)

def check_in_complete():
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
        
        screen.fill(white)
        title = text("Check-in complete","Quicksand",30,(X/4)-50,50)
        info = text("Check your account on the website","Quicksand",50,X/2,Y/2)
        
        pygame.display.update() 
        clock.tick(60)

kiosk_menu()

pygame.quit()  # If we exit the loop this will execute and close our game
