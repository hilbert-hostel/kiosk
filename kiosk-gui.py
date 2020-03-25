import pygame
#from picamera import PiCamera
from time import sleep
from card_reader import cardreader
from threadboi import Td
from smartcard.Exceptions import NoCardException

red = (200,0,0)
lightred = (255,0,0)
green = (0,200,0)
lightgreen = (0,255,0)
blue = (0,0,200)
lightblue = (0,0,255)
white = (255,255,255)
grey = (224,224,224)
dgrey = (200,200,200)
black = (0,0,0)
X = 800
Y = 460
#camera = PiCamera()
clock = pygame.time.Clock()
cr = cardreader()
otp = []
pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption("Hilbert")

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

def numpad():
    no1 = Button("1",60,60,grey,dgrey,20)
    no1.place(X/9,Y/2-45)
    no2 = Button("2",60,60,grey,dgrey,20)
    no2.place(X/9+70,Y/2-45)
    no3 = Button("3",60,60,grey,dgrey,20)
    no3.place(X/9+140,Y/2-45)
    no4 = Button("4",60,60,grey,dgrey,20)
    no4.place(X/9,Y/2+25)
    no5 = Button("5",60,60,grey,dgrey,20)
    no5.place(X/9+70,Y/2+25)
    no6 = Button("6",60,60,grey,dgrey,20)
    no6.place(X/9+140,Y/2+25)
    no7 = Button("7",60,60,grey,dgrey,20)
    no7.place(X/9,Y/2+95)
    no8 = Button("8",60,60,grey,dgrey,20)
    no8.place(X/9+70,Y/2+95)
    no9 = Button("9",60,60,grey,dgrey,20)
    no9.place(X/9+140,Y/2+95)
    no0 = Button("0",60,60,grey,dgrey,20)
    no0.place(X/9+70,Y/2+165)
    delete = Button("DEL",60,60,grey,dgrey,20)
    delete.place(X/9+140,Y/2+165)
    clear = Button("CLR",60,60,grey,dgrey,20)
    clear.place(X/9,Y/2+165)

    if(len(otp)<6):
        if(no1.is_clicked()):
            otp.append(1)
            sleep(0.2)
        if(no2.is_clicked()):
            otp.append(2)
            sleep(0.2)
        if(no3.is_clicked()):
            otp.append(3)
            sleep(0.2)        
        if(no4.is_clicked()):
            otp.append(4)
            sleep(0.2)
        if(no5.is_clicked()):
            otp.append(5)
            sleep(0.2)
        if(no6.is_clicked()):
            otp.append(6)
            sleep(0.2)
        if(no7.is_clicked()):
            otp.append(7)
            sleep(0.2)
        if(no8.is_clicked()):
            otp.append(8)
            sleep(0.2)
        if(no9.is_clicked()):
            otp.append(9)
            sleep(0.2)
        if(no0.is_clicked()):
            otp.append(0)
            sleep(0.2)
    if(delete.is_clicked()):
        if(len(otp)!=0):
            otp.pop()
            sleep(0.2)  
    if(clear.is_clicked()):
        otp.clear()
        sleep(0.2)

class Button(object):
    def __init__(self,msg,w,h,ic,ac,msgz):
        self.msg = msg
        self.w = w
        self.h = h
        self.ic = ic
        self.ac = ac
        self.msgz = msgz
    
    def place(self,x,y):
        self.x = x
        self.y = y
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()
        if(x+self.w > mouse[0] > x and y+self.h > mouse[1] > y):
            pygame.draw.rect(screen, self.ac, (x,y,self.w,self.h))  #posx,posy,dimx,dimy
        
        else:
            pygame.draw.rect(screen, self.ic, (x,y,self.w,self.h))
        
        btnText2 = text(self.msg,"Quicksand Medium",self.msgz,x+self.w/2,y+self.h/2)

    def is_clicked(self):
        mouse = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if(self.x+self.w > mouse[0] > self.x and self.y+self.h > mouse[1] > self.y):
            if(clicked[0] == 1):
                return True
        
        return False

#def takePic():
#    camera.start_preview(alpha=192)
#    sleep(3)
#    camera.capture("/home/pi/Desktop/pic69.jpg")
#    camera.stop_preview()


