#brendan ha, aviral kumar
#6/10


#going to try to put the maze program onto the pygame window
from random import shuffle, randrange
import pygame, sys
from pygame.locals import *
pygame.init()
#pygame.mixer.init()
screen = pygame.display.set_mode((202,172))
pygame.display.set_caption('LEVEL ONE')

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (255,0,0)

blue = (255,0,0)
mazeblue=(58,143,254)
mazeblue3=(58,144,255)
mazeblue2=(102,182,255)
mazepink=(255,182,255)
mazepink2=(255,219,255)
horblu=(182,255,255)
horblu2=(102,0,255)

screen.fill((255,255,255))

"""def make_maze(w = 20, h = 10):
        vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)] #did i visit this
        ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]] #makes the vertical walls
        hor = [["+--"] * w + ['+'] for _ in range(h + 1)] #makes all the horizontal walls
        def walk(x, y):
                vis[y][x] = 1
 
                d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
                shuffle(d) #pick an adjacent block
                hor[0][0]="   " #opening for the "beginning"
                for (xx, yy) in d:
                        if vis[yy][xx]: #if this block has been visited (=1)
                                continue #then move on
                        if xx == x: #if is an x value
                                hor[max(y, yy)][x] = "+  " #then replaces +-- with +  to remove a wall
                        if yy == y:
                                ver[y][max(x, xx)] = "   " #then replaces |  with   to remove walls
                        walk(xx, yy) #repeat with new coord

        walk(1, 1) #start from 1,1
        for (a, b) in zip(hor, ver):
                print(''.join(a + ['\n'] + b))"""

# new plan: generate a few mazes of varying size, screen cap/import to picture
# designate ending pixels/area
#make game off that
##to work on: assign the color value to a wall, so the pic can't get past it

maze1=pygame.image.load("mazeA.png")
maze2=pygame.image.load("mazeB.png")
maze3=pygame.image.load("mazeC.png")
maze4a=pygame.image.load("mazeD1.png")
maze4b=pygame.image.load("mazeD2.png")

sprite=pygame.image.load("kanyesprite.jpg")

maze1x=0
maze1y=0
pygame.key.set_repeat(5,20)
kanyex=34
kanyey=25
def collide(x,y,z): #tell when ending is reached
        if y[1]== x[1]   == z[1] and y[0] <= x[0] <=z[0]:
                return True
        else:
                return False
#mask set??
#wallmask1=pygame.mask.from_surface(maze1)

def colortest(coord): #identify certain maze colors
        if coord == blue or coord== mazeblue or coord == mazeblue3 or coord ==mazeblue2 or coord ==mazepink or coord== mazepink2 or coord==horblu or coord ==horblu2:
                return True
        else:
                return False

end_it=False
kanyeswag=False
#start screen
startscreensound=pygame.mixer.Sound('Untitled.wav')
startscreensound.play()
while(end_it==False):
        screen.fill(black)
        myfont=pygame.font.SysFont("Times New Roman", 20)
        nlabel=myfont.render("Welcome to West Side Story. Mouse Click to begin.", True, (white))
        nlabel2=myfont.render("story", True, (white))
        nlabel3=myfont.render("Click mouse to begin", True, (white))
        pleading=myfont.render("walls don't work", True, (white))
        pleading2=myfont.render("just pretend :/", True, (white))
        
        
        for event in pygame.event.get():
                if event.type == QUIT: #if player makes the game quit, smoothly exits
                    pygame.quit() 
                    sys.exit()
                #nigganigganigga
                elif event.type==MOUSEBUTTONDOWN:
                        
                        end_it=True
                
        screen.blit(nlabel,(10,10))
        screen.blit(nlabel2,(83,40))
        screen.blit(nlabel3,(10,70))
        screen.blit(pleading, (10,100))
        screen.blit(pleading2, (10,130))
        pygame.display.flip()
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1,0.0)
while (kanyeswag==False):
        screen.blit(maze1,(maze1x,maze1y))
        screen.blit(sprite, (kanyex,kanyey))
        for event in pygame.event.get():
                if event.type == QUIT: #if player makes the game quit, smoothly exits
                    pygame.quit() 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        if colortest((kanyex+19,kanyey)) == False:
                                kanyex +=1
                    if event.key ==K_LEFT:
                        if colortest((kanyex-1,kanyey)) == False:
                                kanyex -=1
                    if event.key==K_DOWN:
                        if colortest((kanyex,kanyey+1)) == False:
                                kanyey +=1
                    if event.key == K_UP:
                        if colortest((kanyex,kanyey-1)) == False:
                                kanyey -=1
        
                
        pygame.draw.line(screen, (white), (132,134),(149,134),1)
        if collide((kanyex,kanyey),(129,134),(153,134)) == True:
                kanyeswag=True
        
        pygame.display.update()
