import pygame, sys
from pygame.locals import*



pygame.init()
pygame.font.init()


SW = 600
SH = 600

size = SW,SH               
screen = pygame.display.set_mode(size)       #initilises the screen


global dead,deadrect,clock                  #sets the global clock
clock = pygame.time.Clock()
dead = pygame.image.load("dead.bmp")
deadrect = dead.get_rect()
deadrect.topleft = (100,250)

def death():                            # death funtion, runs he player dies
        running = True
        clock.tick(4000)
        
        screen.blit(dead,deadrect)
        pygame.display.flip()
        while running == True:
                for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                                pygame.display.quit()
                                running = False
                        elif event.type == KEYDOWN: 
                                running = False
#screen.blit(level, levelrect)


                
def main():

        manR = pygame.image.load("manR.bmp")
        manrect = manR.get_rect()
        manL = pygame.image.load("manL.bmp")
        manwalkR = pygame.image.load("manwalkR.bmp")     # picture loaded into lists
        manwalkL = pygame.image.load("manwalkL.bmp")
        manwalkR2 = pygame.image.load("manwalkR2.bmp")
        manwalkL2 = pygame.image.load("manwalkL2.bmp")
        jetpackonR = pygame.image.load("jetpackonR.bmp")
        jetpackonL = pygame.image.load("jetpackonL.bmp")
        jetpackoffR = pygame.image.load("jetpackoffR.bmp")
        jetpackoffL = pygame.image.load("jetpackoffL.bmp")
        brick = pygame.image.load("brick.bmp")
        brickrect = brick.get_rect()

        brickrect = brickrect.move(0, 0)

        man = manR


        
        



        
        
        level1 = pygame.image.load("level 1.bmp")
        level2 = pygame.image.load("level 2.bmp")
        level3 = pygame.image.load("level 3.bmp")
        level4 = pygame.image.load("level 4.bmp")
        level5 = pygame.image.load("level 5.bmp")
        lvl1 = pygame.image.load("lvl 1.bmp")
        lvl2 = pygame.image.load("lvl 2.bmp")
        lvl3 = pygame.image.load("lvl 3.bmp")
        lvl4 = pygame.image.load("lvl 4.bmp")
        lvl5 = pygame.image.load("lvl 5.bmp")
        load = pygame.image.load("loading.bmp")
        levelrect = level1.get_rect()

        screen.blit(load, levelrect)

        pygame.display.flip()

        back = []
        lvl = []
        one = []
        two = []
        three = []
        four = []
        five = []
        level = level1

        print 'Loading level 1....'#loads the first level during the loading time
        for x in range(0, 600):
                tmpList = []
                for y in range(0, 600):
                    tmpColour = lvl1.get_at((x, y))
                    if tmpColour == (255, 255, 255, 255):
                        tmpList.append(1)

                    else:
                        tmpList.append(0)
                one.append(tmpList)
        print "Done"

        


        
                



        '''
        print "Loading level 2...."                                     # levels avalable for loading
        for x in range(0, 600):
                tmpList = []
                for y in range(0, 600):
                    tmpColour = lvl2.get_at((x, y))
                    if tmpColour == (255, 255, 255, 255):
                        tmpList.append(1)

                    else:
                        tmpList.append(0)
                two.append(tmpList)
        print "Done"
        print "Loading level 3...."
        for x in range(0, 600):
                tmpList = []
                for y in range(0, 600):
                    tmpColour = lvl3.get_at((x, y))
                    if tmpColour == (255, 255, 255, 255):
                        tmpList.append(1)

                    else:
                        tmpList.append(0)
                three.append(tmpList)
        print "Done"
        print "Loading level 4...."
        for x in range(0, 600):
                tmpList = []
                for y in range(0, 600):
                    tmpColour = lvl4.get_at((x, y))
                    if tmpColour == (255, 255, 255, 255):
                        tmpList.append(1)

                    else:
                        tmpList.append(0)
                four.append(tmpList)
        print "Done"
        print "Loading level 5...."
        for x in range(0, 600):
                tmpList = []
                for y in range(0, 600):class spiky:
                
                    tmpColour = lvl5.get_at((x, y))
                    if tmpColour == (255, 255, 255, 255):
                        tmpList.append(1)

                    else:
                        tmpList.append(0)
                five.append(tmpList)
        print "Done"
        '''




        back = one

        running = True
        clock = pygame.time.Clock()
        Xpos = 0
        Ypos = 0
        gravity = 1
        jump = 0
        keyCheck = 0
        move = 0
        moveCheck = 0
        direction = 0
        jumping= 0
        manrect.bottomright = (65,500)

        x = 2
        y = 2
           
      
        start = (500,350)
        class spiky:                                                            #This is the new spike class. It now perpetuates itself and spawns in different directions
                counter = -1
                def __init__(self, topleft):
                        self.spike = pygame.image.load("spike.bmp")
                        self.rect = self.spike.get_rect()
                        self.rect.topleft = topleft
                        spiky.counter += 1
                        self.x = 2
                        self.y = 2
                        self.split = 0
                def move(self):
                        if self.split != 5:        
                                self.pix = self.rect.move(self.x,self.y)                                                       #moves the spike around and screen and checks if that object had split yet - Josh F

                        if back[self.pix.right][self.pix.centery] == 1 or back[self.pix.left][self.pix.centery] == 1:
                                self.x = self.x * -1
                                self.split += 1
                        
                        self.pix = self.rect.move(self.x,self.y)
                        if back[self.pix.centerx][self.pix.top] == 1 or back[self.pix.centerx][self.pix.bottom] == 1:
                                self.y = self.y * -1
                        elif back[self.pix.left][self.pix.top] == 1 or back[self.pix.right][self.pix.top] == 1:
                                self.y = self.y * -1
                        self.rect = self.rect.move(self.x,self.y)

        
        
        spikeList = [spiky(start)]
        #spike2.move()
        #screen.blit(spike2.spike,spike2.rect)
        #if manrect.colliderect(spikerect) == True:
        #death()
        #running = False

        #screen.blit(spike,rect)
        
        while running is True:     #main loop
                clock.tick(40)
                
                for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                                pygame.display.quit()
                                running = False
                        elif event.type == KEYDOWN:     # check if key is down
                                
                                if event.key == K_LEFT:
                                        keyCheck = keyCheck + 1
                                        direction = 1
                                elif event.key == K_RIGHT:
                                        keyCheck = keyCheck + 2
                                        direction = 2
                                elif event.key == K_SPACE:
                                       if moveCheck == manrect.top:       # jump key 
                                                Ypos = -11                      #Changed the value of Ypos from 15 to 11 - Josh F
                                                jumping= 1
                                elif event.key == K_LCTRL:              # jetpack key
                                        jump = 1
                                elif event.key == K_ESCAPE:
                                        running = False                                        
                        elif event.type == KEYUP:      #check if key is up
                                if event.key == K_LEFT:
                                        keyCheck = keyCheck - 1
                                        if keyCheck == 0:
                                                Xpos = 0
                                        man = manL
                                        direction = 2
                                elif event.key == K_RIGHT:
                                        keyCheck = keyCheck - 2
                                        if keyCheck == 0:
                                                Xpos = 0
                                        man = manR
                                        direction = 1
                                elif event.key == K_LCTRL:

                                        jump = 0
                                        jumping= 0

                

                
                if keyCheck == 1 :                              #moves the x axis
                        Xpos = -5
                                                
                elif keyCheck == 2:
                        Xpos = 5

                elif keyCheck == 3:
                        pass


                if Xpos == -5:                               # displays the walking sprites
                        if move < 4:
                                man = manL
                        elif move == 10:
                                move = 0
                        elif move > 4:
                                man = manwalkL
                        move = move + 1
                elif Xpos == 5:                        
                        if move < 4:
                                man = manR
                        elif move == 10:
                                move = 0
                        elif move > 4:
                                man = manwalkR
                        move = move + 1




                        
                if jumping== 1 and moveCheck != manrect.top:                    #makes man fall whether gravity or constant
                        Ypos = Ypos + gravity
                elif jumping== 0:
                        Ypos = Ypos + gravity


                if jump == 1 :                                                  # Makes man move on the y axis and shows the sprites
                        Ypos = -5
                        
                        if keyCheck == 1 :
                                man = jetpackonL
                        elif keyCheck == 2 :
                                man = jetpackonR
                        elif direction == 2:
                                man = jetpackonL
                        elif direction == 1:
                                man = jetpackonR
                        
                elif jump == 0 and moveCheck != manrect.top:
                        if keyCheck == 1 :
                                man = jetpackoffL
                        elif keyCheck == 2:
                                man = jetpackoffR 
                        elif direction == 2:
                                man = jetpackoffL
                        elif direction == 1:
                                man = jetpackoffR



                
                '''
                pix = spikerect.move(x,y)                                                       #moves monster called spike
                if back[pix.right][pix.centery] == 1 or back[pix.left][pix.centery] == 1:
                        x = x * -1
                pix = spikerect.move(x,y)
                if back[pix.centerx][pix.top] == 1 or back[pix.centerx][pix.bottom] == 1:
                        y = y * -1
                elif back[pix.left][pix.top] == 1 or back[pix.right][pix.top] == 1:
                        y = y * -1
                spikerect = spikerect.move(x,y)
               


                if manrect.colliderect(spikerect) == True:
                        death()
                        running = False
                '''

                moveCheck = manrect.top
                pixcheck = manrect.move(Xpos,Ypos)
                if back[pixcheck.left][pixcheck.top] == 1 or back[pixcheck.left][pixcheck.bottom] == 1:                                 #collision into brick are made impossible here
                        pop = 0
                        while (back[pixcheck.left][pixcheck.top] == 1 or back[pixcheck.left][pixcheck.bottom] == 1)and pop < 20:

                                if (back[pixcheck.left][pixcheck.top] == 1 or back[pixcheck.left][pixcheck.bottom] == 1):
                                        if Xpos < 0:
                                                Xpos = Xpos - Xpos 
                                                
                                        elif Xpos > 0:
                                                Xpos = Xpos - Xpos
                                                

                                pixcheck = manrect.move(Xpos,Ypos)

                                if (back[pixcheck.left][pixcheck.top] == 1 or back[pixcheck.left][pixcheck.bottom] == 1):
                                        if Ypos < 0:
                                                Ypos = Ypos -Ypos
            
                                        elif Ypos > 0:
                                                while (back[pixcheck.left][pixcheck.top] == 1 or back[pixcheck.left][pixcheck.bottom] == 1) and pop < 20:
                                                        
                                                        Ypos = Ypos -1
                                                        pop = pop + 1
                                                        pixcheck = manrect.move(Xpos,Ypos)
                                        if Ypos == 0:
                                                if keyCheck == 2 :
                                                        Xpos = 5

                                if back[pixcheck.left - 5][pixcheck.top] == 0 and back[pixcheck.left- 5][pixcheck.bottom] == 0:
                                        if keyCheck == 1 :
                                                Xpos = -5
                                                
                                        elif keyCheck == 2:
                                                Xpos = 5                           

                                #pixcheck = manrect.move(Xpos,Ypos)
                                pop = pop + 1

                if back[pixcheck.right][pixcheck.top] == 1 or back[pixcheck.right][pixcheck.bottom] == 1 :
                        pop = 0
                        while (back[pixcheck.right][pixcheck.top] == 1 or back[pixcheck.right][pixcheck.bottom] == 1) and pop < 20:

                                if Xpos < 0:
                                        Xpos = Xpos - Xpos 
                                        
                                elif Xpos > 0:
                                        
                                        Xpos = Xpos - Xpos
                                        

                                pixcheck = manrect.move(Xpos,Ypos)

                                if (back[pixcheck.right][pixcheck.top] == 1 or back[pixcheck.right][pixcheck.bottom] == 1):
                                        if Ypos < 0:
                                                Ypos = Ypos -Ypos
            
                                        elif Ypos > 0:
                                                while (back[pixcheck.right][pixcheck.top] == 1 or back[pixcheck.right][pixcheck.bottom] == 1) and pop < 20:
                                                        
                                                        Ypos = Ypos -1
                                                        pop = pop + 1
                                                        pixcheck = manrect.move(Xpos,Ypos)
                                        if Ypos == 0:
                                                if keyCheck == 1 :
                                                        Xpos = -5

                                              
                                                
                                if back[pixcheck.right + 5][pixcheck.top] == 0 and back[pixcheck.right+ 5][pixcheck.bottom] == 0:
                                        if keyCheck == 1 :
                                                Xpos = -5
                                                
                                        elif keyCheck == 2:
                                                Xpos = 5
                                pop = pop + 1


              
                pixcheck = 0        
                manrect = manrect.move(Xpos,Ypos)

   
                                
                if manrect.left < 0:   #    This is the boundry values so the man cannot move outside the screen
                        manrect.left = 0
                elif manrect.right > SW:
                        manrect.right = SW

                if manrect.top < 0:
                        manrect.top = 0
                elif manrect.bottom > SH:
                        manrect.bottom = SH
                        
                if moveCheck == manrect.top:
                        Ypos = 1
                elif Ypos > 6:
                        Ypos = 6



                

                if running == True:                                                     #This if statement stops the program crashing and creating an error message.
                
                        screen.blit(level, levelrect)
                        screen.blit(man, manrect)                                               # blits the game to the screen
                
                        #screen.blit(spike,spikerect)
                        
                        count = 0                                                               #Changed spike display. This displays all the new spikes and perpetuates new spikes - Josh F
                        while count <= spiky.counter:
                                spikeList[count].move()
                                screen.blit(spikeList[count].spike,spikeList[count].rect)
                                if spikeList[spiky.counter].split == 5:                     
                                                                                                                               
                                        spikeList.append(spiky(spikeList[spiky.counter].rect.topleft))          #appends the array to add more spike objects - Josh F
                                        spikeList[spiky.counter].move()
                                #screen.blit(spikeList[spiky.counter].spike,spikeList[spiky.counter].rect)
                                
                                if manrect.colliderect(spikeList[count].rect) == True:
                                        death()
                                        running = False
                                count += 1
                        

                
                        
                        pygame.display.flip()                           #refreshes the page - Josh F
                


