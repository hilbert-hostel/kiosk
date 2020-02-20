import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("yee")

run = True

while run:
    pygame.time.delay(100) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay

    for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
        if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
            run = False  # Ends the game loop

    pygame.draw.rect(screen, (255,0,0), (100,100,50,50))  
    pygame.display.update()      

pygame.quit()  # If we exit the loop this will execute and close our game