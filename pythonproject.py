import pygame
import sys
import random
pygame.init()
screen = pygame.display.set_mode((350, 600))#screen size
clock = pygame.time.Clock()#fps thing makes game smooth
class Apple:
    def __init__(self,image,position,speed):
        self.image = image
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
    def move(self):
        self.rect.y += self.speed
#variables
speed = 3
score = 0

TILESIZE = 32

#floor
floor_image = pygame.image.load("floor.png").convert_alpha()#load image
floor_image = pygame.transform.scale(floor_image,(TILESIZE*15,TILESIZE))#increase asize of image
floor_rect = floor_image.get_rect(bottomleft = (0,screen.get_height()))#determining postion of floor

#player
player_image = pygame.image.load("player_static.png").convert_alpha()#load image
player_image = pygame.transform.scale(player_image, (TILESIZE,TILESIZE*2))#width,height*2
player_rect = player_image.get_rect(center=(screen.get_width()/2,
                                        screen.get_height()- floor_image.get_height()-(player_image.get_height()/2)))#determine position of player_image

#apple
apple_image = pygame.image.load("apple.png").convert_alpha()
apple_image =  pygame.transform.scale(apple_image,(TILESIZE,TILESIZE))

#fonts
font = pygame.font.Font("PixeloidMono.ttf", TILESIZE//2)
#sound fx
pickup = pygame.mixer.Sound("powerup.mp3")
pickup.set_volume(0.1)
apples =[
        Apple(apple_image,(100,0),3),
        Apple(apple_image,(300,0),3)
]



#responding to user keys
def update():
    global speed
    global score
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 8
    elif keys[pygame.K_RIGHT]:
        player_rect.x += 8
    #apple management
    for apple in apples:
        apple.move()
        if apple.rect.colliderect(floor_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image,(random.randint(50,300), -50),speed))
        elif apple.rect.colliderect(player_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image,(random.randint(50,300), -50),speed))
            speed += 0.1
            score += 1
            pickup.play()
        elif apple.rect.colliderect(floor_rect) == 10:
            break
def draw():
    screen.fill("lightblue")#determines the colour of the screen
    screen.blit(floor_image,floor_rect)#determines postion of a image in a screen
    screen.blit(player_image, player_rect)#determines postion of a image

    for apple in apples:
        screen.blit(apple.image,apple.rect)
    
    score_text = font.render(f"Score: {score}", True,"white")
    screen.blit(score_text,(5,5))#helps to determine the postion of the image

running = True
#game loop
while running:
    for event in pygame.event.get():#takes input of any key from user
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    update()
    draw()
    clock.tick(60)
    pygame.display.update()
    