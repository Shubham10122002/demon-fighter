import pygame
import math
import random
pygame.init()
screen=pygame.display.set_mode((800,600))

#background
background=pygame.image.load('C:/Users/Dell/Downloads/space-galaxy-background.jpg')
#caption and iconbitmap
pygame.display.set_caption("SPACE GAME")
icon=pygame.image.load('C:/Users/Dell/Downloads/ufo.png')
pygame.display.set_icon(icon)
#player
playerImg=pygame.image.load('C:/Users/Dell/Downloads/space-ship (2).png')
playerx=370
playery=480
playerxchange=0


#enemy
enemyImg=[]
enemyy=[]
enemyx=[]
enemyxchange=[]
enemyychange=[]
noe=6
for i in range(noe):

    enemyImg.append(pygame.image.load('C:/Users/Dell/Downloads/rocksteady.png'))
    enemyx.append(random.randint(0,800))
    enemyy.append(random.randint(50,150))
    enemyxchange.append(0.3)
    enemyychange.append(40)
#Bullet
bulletImg=pygame.image.load('C:/Users/Dell/Downloads/bullet.png')
bulletx=0
bullety=480
bulletxchange=0
bulletychange=1
bulletstate="ready"

scorev=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=10
testy=10
def showscore(x,y):
    score=font.render("Score:"+str(scorev),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=font.render("GAME OVER"+" "+"your score: "+""+str(scorev),True,(255,255,255))
    screen.blit(over_text,(200,250))
def player(x,y):
    #screen ma playerImg nakhavanu and (x,y)coordinate ana
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    #screen ma enemyImg nakhavanu and (x,y)coordinate ana
    screen.blit(enemyImg[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletImg,(x+16,y+10))

def iscollision(enemyx,enemyy,bulletx,bullety):
    distance = math.sqrt(math.pow(enemyx-bulletx,2)+(math.pow(enemyy-bullety,2)))
    if distance<27:
        return True
    else:
        return False
#game screen loop
running=True
while running:
    screen.fill((0,0,128))
    #background
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False


    # if keystroke is pressed check wheter its right or left
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            playerxchange=-0.3
        if event.key==pygame.K_RIGHT:
            playerxchange=0.3
        if event.key==pygame.K_BACKSPACE:
            if bulletstate is "ready":
                #get the current x coordinate of spaceship
                bulletx=playerx
                firebullet(bulletx,bullety)
    if event.type==pygame.KEYUP:
        if event.key==pygame.K_LEFT or  event.key==pygame.K_RIGHT:
            playerxchange=0
    playerx+=playerxchange
    #setting boundary for spaceship
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736
    #enemy movement
    for i in range(noe):
        #go
        if enemyy[i]>440:
            for j in range(noe):
                enemyy[j]=2000
            game_over_text()
            break

        enemyx[i]+=enemyxchange[i]
        if enemyx[i]<=0:
            enemyxchange[i]=0.3
            enemyy[i]+=enemyychange[i]
        elif enemyx[i]>=736:
            enemyxchange[i]=-0.3
            enemyy[i]+=enemyychange[i]
        #iscollision
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            bullety=480
            bulletstate="ready"
            scorev+=1

            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)
        #bullet movement
    if bullety<=0:
        bullety=480
        bulletstate="ready"
    if bulletstate is "fire":
        firebullet(bulletx,bullety)
        bullety-=bulletychange



    player(playerx,playery)
    showscore(textx,testy)
    pygame.display.update()