screen=pygame.display.set_mode((308,243))
screen.fill(black)
while(end_it==True):
       nlabl=myfont.render("Onto Level 2", True, (white))
       interludesound=pygame.mixer.Sound('interlude.wav')
       interludesound.play()
       screen.blit(nlabl,(90,150))
       for event in pygame.event.get():
                if event.type == QUIT: #if player makes the game quit, smoothly exits
                    pygame.quit() 
                    sys.exit()
                if event.type == KEYDOWN:
                        
                        end_it=False
                elif event.type==MOUSEBUTTONDOWN:
                        end_it=False
       pygame.display.update()










maze2x=0
maze2y=0
kanyex=49
kanyey=30
screen=pygame.display.set_mode((308,243))
screen.fill(white)
pygame.display.set_caption('LEVEL TWO')
while (kanyeswag==True):
        screen.blit(maze2,(maze2x,maze2y))
        screen.blit(sprite, (kanyex,kanyey))
        for event in pygame.event.get():
                if event.type == QUIT: #if player makes the game quit, smoothly exits
                    pygame.quit() 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        kanyex +=1
                    if event.key ==K_LEFT:
                        kanyex -=1
                    if event.key==K_DOWN:
                        kanyey +=1
                    if event.key == K_UP:
                        kanyey -=1
        pygame.draw.line(screen, (white), (121,201), (137,201),1)
        if collide((kanyex,kanyey),(118,201),(140,201)) == True:
                kanyeswag=False #makes the req not true
        pygame.display.update()
        
screen=pygame.display.set_mode((540,419))
screen.fill(black)
myfont=pygame.font.SysFont("Times New Roman", 50)
while(end_it==False):
       nlabl=myfont.render("Onto Level 3", True, (white))
       interludesound=pygame.mixer.Sound('interlude.wav')
       interludesound.play()
       screen.blit(nlabl,(90,210))
       for event in pygame.event.get():
                if event.type == QUIT: #if player makes the game quit, smoothly exits
                    pygame.quit() 
                    sys.exit()
                if event.type == KEYDOWN:
                        
                        end_it=False
                elif event.type==MOUSEBUTTONDOWN:
                        end_it=True
       pygame.display.update()

maze3x=0
maze3y=0
kanyex=31
kanyey=36
screen=pygame.display.set_mode((540,419))
screen.fill(white)
pygame.display.set_caption('LEVEL THREE')
while (kanyeswag==False):
        screen.blit(maze3,(maze3x,maze3y))
        screen.blit(sprite, (kanyex,kanyey))
        for event in pygame.event.get():
                if event.type == QUIT: #if player makes the game quit, smoothly exits
                    pygame.quit() 
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        kanyex +=1
                    if event.key ==K_LEFT:
                        kanyex -=1
                    if event.key==K_DOWN:
                        kanyey +=1
                    if event.key == K_UP:
                        kanyey -=1
        pygame.draw.line(screen, (white), (121,201), (137,201),1)
        if collide((kanyex,kanyey),(481,363),(505,363)) == True or collide((kanyex,kanyey),(73,107),(97,107))==True:
                kanyeswag=True #makes the req not true
        pygame.display.update()
