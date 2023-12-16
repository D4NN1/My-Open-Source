import pygame
import time
display_width = 800
display_height = 600
x_change = 0
y_change = 0
car_speed = 0

pygame.init()
dis = pygame.display.set_mode((800,600))
pygame.display.set_caption('Racing Into The Night')
black = (0,0,0)
blue = (180,180,255)
car_width = 73
car_height = 50
clock = pygame.time.Clock()
dead = False
playcar = pygame.image.load('racecar.png')

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    dis.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    
    

def crash():
    message_display('You Crashed')
def game(x,y):
    dis.blit(playcar,(x,y))
x = (display_width*0.5)
y = (display_height*0.5 )
while not dead:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           dead = True
        print(event)
         ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 0
        
            
        ######################
    ##
    x += x_change
    y += y_change
    dis.fill(blue)
    game(x,y)

    if x > display_width - car_width or x < 0:
        crash()
    if y > display_height - car_height or y < 0:
            crash()

    pygame.display.update()
    clock.tick(60)
else:
    print('You died')
pygame.quit()
quit()