def menu():                                                                     # start menu function
        runnning = True 
        menu1 = pygame.image.load("menu1.bmp")
        menurect = menu1.get_rect()
        menu = menu1
        screen.blit(menu, menurect)

        pygame.display.flip()
        start = 1
        menuman = pygame.image.load("menuman.bmp")
        menumanrect= menuman.get_rect()
        menumanrect.topleft = (125,150)
        menuman1 = pygame.image.load("menuman1.bmp")
        guy = menuman

        
        up = 3
        left = 2
        while start ==1 :     #main loop
                clock.tick(60)
                
                for event in pygame.event.get():

                        if event.type == pygame.QUIT:                                   #check if play or quit
                                pygame.display.quit()
                                
                                start == 0
                        elif event.type == KEYDOWN:     # check if key is down
                                if event.key == K_RETURN:
                                        main()
                                        runnning = True 
                                elif event.key == K_ESCAPE:
                                        start = 0
                                        
                                        pygame.display.quit()
                
                menumanrect = menumanrect.move(left,up)
                if menumanrect.top < 135:                                       #moves the opening bitmap
                        up = up* -1
                elif menumanrect.bottom > 575:
                        up = up * -1
                if menumanrect.left < 10:
                        left = left * -1
                        guy = menuman1
                elif menumanrect.right > 325:
                        left = left * -1
                        guy = menuman
                if start !=0:
                        screen.blit(menu, menurect)
                        screen.blit(guy,menumanrect)

                        pygame.display.flip()   


menu()
































