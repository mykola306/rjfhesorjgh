from pygame import*
import random
import time as tm
import pygame

WHITE = (255, 255,255)
BLACK = (0,0,0)


window = display.set_mode((600,600))
back = (225,225,255)
window.fill(back)
display.set_caption('Game')
pygame.mouse.set_visible(False)  # hide the cursor
MANUAL_CURSOR = pygame.image.load('flyfiii.png').convert_alpha()

score = pygame.Surface([80,40])
score.fill([100,20,120])
class Fly():
    def __init__(self):
        self.picture = transform.scale(image.load('fly.png'), (60,60))
        self.rect = self.picture.get_rect()
        self.rect.x = 0
        self.rect.y = 0
    def draw(self):
        window.blit(self.picture, (self.rect.x, self.rect.y))
                
    def fly(self):
        self.rect.x = random.randint(10,580)
        self.rect.y = random.randint(10,580)
    def catch(self, x,y):
        if self.rect.collidepoint(x,y):
zsrhfnrdmfyxtjhfbszdyxfctjfhgf0,50))

#картинка и надпись
#win = transform.scale(image.load('win.png'), (600,600)), (0, 0))

pygame.font.init()
myFont = pygame.font.Font(None,25)

points = 0 
clock = time.Clock()
win = transform.scale(image.load("win.png"),(600,600))

fly = Fly()
start_time = tm.time()
run = True
finish = False
while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x,y = e.pos
            if fly.catch(x,y):
                points += 1
            else:
                points -= 1
            print(points)
        #финальное окно 
        if points >= 10:
            finish = True
            window.blit( win ,(0,0))
    if not finish:    
        window.fill(back)
        fly.draw()
        curr_time = tm.time()
        if curr_time -start_time >1:
            fly.fly()
            start_time = curr_time
        clock.tick(40)
        text = myFont.render('Score:' + str(points), 1, [255,0,0])
        score.blit(text,[10,10])
        window.blit(score, [0,0])
        score.fill([100,20,120])
        window.blit( MANUAL_CURSOR, ( pygame.mouse.get_pos() ) )
    display.update()