screen=pygame.display.set_mode((801,552))
screen.fill(black)
myfont=pygame.font.SysFont("Times New Roman", 70)
maze4ax=0
maze4ay=0

maze4bx=0
maze4by=0
screen=pygame.display.set_mode((801,552))

pygame.display.set_caption('LEVEL FOUR')
if collide((kanyex,kanyey),(73,107),(97,107))==True:
        kanyex=38
        kanyey=28
        while(end_it==True):
               nlabl2=myfont.render("Onto Level 4", True, (white))
               nlab13=myfont.render('(you lazy bastard)', True, (white))
               interludesound=pygame.mixer.Sound('interlude.wav')
               interludesound.play()
               screen.blit(nlabl2,(90,225))
               screen.blit(nlab13,(90,300))
               for event in pygame.event.get():
                        if event.type == QUIT: #if player makes the game quit, smoothly exits
                            pygame.quit() 
                            sys.exit()
                        if event.type == KEYDOWN:
                                
                                end_it=False
                        elif event.type==MOUSEBUTTONDOWN:
                                end_it=False
               pygame.display.update()
        while(kanyeswag==True):
                screen.fill(white)
                screen.blit(maze4a,(maze4ax,maze4ay))
                screen.blit(sprite, (kanyex,kanyey))
                for event in pygame.event.get():
                        if event.type == QUIT: #if player makes the game quit, smoothly exits
                            pygame.quit() 
                            sys.exit()
                        elif event.type == KEYDOWN:
                            if event.key == K_RIGHT:
                                kanyex +=1
                            if event.key ==K_LEFT:
                                kanyex -=1
                            if event.key==K_DOWN:
                                kanyey +=1
                            if event.key == K_UP:
                                kanyey -=1
                if collide((kanyex,kanyey),(492,515),(519,515)) == True:
                        kanyeswag=False
                pygame.display.update()






elif collide((kanyex,kanyey),(481,363),(505,363))==True:
        kanyex=38
        kanyey=28
        while(end_it==True):
                nlab12=myfont.render("Onto Level 4 ",True, (white))
                nlab13=myfont.render("(you're not lazy gj)", True, (white))
                interludesound.play()
                screen.blit(nlab12,(90,225))
                screen.blit(nlab13,(90,300))
                for event in pygame.event.get():
                        if event.type==QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type==KEYDOWN:
                                
                                end_it=False
                        elif event.type==MOUSEBUTTONDOWN:
                                end_it=False
                pygame.display.update()

        while(kanyeswag==True):
                screen.fill(white)
                screen.blit(maze4b,(maze4bx,maze4by))
                screen.blit(sprite, (kanyex,kanyey))
                for event in pygame.event.get():
                        if event.type == QUIT: #if player makes the game quit, smoothly exits
                            pygame.quit() 
                            sys.exit()
                        elif event.type == KEYDOWN:
                            if event.key == K_RIGHT:
                                kanyex +=1
                            if event.key ==K_LEFT:
                                kanyex -=1
                            if event.key==K_DOWN:
                                kanyey +=1
                            if event.key == K_UP:
                                kanyey -=1
                if collide((kanyex,kanyey),(81,33),(105,33)) == True:
                        kanyeswag=False
                pygame.display.update()

screen=pygame.display.set_mode((801,552))
pygame.display.set_caption('You did it!!!')
while (end_it)==False:
        myfont2=pygame.font.SysFont('Comic Sans',50)
        swag=myfont2.render('you did it wow gj this was bad', True, white)
        bound2=myfont2.render('kanye is proud of you',True,white)
        interludesound.play()
        screen.blit(swag,(200,225))
        screen.blit(bound2,(200,400))
        for event in pygame.event.get():
                if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type==KEYDOWN:
                        interludesound.play()
                        end_it=False
                elif event.type==MOUSEBUTTONDOWN:
                        end_it=True
        pygame.display.update()
        