def kiosk_menu():
    boundary = -X/4
    alpha = 0
    is_inserted = 0
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
    
        screen.fill(white)
        
        doge = picture('doge2.png',X/4+40,Y/2,alpha)
        if(alpha<128):
            alpha += 3
        
        title = text("Welcome to Hilbert Hostel","Quicksand",40,boundary,60)
        if(boundary<X/3):
            boundary += 9
        
        insert = text("Insert ID card to check-in","Quicksand",20,X-150,Y*3/4)
        ckoutBtn = Button("Check-out",100,50,red,lightred,15)
        ckoutBtn.place(X/5,Y-100)
        
        if(ckoutBtn.is_clicked()):
            check_out()
            boundary = -X/4
            alpha = 0
        
        cardBtn = Button("Book",100,50,blue,lightblue,20)
        cardBtn.place(X-200,Y/2+50)
        
        try:
            cr.connection.connect()
            td = Td()
            td.setAction(cr.read_card)
            td.start()
            book_detail()
            boundary = -X/4
            alpha = 0
        except NoCardException:
            print("no card woei")
            
        if(cardBtn.is_clicked()):
            book_detail()
            boundary = -X/4
            alpha = 0

        pygame.display.update() 
        clock.tick(30)

def book_detail():
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                cr.CID = None
                run = False  # Ends the game loop
    
        screen.fill(white)   
        
        tom = picture('tomnews.jpeg',X/3,Y/2-50,128)
        title = text("Here is your booking detail","Quicksand",30,(X/4),50)
        add_on = text("Add-on","Quicksand",30,X-150,Y/3-50)
        if(cr.CID != None):
            info = text(cr.CID,"Quicksand",15,X/3,Y*3/4)        
        else :
            info = text("Bluh bluh bluh bluh","Quicksand",15,X/3,Y*3/4)
        OTPBtn = Button("Request OTP",100,50,green,lightgreen,15)
        
        OTPBtn.place(X-200,Y-80)
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
                otp.clear()
                run = False  # Ends the game loop
        
        slide = 0
        screen.fill(white)
        title = text("Enter your OTP","Quicksand",30,125,50)
        ref = text("OTP ref no.","Quicksand",25,95,Y/3+5)
        refNum = text("696969","Quicksand",25,X/4,Y/3+5)
        tom = picture('tomnews.jpeg',X-150,Y/4,128)
        info = text("Bluh bluh bluh bluh","Quicksand",15,X-150,Y/2)
        submitBtn = Button("Submit",100,50,green,lightgreen,20)

        for i in range(6):
            pygame.draw.rect(screen,grey,(50+slide,Y/4-40,50,50))
            slide += 70
        
        slide = 0
        for num in otp:
            text(str(num),"Quicksand",25,75+slide,Y/4-10)
            slide += 70

        submitBtn.place(X/2-50,Y-80)
    
        if(submitBtn.is_clicked()):
            take_pic()
            otp.clear()
            run = False
        np = numpad()
        pygame.display.update() 
        clock.tick(60)

def take_pic():
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
        
        screen.fill(white)    

        title = text("Lemme take a selfie","Quicksand",40,X/3,60)  
        
        smileBtn = Button("Smile!",100,50,red,lightred,20)
        smileBtn.place(X/5,Y-100)
        if(smileBtn.is_clicked()):
        #    takePic()  
            check_in_complete()
            run = False
        
        pygame.display.update() 
        clock.tick(60)

def check_in_complete():
    blink = 0
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN: # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
        
        screen.fill(white)
        title = text("Check-in complete","Quicksand",30,(X/4)-50,50)
        info = text("Check your account on the website","Quicksand",40,X/2,Y/2)
        if(blink<60): 
            leave = text("-Touch to leave-","Quicksand",20,(X/2),Y-80)
        if(blink>120):
            blink = 0   
        blink += 1
        pygame.display.update() 
        clock.tick(60)

def check_out():
    run = True
    while run:

        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT:  # Checks if the red button in the corner of the window is clicked
                run = False  # Ends the game loop
        
        screen.fill(white)
        title = text("Please scan QR Code to check-out","Quicksand",40,X/2,Y/2)
        pygame.display.update() 
        clock.tick(30)
        
kiosk_menu()

pygame.quit()  # If we exit the loop this will execute and close our game
