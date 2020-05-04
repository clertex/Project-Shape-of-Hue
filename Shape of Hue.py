import pygame, time, random, sys
pygame.init() #initiation of pygame

#-------------------- SETUP ----------------------------------------------------
display_width = 1355
display_height = 750

gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Shape of Hue') 
clock = pygame.time.Clock()

pygame.mixer.music.load('rsc/01 - Main Menu.mp3')
pygame.mixer.music.play(-1)
#--------------------- VARIABLE INITIALIZATION ---------------------------------
#------ COLORS --------------
black = (20,20,20)
white = (255,255,255)
gray1 = (50, 50, 50)
yellow = (216,213,0)
violet = (97,0,194)
blue = (0,25,188)
orange = (190,95,0)
green = (31,188,0)
red = (201,0,0)

#------ PLAYER COUNT --------
player_count = 1
start_game = False
shape_on_play = 0

#------ PLAYER STATS --------
counter_round_total = [0,0,0,0]

#------ STAMINA -------------
stamina_P = [0,200,200,200]

#------ FLOOR IS LAVA -------
stateFloor = 0
countdown = 0
roundX = 0

spotSit = []

xY, yY = 18, 55
xV, yV = 458, 55
xB, yB = 898, 55
xO, yO = 18, 276
xG, yG = 458, 276
xR, yR = 898, 276

lavaColor = []

x1, y1 = 18, 497
x2, y2 = 458, 497
x3, y3 = 898, 497

randomLava1 = 1
randomLava2 = 6
randomLava3 = 3

#------- TILE COLLISSION ------
hitbox = [0]*20

tile_initializer = pygame.Surface((440,221), pygame.SRCALPHA)
tile_initializer.fill((0,0,0,150))
hitboxTile = pygame.mask.from_surface(tile_initializer)
hitbox[1] = hitboxTile

#------- TILES ----------------
tileColors = [["COLOR0"],["COLOR1"],["COLOR2"],["COLOR3"],["COLOR4"],["COLOR5"],["COLOR6"],["COLOR7"],["COLOR8"],["COLOR9"]]

#------- PLAYER INFO ---------
lives_P = [0,2,2,2]
play_P = [0,True,True,True]
iFrames_P = [0,0,0,0]
player_SHAPE = [[0],[0,0],[0,0],[0,0]]
pSHAPE = ["X","X","X","X"]
shapeAvailable = [[0],
                  [0,False,False,False,False,False,False,False],
                  [0,False,False,False,False,False,False,False],
                  [0,False,False,False,False,False,False,False]]
formState_P = [0,1,1,1]
formStateLock_P = [0, False, False, False]

#-------- USER INTERFACE ------
shapeDisplay_Ticket = [[0],
                       ["X","X","X","X","X","X","X","X"],
                       ["X","X","X","X","X","X","X","X"],
                       ["X","X","X","X","X","X","X","X"]]

menuButton_Shape = [0,0,0,0,0,0,0]
menuButton_Shape[1] = pygame.image.load('img/1032 - Boss Pentagon.png').convert_alpha()
menuButton_Shape[2] = pygame.image.load('img/1032 - Boss Pentagon 2.png').convert_alpha()
menuButton_Shape[3] = pygame.image.load('img/1034 - Boss Heart.png').convert_alpha()
menuButton_Shape[4] = pygame.image.load('img/1034 - Boss Heart 2.png').convert_alpha()
menuButton_Shape[5] = pygame.image.load('img/1033 - Boss Hexagon.png').convert_alpha()
menuButton_Shape[6] = pygame.image.load('img/1033 - Boss Hexagon 2.png').convert_alpha()

menuAction = "none"

prePlayButton_Shape = [0,0,0,0,0,0,0,0,0,0,0,0,0]
prePlayButton_Shape[1] = pygame.image.load('img/3213 - Pentagon 2.png').convert_alpha()
prePlayButton_Shape[2] = pygame.image.load('img/3213 - Pentagon 3.png').convert_alpha()
prePlayButton_Shape[3] = pygame.image.load('img/3113 - Heart 2.png').convert_alpha()
prePlayButton_Shape[4] = pygame.image.load('img/3113 - Heart 3.png').convert_alpha()

customShape = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
customShape[1] = pygame.image.load('img/1011 - Main Circle 3.png').convert_alpha()
customShape[8] = pygame.image.load('img/1011 - Main Circle 4.png').convert_alpha()
customShape[2] = pygame.image.load('img/1012 - Main Square 3.png').convert_alpha()
customShape[9] = pygame.image.load('img/1012 - Main Square 4.png').convert_alpha()
customShape[3] = pygame.image.load('img/1013 - Main Triangle 3.png').convert_alpha()
customShape[10] = pygame.image.load('img/1013 - Main Triangle 4.png').convert_alpha()
customShape[4] = pygame.image.load('img/1014 - Main Diamond 3.png').convert_alpha()
customShape[11] = pygame.image.load('img/1014 - Main Diamond 4.png').convert_alpha()
customShape[5] = pygame.image.load('img/1015 - Main Pentagon 3.png').convert_alpha()
customShape[12] = pygame.image.load('img/1015 - Main Pentagon 4.png').convert_alpha()
customShape[6] = pygame.image.load('img/1016 - Main Hexagon 3.png').convert_alpha()
customShape[13] = pygame.image.load('img/1016 - Main Hexagon 4.png').convert_alpha()
customShape[7] = pygame.image.load('img/1017 - Main Heart 3.png').convert_alpha()
customShape[14] = pygame.image.load('img/1017 - Main Heart 4.png').convert_alpha()
customShape_Mini = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
customShape_Mini[1] = pygame.image.load('img/2014 - Circle A.png').convert_alpha()
customShape_Mini[8] = pygame.image.load('img/2014 - Circle B.png').convert_alpha()
customShape_Mini[2] = pygame.image.load('img/2015 - Square A.png').convert_alpha()
customShape_Mini[9] = pygame.image.load('img/2015 - Square B.png').convert_alpha()
customShape_Mini[3] = pygame.image.load('img/2016 - Triangle A.png').convert_alpha()
customShape_Mini[10] = pygame.image.load('img/2016 - Triangle B.png').convert_alpha()
customShape_Mini[4] = pygame.image.load('img/2017 - Diamond A.png').convert_alpha()
customShape_Mini[11] = pygame.image.load('img/2017 - Diamond B.png').convert_alpha()
customShape_Mini[5] = pygame.image.load('img/2018 - Pentagon A.png').convert_alpha()
customShape_Mini[12] = pygame.image.load('img/2018 - Pentagon B.png').convert_alpha()
customShape_Mini[6] = pygame.image.load('img/2019 - Hexagon A.png').convert_alpha()
customShape_Mini[13] = pygame.image.load('img/2019 - Hexagon B.png').convert_alpha()
customShape_Mini[7] = pygame.image.load('img/2020 - Heart A.png').convert_alpha()
customShape_Mini[14] = pygame.image.load('img/2020 - Heart B.png').convert_alpha()

customShape_Ticket = [[0],
                       ["X","X","X","X","X","X","X","X"],
                       ["X","X","X","X","X","X","X","X"],
                       ["X","X","X","X","X","X","X","X"]]
armory_Ticket = [0,0,0,0]
dress_Ticket = [[0],
                [0,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1],
                [0,1,1,1,1,1,1,1]]
spot1_TAKEN = [[0],
               ["NO",0,0,0,0,0,0,0],
               ["NO",0,0,0,0,0,0,0],
               ["NO",0,0,0,0,0,0,0]]
#-------------------- PLAYER SHAPE ----------------------------------------------
mainShapeA = pygame.image.load('img/1011 - Main Circle.png').convert_alpha()
mainShapeA2 = pygame.image.load('img/1011 - Main Circle 2.png').convert_alpha()
mainShapeA3 = pygame.image.load('img/1011 - Main Circle 5.png').convert_alpha()
mainShapeA4 = pygame.image.load('img/1011 - Main Circle 6.png').convert_alpha()
hitboxShapeA = pygame.mask.from_surface(mainShapeA)
hitbox[2] = hitboxShapeA

mainShapeB = pygame.image.load('img/1012 - Main Square.png').convert_alpha()
mainShapeB2 = pygame.image.load('img/1012 - Main Square 2.png').convert_alpha()
mainShapeB3 = pygame.image.load('img/1012 - Main Square 5.png').convert_alpha()
mainShapeB4 = pygame.image.load('img/1012 - Main Square 6.png').convert_alpha()
hitboxShapeB = pygame.mask.from_surface(mainShapeB)
hitbox[3] = hitboxShapeB

mainShapeC = pygame.image.load('img/1013 - Main Triangle.png').convert_alpha()
mainShapeC2 = pygame.image.load('img/1013 - Main Triangle 2.png').convert_alpha()
mainShapeC3 = pygame.image.load('img/1013 - Main Triangle 5.png').convert_alpha()
mainShapeC4 = pygame.image.load('img/1013 - Main Triangle 6.png').convert_alpha()
hitboxShapeC = pygame.mask.from_surface(mainShapeC)
hitbox[4] = hitboxShapeC

mainShapeD = pygame.image.load('img/1014 - Main Diamond.png').convert_alpha()
mainShapeD2 = pygame.image.load('img/1014 - Main Diamond 2.png').convert_alpha()
mainShapeD3 = pygame.image.load('img/1014 - Main Diamond 5.png').convert_alpha()
mainShapeD4 = pygame.image.load('img/1014 - Main Diamond 6.png').convert_alpha()
hitboxShapeD = pygame.mask.from_surface(mainShapeD)
hitbox[5] = hitboxShapeD

mainShapeE = pygame.image.load('img/1015 - Main Pentagon.png').convert_alpha()
mainShapeE2 = pygame.image.load('img/1015 - Main Pentagon 2.png').convert_alpha()
mainShapeE3 = pygame.image.load('img/1015 - Main Pentagon 5.png').convert_alpha()
mainShapeE4 = pygame.image.load('img/1015 - Main Pentagon 6.png').convert_alpha()
hitboxShapeE = pygame.mask.from_surface(mainShapeE)
hitbox[6] = hitboxShapeE

mainShapeF = pygame.image.load('img/1016 - Main Hexagon.png').convert_alpha()
mainShapeF2 = pygame.image.load('img/1016 - Main Hexagon 2.png').convert_alpha()
mainShapeF3 = pygame.image.load('img/1016 - Main Hexagon 5.png').convert_alpha()
mainShapeF4 = pygame.image.load('img/1016 - Main Hexagon 6.png').convert_alpha()
hitboxShapeF = pygame.mask.from_surface(mainShapeF)
hitbox[7] = hitboxShapeF

mainShapeG = pygame.image.load('img/1017 - Main Heart.png').convert_alpha()
mainShapeG2 = pygame.image.load('img/1017 - Main Heart 2.png').convert_alpha()
mainShapeG3 = pygame.image.load('img/1017 - Main Heart 5.png').convert_alpha()
mainShapeG4 = pygame.image.load('img/1017 - Main Heart 6.png').convert_alpha()
hitboxShapeG = pygame.mask.from_surface(mainShapeG)
hitbox[8] = hitboxShapeG

weakness_P = [[0],
              ["COLOR1","COLOR2"],
              ["COLOR1","COLOR2"],
              ["COLOR1","COLOR2"]]

#------------ BACKGROUND ------------------
bg0 = pygame.image.load('img/1104 - Floor D.png').convert_alpha()
bg1 = pygame.image.load('img/1103 - Floor C.png').convert_alpha()
bg2 = pygame.image.load('img/1105 - Floor E.png').convert_alpha()
bg3 = pygame.image.load('img/1110 - Floor J.png').convert_alpha()
background_menu = 0
background_INFO1 = True

#------------ TUTORIAL --------------------
page = 1
bgT1 = pygame.image.load('img/1200 - Tutorial 1.png').convert_alpha()
bgT2 = pygame.image.load('img/1200 - Tutorial 2.png').convert_alpha()
bgT3 = pygame.image.load('img/1200 - Tutorial 3.png').convert_alpha()
bgT4 = pygame.image.load('img/1200 - Tutorial 4.png').convert_alpha()
bgT5 = pygame.image.load('img/1200 - Tutorial 5.png').convert_alpha()

bgT6 = pygame.image.load('img/1200 - Tutorial 6.png').convert_alpha()
bgT7 = pygame.image.load('img/1200 - Tutorial 7.png').convert_alpha()
bgT8 = pygame.image.load('img/1200 - Tutorial 8.png').convert_alpha()
bgT9 = pygame.image.load('img/1200 - Tutorial 9.png').convert_alpha()
bgT10 = pygame.image.load('img/1200 - Tutorial 10.png').convert_alpha()

bgT11 = pygame.image.load('img/1200 - Tutorial 11.png').convert_alpha()
bgT12 = pygame.image.load('img/1200 - Tutorial 12.png').convert_alpha()
bgT13 = pygame.image.load('img/1200 - Tutorial 13.png').convert_alpha()
bgT14 = pygame.image.load('img/1200 - Tutorial 14.png').convert_alpha()
bgT15 = pygame.image.load('img/1200 - Tutorial 15.png').convert_alpha()

bgT16 = pygame.image.load('img/1200 - Tutorial 16.png').convert_alpha()
bgT17 = pygame.image.load('img/1200 - Tutorial 17.png').convert_alpha()
bgT18 = pygame.image.load('img/1200 - Tutorial 18.png').convert_alpha()
bgT19 = pygame.image.load('img/1200 - Tutorial 19.png').convert_alpha()
bgT20 = pygame.image.load('img/1200 - Tutorial 20.png').convert_alpha()

bgT21 = pygame.image.load('img/1200 - Tutorial 21.png').convert_alpha()
bgT22 = pygame.image.load('img/1200 - Tutorial 22.png').convert_alpha()

#------------ CLOSING ---------------------
bgCA1 = pygame.image.load('img/5001 - Floor A.png').convert_alpha()
bgCA2 = pygame.image.load('img/5001 - Floor B.png').convert_alpha()
bgCA3 = pygame.image.load('img/5001 - Floor C.png').convert_alpha()
background_closing = 0
background_INFO2 = True
closeAction = "none"
closing_message = random.randrange(0,4)

#-------------------- FUNCTIONS ------------------------------------------------
#----------------- OTHERS -----------------------------------------
def background():
    x = int(display_width * 0.975)
    y = int(display_height * 0.885)
    bg = pygame.transform.scale((pygame.image.load
                                 ('img/1101 - Floor A.png').convert_alpha()),(x,y))
    gameDisplay.blit(bg,(18,55))

def boundariesMain():
    pygame.draw.rect(gameDisplay, white, (18,55,3,660))
    pygame.draw.rect(gameDisplay, white, (display_width-18,55,3,663))
    pygame.draw.rect(gameDisplay, white, (18,55,1320,3))
    pygame.draw.rect(gameDisplay, white, (18,display_height-35,1320,3))

#------------------ MAIN MENU SCREEN --------------------------------------------  
def SFX(sound):
    if sound == 0:
        effect = pygame.mixer.Sound('rsc/00 - Click 0.wav')
    if sound == 1:
        effect = pygame.mixer.Sound('rsc/00 - Click 1.wav')
    if sound == 2:
        effect = pygame.mixer.Sound('rsc/00 - Click 2.wav')
    if sound == 3:
        effect = pygame.mixer.Sound('rsc/00 - Click 3.wav')
    if sound == 4:
        effect = pygame.mixer.Sound('rsc/00 - Hit 1.wav')
    if sound == 5:
        effect = pygame.mixer.Sound('rsc/00 - Hit 2.wav')
    if sound == 6:
        effect = pygame.mixer.Sound('rsc/00 - Hit 3.wav')
    if sound == 7:
        effect = pygame.mixer.Sound('rsc/00 - Died.wav')
        
    effect.play()

def game_intro():
    global menuAction
    global background_menu
    global page
    
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    quit()

        #---------------------------           
        gameDisplay.fill(black)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if background_menu == 1:
            gameDisplay.blit(bg1,(15,15))
        elif background_menu == 2:
            gameDisplay.blit(bg2,(15,15))
        elif background_menu == 3:
            gameDisplay.blit(bg3,(15,15))
        else:
            gameDisplay.blit(bg0,(15,15))
            
        menu_intro_buttons("PLAY", 335, 535, 270, 320, 1)
        menu_intro_buttons("TUTORIAL", 600, 535, 570, 320, 3)
        menu_intro_buttons("QUIT", 938, 535, 870, 320, 5)

        logo = pygame.image.load('img/4000 - Logo.png').convert_alpha()
        gameDisplay.blit(logo,(595,20))
        font = pygame.font.Font('rsc/LionelloR.ttf', 120)
        text_LOGO = font.render("SHAPE OF HUE", True, white)
        gameDisplay.blit(text_LOGO,(375,165))
        
        if menuAction != "none":
            intro = False
            
        pygame.display.update()
        clock.tick(15)

    if menuAction == "play":
        menuAction = "none"
        prePlay()
    if menuAction == "tutorial":
        meanuAction = "none"
        page = 1
        tutorial()
    
def menu_intro_buttons(msg, x_msg, y_msg, x_button, y_button, imgCode):
    global menuButton_Shape
    global menuAction
    global background_menu
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    font = pygame.font.Font('rsc/Agency.ttf', 50)
    text = font.render(msg, True, white)
    gameDisplay.blit(text,(x_msg,y_msg))

    font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
    text_INFO1 = font5.render("Choose your shapes and survive colorful the lava.", True, white)
    text_INFO2 = font5.render("Learn the basics and controls of the game.", True, white)
    text_INFO3 = font5.render("Leave the game.", True, white)
    
    if x_button+200 > mouse[0] > x_button and y_button+200 > mouse[1] > y_button:
        gameDisplay.blit(menuButton_Shape[imgCode+1],(x_button-15,y_button-20))
        if imgCode == 1:
            gameDisplay.blit(text_INFO1,(290,670))
            background_menu = 1
        if imgCode == 3:
            gameDisplay.blit(text_INFO2,(345,670))
            background_menu = 2
        if imgCode == 5:
            gameDisplay.blit(text_INFO3,(530,670))
            background_menu = 3
            
        if click[0] == 1 and imgCode == 1 and menuAction == "none":
            SFX(0)
            menuAction = "play"
        elif click[0] == 1 and imgCode == 3 and menuAction == "none":
            SFX(0)
            menuAction = "tutorial"
        elif click[0] == 1 and imgCode == 5 and menuAction == "none":
            pygame.quit()
            quit()
    else:
        gameDisplay.blit(menuButton_Shape[imgCode],(x_button,y_button))

#------------------ TUTORIAL SCREEN --------------------------------------------
def tutorial():
    global page
    global menuAction
    global background_menu

    process = True
    while process:
        for event in pygame.event.get(): #takes the event of all the current inputs
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        pygame.quit()
                        quit()
        gameDisplay.fill(black)
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        page_display()
        
        #------ ARROWS ------------
        arrowLeft = pygame.image.load('img/0001 - Arrow Left.png').convert_alpha()
        arrowRight = pygame.image.load('img/0001 - Arrow Right.png').convert_alpha()

        gameDisplay.blit(arrowLeft,(30,400))
        gameDisplay.blit(arrowRight,(1290,400))

        paging()

        #------- COMMON -----------
        logo = pygame.image.load('img/4000 - Logo 2.png').convert_alpha()
        gameDisplay.blit(logo,(25,20))
        font1 = pygame.font.Font('rsc/LionelloR.ttf', 80)
        text_LOGO = font1.render("SHAPE OF HUE", True, white)
        gameDisplay.blit(text_LOGO,(125,27))
        font3 = pygame.font.Font('rsc/Agency.ttf', 50)
        text_LOBBY = font3.render("TUTORIAL", True, white)
        gameDisplay.blit(text_LOBBY,(550,47))

        #------- BACK -------------
        font2 = pygame.font.Font('rsc/Agency.ttf', 30)
        text = font2.render("BACK", True, white)
        gameDisplay.blit(text,(38,695))
        if 28+93 > mouse[0] > 28 and 625+93 > mouse[1] >625:
            gameDisplay.blit(prePlayButton_Shape[2],(25,622))
            font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
            text_INFO6 = font5.render("Return to main menu.", True, white)
            gameDisplay.blit(text_INFO6,(530,670))
            if click[0] == 1:
                SFX(0)
                menuAction = "none"
                background_menu = 0
                game_intro()
        else:
            gameDisplay.blit(prePlayButton_Shape[1],(28,625))

        #---------------------
        pygame.display.update()
        clock.tick(15)

def paging():
    global page
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    
    arrowLeft2 = pygame.image.load('img/0001 - Arrow Left 2.png').convert_alpha()
    arrowRight2 = pygame.image.load('img/0001 - Arrow Right 2.png').convert_alpha()
    if 30+29 > mouse[0] > 30 and 400+35 > mouse[1] > 400:
        gameDisplay.blit(arrowLeft2,(28,398))
        if click[0] == 1 or keys[pygame.K_LEFT]:
            SFX(0)
            page -= 1
            if page < 1:
                page = 44
                
    if 1290+29 > mouse[0] > 1288 and 400+35 > mouse[1] > 400:
        gameDisplay.blit(arrowRight2,(1288,398))
        if click[0] == 1 or keys[pygame.K_RIGHT]:
            SFX(0)
            page += 1
            if page > 44:
                page = 1
                
def page_display():
    global page

    if page == 1 or page == 2:
        gameDisplay.blit(bgT1,(15,15))
    if page == 3 or page == 4:
        gameDisplay.blit(bgT2,(15,15))
    if page == 5 or page == 6:
        gameDisplay.blit(bgT3,(15,15))
    if page == 7 or page == 8:
        gameDisplay.blit(bgT4,(15,15))
    if page == 9 or page == 10:
        gameDisplay.blit(bgT5,(15,15))
        
    if page == 11 or page == 12:
        gameDisplay.blit(bgT6,(15,15))
    if page == 13 or page == 14:
        gameDisplay.blit(bgT7,(15,15))
    if page == 15 or page == 16:
        gameDisplay.blit(bgT8,(15,15))
    if page == 17 or page == 18:
        gameDisplay.blit(bgT9,(15,15))
    if page == 19 or page == 20:
        gameDisplay.blit(bgT10,(15,15))

    if page == 21 or page == 22:
        gameDisplay.blit(bgT11,(15,15))
    if page == 23 or page == 24:
        gameDisplay.blit(bgT12,(15,15))
    if page == 25 or page == 26:
        gameDisplay.blit(bgT13,(15,15))
    if page == 27 or page == 28:
        gameDisplay.blit(bgT14,(15,15))
    if page == 29 or page == 30:
        gameDisplay.blit(bgT15,(15,15))

    if page == 31 or page == 32:
        gameDisplay.blit(bgT16,(15,15))
    if page == 33 or page == 34:
        gameDisplay.blit(bgT17,(15,15))
    if page == 35 or page == 36:
        gameDisplay.blit(bgT18,(15,15))
    if page == 37 or page == 38:
        gameDisplay.blit(bgT19,(15,15))
    if page == 39 or page == 40:
        gameDisplay.blit(bgT20,(15,15))
    if page == 41 or page == 42:
        gameDisplay.blit(bgT21,(15,15))
    if page == 43 or page == 44:
        gameDisplay.blit(bgT22,(15,15))
        
#------------------ PRE-PLAY SCREEN --------------------------------------------
def prePlay():
    global prePlayButton_Shape
    global menuAction
    global background_INFO1
    global background_menu
    global player_count
    global start_game
    
    prePlay = True
    player_2 = False
    player_3 = False
    
    while prePlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    quit()
        #----------------------------
        gameDisplay.fill(black)
        #-------- FOOTER MESSAGES -------------------
        font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
        text_INFO1 = font5.render("Add or subtract more players and assign their shapes.", True, white)
        text_INFO2 = font5.render("Add Player 2.", True, white)
        text_INFO3 = font5.render("Remove Player 2.", True, white)
        text_INFO4 = font5.render("Add Player 3.", True, white)
        text_INFO5 = font5.render("Remove Player 3.", True, white)
        text_INFO6 = font5.render("Return to main menu.", True, white)
        text_INFO7 = font5.render("All are finalized and ready to play.", True, white)
        
        #------- FOOTER -----------
        gameDisplay.blit(bg1,(15,15))

        if background_INFO1 == True:
            gameDisplay.blit(text_INFO1,(260,670))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        logo = pygame.image.load('img/4000 - Logo 2.png').convert_alpha()
        gameDisplay.blit(logo,(25,20))
        font1 = pygame.font.Font('rsc/LionelloR.ttf', 80)
        text_LOGO = font1.render("SHAPE OF HUE", True, white)
        gameDisplay.blit(text_LOGO,(125,27))
        font3 = pygame.font.Font('rsc/Agency.ttf', 50)
        text_LOBBY = font3.render("PLAYER LOBBY", True, white)
        gameDisplay.blit(text_LOBBY,(550,47))


        customBox = pygame.image.load('img/0001 - Custom Box.png').convert_alpha()
        gameDisplay.blit(customBox,(25,120))
        pygame.draw.rect(gameDisplay, white, (135,105,200,35))
        font4 = pygame.font.Font('rsc/Agency.ttf', 35)
        text_TAGP1 = font4.render("PLAYER 1", True, black)
        gameDisplay.blit(text_TAGP1,(192,107))
        shapePicking_Mini(70, 1, player_2, player_3)
        shapePicking_Display(110, 190, 1)

        add1 = pygame.image.load('img/0001 - Add 1.png').convert_alpha()
        add2 = pygame.image.load('img/0001 - Add 2.png').convert_alpha()
        minus1 = pygame.image.load('img/0001 - Minus 1.png').convert_alpha()
        minus2 = pygame.image.load('img/0001 - Minus 2.png').convert_alpha()
        if player_2 == True:
            gameDisplay.blit(customBox,(460,120))
            pygame.draw.rect(gameDisplay, white, (570,105,200,35))
            font4 = pygame.font.Font('rsc/Agency.ttf', 35)
            text_TAGP2 = font4.render("PLAYER 2", True, black)
            gameDisplay.blit(text_TAGP2,(627,107))
            shapePicking_Mini(505, 2, player_2, player_3)
            shapePicking_Display(545, 190, 2)
            if 560+45 > mouse[0] > 560 and 100+95 > mouse[1] > 100:
                gameDisplay.blit(minus2,(560,100))
                background_INFO1 = False
                gameDisplay.blit(text_INFO3,(550,670))
                if click[0] == 1:
                    SFX(0)
                    player_2 = False
                    player_count -= 1
            else:
                gameDisplay.blit(minus1,(560,100))
        else:
            if 620+95 > mouse[0] > 620 and 290+95 > mouse[1] > 290:
                gameDisplay.blit(add2,(620,290))
                background_INFO1 = False
                gameDisplay.blit(text_INFO2,(550,670))
                if click[0] == 1:
                    SFX(0)
                    player_2 = True
                    player_count += 1
                    start_game = False
            else:
                gameDisplay.blit(add1,(620,290))

        if player_3 == True:
            gameDisplay.blit(customBox,(895,120))
            pygame.draw.rect(gameDisplay, white, (1005,105,200,35))
            font4 = pygame.font.Font('rsc/Agency.ttf', 35)
            text_TAGP3 = font4.render("PLAYER 3", True, black)
            gameDisplay.blit(text_TAGP3,(1062,107))
            shapePicking_Mini(940, 3, player_2, player_3)
            shapePicking_Display(980, 190, 3)
            if 995+45 > mouse[0] > 995 and 100+95 > mouse[1] > 100:
                gameDisplay.blit(minus2,(995,100))
                background_INFO1 = False
                gameDisplay.blit(text_INFO5,(550,670))
                if click[0] == 1:
                    SFX(0)
                    player_3 = False
                    player_count -= 1
            else:
                gameDisplay.blit(minus1,(995,100))
        else:
            if 1050+95 > mouse[0] > 1050 and 290+95 > mouse[1] > 290:
                gameDisplay.blit(add2,(1050,290))
                gameDisplay.blit(text_INFO4,(550,670))
                background_INFO1 = False
                if click[0] == 1:
                    SFX(0)
                    player_3 = True
                    player_count += 1
                    start_game = False
            elif player_2 == True:
                gameDisplay.blit(add1,(1050,290))
        
        #------- BACK -------------
        font2 = pygame.font.Font('rsc/Agency.ttf', 30)
        text = font2.render("BACK", True, white)
        gameDisplay.blit(text,(38,695))
        if 28+93 > mouse[0] > 28 and 625+93 > mouse[1] >625:
            gameDisplay.blit(prePlayButton_Shape[2],(25,622))
            background_INFO1 = False
            gameDisplay.blit(text_INFO6,(530,670))
            if click[0] == 1:
                SFX(0)
                start_game = False
                menuAction = "none"
                background_menu = 0
                game_intro()
        else:
            gameDisplay.blit(prePlayButton_Shape[1],(28,625))

        #------- PLAY -------------
        font2 = pygame.font.Font('rsc/Agency.ttf', 30)
        text = font2.render("PLAY", True, white)
        gameDisplay.blit(text,(1280,695))
        if 1268+93 > mouse[0] > 1268 and 625+93 > mouse[1] >625:
            gameDisplay.blit(prePlayButton_Shape[4],(1265,622))
            background_INFO1 = False
            gameDisplay.blit(text_INFO7,(430,670))
            if click[0] == 1 and start_game == True:
                SFX(0)
                pygame.mixer.music.stop()
                shape_Equip(1)
                shape_Equip(2)
                shape_Equip(3)
                game_main()
        else:
            gameDisplay.blit(prePlayButton_Shape[3],(1268,625))
        
        pygame.display.update()
        clock.tick(15)

def shapePicking_Mini(x, ID, player_2, player_3):
    global customShape,customShape_Mini,customShape_Ticket,armory_Ticket
    global start_game,player_count,shape_on_play
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    y = 550
    
    ok = 1
    while ok <= 7:
        if x+(50*(ok-1))+38 > mouse[0] > x+(50*(ok-1)) and y+38 > mouse[1] > y:
            if click[0] == 1:
                SFX(0)
                if customShape_Ticket[ID][ok] == "X" and armory_Ticket[ID] < 2:
                    customShape_Ticket[ID][ok] = "O"
                    click = (0,0,0)
                    armory_Ticket[ID] += 1
                    shape_on_play += 1
                elif customShape_Ticket[ID][ok] == "O":
                    customShape_Ticket[ID][ok] = "X"
                    click = (0,0,0)
                    armory_Ticket[ID] -= 1
                    shape_on_play -= 1
                if armory_Ticket[ID] == 2:
                    if player_2 == False and shape_on_play >= 2:
                        start_game = True
                    if player_2 == True and shape_on_play >= 4:
                        start_game = True
                    if player_3 == True and shape_on_play == 6:
                        start_game = True
                else:
                    start_game = False
                print("SHAPE ON PLAY:",shape_on_play)
                print("GAME START?:", start_game)
        ok += 1
                    
    ctr = 1
    while ctr <= 7:
        if customShape_Ticket[ID][ctr] == "O":
            gameDisplay.blit(customShape_Mini[ctr+7],(x+(50*(ctr-1)),y))
        elif customShape_Ticket[ID][ctr] == "X":
            gameDisplay.blit(customShape_Mini[ctr],(x+(50*(ctr-1)),y))          
        ctr += 1

def shapePicking_Display(x, y, ID):
    global customShape,customShape_Ticket,dress_Ticket
    global displayed
    global player_SHAPE
    
    arrowLeft = pygame.image.load('img/0001 - Arrow Left.png').convert_alpha()
    arrowRight = pygame.image.load('img/0001 - Arrow Right.png').convert_alpha()
    
    checking = 1
    while checking <= 7:
        if customShape_Ticket[ID][checking] == "O" and spot1_TAKEN[ID][0] == "NO":
            spot1_TAKEN[ID][0] = "YES"
            spot1_TAKEN[ID][1] = checking
        if customShape_Ticket[ID][checking] == "X" and spot1_TAKEN[ID][1] == checking:
            spot1_TAKEN[ID][0] = "NO"
            spot1_TAKEN[ID][1] = 0
            
        if customShape_Ticket[ID][checking] == "O" and spot1_TAKEN[ID][0] == "YES" and spot1_TAKEN[ID][1] != checking:
            if dress_Ticket[ID][checking] % 2 == 1:
                gameDisplay.blit(customShape[checking],(x, y+160))
                player_SHAPE[ID][1] = checking
                colorWeakness_Display(x+170,y+150,ID,checking)
            elif dress_Ticket[ID][checking] % 2 == 0:
                gameDisplay.blit(customShape[checking+7],(x, y+160))
                player_SHAPE[ID][1] = checking+7
                colorWeakness_Display(x+170,y+150,ID,checking)
            gameDisplay.blit(arrowLeft,(x-50,y+190))
            gameDisplay.blit(arrowRight,(x+120,y+190))
            shapePicking_Dress(x-50,y+190,x+120,y+190, checking, ID)
            
        elif customShape_Ticket[ID][checking] == "O" and spot1_TAKEN[ID][0] == "YES" and spot1_TAKEN[ID][1] == checking:
            if dress_Ticket[ID][checking] % 2 == 1:
                gameDisplay.blit(customShape[checking],(x, y))
                player_SHAPE[ID][0] = checking
                colorWeakness_Display(x+170,y-10,ID,checking)
            elif dress_Ticket[ID][checking] % 2 == 0:
                gameDisplay.blit(customShape[checking+7],(x, y))
                player_SHAPE[ID][0] = checking+7
                colorWeakness_Display(x+170,y-10,ID,checking)
            gameDisplay.blit(arrowLeft,(x-50,y+30))
            gameDisplay.blit(arrowRight,(x+120,y+30))
            shapePicking_Dress(x-50,y+30,x+120,y+30, checking, ID)
        checking += 1

def shapePicking_Dress(xLeft,yLeft,xRight,yRight,shape,ID):
    global dress_Ticket
    global background_INFO1
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
    text_INFO8 = font5.render("Change shape design.", True, white)
    arrowLeft = pygame.image.load('img/0001 - Arrow Left 2.png').convert_alpha()
    arrowRight = pygame.image.load('img/0001 - Arrow Right 2.png').convert_alpha()
    
    if xLeft+35 > mouse[0] > xLeft and yLeft+35 > mouse[1] > yLeft:
        gameDisplay.blit(arrowLeft,(xLeft-2,yLeft-3))
        background_INFO1 = False
        gameDisplay.blit(text_INFO8,(500,670))
        if click[0] == 1:
            SFX(0)
            dress_Ticket[ID][shape] += 1
    if xRight+35 > mouse[0] > xRight and yRight+35 > mouse[1] > yRight:
        gameDisplay.blit(arrowRight,(xRight-2,yRight-3))
        background_INFO1 = False
        gameDisplay.blit(text_INFO8,(500,670))
        if click[0] == 1:
            SFX(0)
            dress_Ticket[ID][shape] += 1

def colorWeakness_Display(x,y,ID,shape):
    font1 = pygame.font.Font('rsc/Agency.ttf', 29)
    text_WEAKNESS = font1.render("COLOR WEAKNESS", True, white)
    gameDisplay.blit(text_WEAKNESS,(x,y))

    if shape == 1:
        pygame.draw.rect(gameDisplay, yellow, (x,y+40,68,35))
        pygame.draw.rect(gameDisplay, violet, (x+78,y+40,68,35))
    if shape == 2:
        pygame.draw.rect(gameDisplay, blue, (x,y+40,68,35))
        pygame.draw.rect(gameDisplay, orange, (x+78,y+40,68,35))
    if shape == 3:
        pygame.draw.rect(gameDisplay, green, (x,y+40,68,35))
        pygame.draw.rect(gameDisplay, red, (x+78,y+40,68,35))
    if shape == 4:
        pygame.draw.rect(gameDisplay, yellow, (x,y+40,68,35))
        pygame.draw.rect(gameDisplay, red, (x+78,y+40,68,35))
    if shape == 5:
        pygame.draw.rect(gameDisplay, blue, (x,y+40,68,35))
        pygame.draw.rect(gameDisplay, violet, (x+78,y+40,68,35))
    if shape == 6:
        pygame.draw.rect(gameDisplay, green, (x,y+40,68,35))
        pygame.draw.rect(gameDisplay, orange, (x+78,y+40,68,35))
    if shape == 7:
        pygame.draw.rect(gameDisplay, blue, (x,y+40,68,35))
        pygame.draw.rect(gameDisplay, yellow, (x+78,y+40,68,35))
    
#------------------------------------------
def shape_Equip(ID):
    global player_SHAPE, shapeDisplay_Ticket
    shape1 = player_SHAPE[ID][0]
    shape2 = player_SHAPE[ID][1]

    ctr = 1
    while ctr <= 7:
        if shape1 == ctr or shape1 == ctr+7:
            shapeAvailable[ID][ctr] = True
            shapeDisplay_Ticket[ID][ctr] = "ON"
        if shape2 == ctr or shape2 == ctr+7:
            shapeAvailable[ID][ctr] = True
            shapeDisplay_Ticket[ID][ctr] = "OFF"
        ctr += 1

#========================== MAIN GAME PARTS ==========================
#----------- PLAYERS ----------------------------------------------
def mShape_P(x,y, ID):
    global weakness_P, play_P, shapeAvailable
    global equipped_Shape, formState_P, player_SHAPE
    global pSHAPE
    
    if play_P[ID] == True:
        if formState_P[ID] == 1:
            if shapeAvailable[ID][1] == True and player_SHAPE[ID][0] == 1:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeA2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeA,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "CIR"
            elif shapeAvailable[ID][1] == True and player_SHAPE[ID][0] == 8:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeA4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeA3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "CIR"
                    
            elif shapeAvailable[ID][2] == True and player_SHAPE[ID][0] == 2:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeB2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeB,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "SQR"
            elif shapeAvailable[ID][2] == True and player_SHAPE[ID][0] == 9:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeB4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeB3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "SQR"
                    
            elif shapeAvailable[ID][3] == True and player_SHAPE[ID][0] == 3:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeC2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeC,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "TRI"
            elif shapeAvailable[ID][3] == True and player_SHAPE[ID][0] == 10:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeC4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeC3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "TRI"
                    
            elif shapeAvailable[ID][4] == True and player_SHAPE[ID][0] == 4:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeD2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeD,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "DIA"
            elif shapeAvailable[ID][4] == True and player_SHAPE[ID][0] == 11:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeD4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeD3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "DIA"
                    
            elif shapeAvailable[ID][5] == True and player_SHAPE[ID][0] == 5:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeE2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeE,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "PEN"
            elif shapeAvailable[ID][5] == True and player_SHAPE[ID][0] == 12:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeE4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeE3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "PEN"
                    
            elif shapeAvailable[ID][6] == True and player_SHAPE[ID][0] == 6:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeF2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeF,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "HEX"
            elif shapeAvailable[ID][6] == True and player_SHAPE[ID][0] == 13:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeF4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeF3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "HEX"
                    
            elif shapeAvailable[ID][7] == True and player_SHAPE[ID][0] == 7:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeG2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeG,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "HRT"
            elif shapeAvailable[ID][7] == True and player_SHAPE[ID][0] == 14:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeG4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                else:
                    gameDisplay.blit(mainShapeG3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][0])
                    pSHAPE[ID] = "HRT"
                
        if formState_P[ID] == 2:
            if shapeAvailable[ID][1] == True and player_SHAPE[ID][1] == 1:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeA2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeA,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "CIR"
            elif shapeAvailable[ID][1] == True and player_SHAPE[ID][1] == 8:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeA4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeA3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "CIR"
                    
            elif shapeAvailable[ID][2] == True and player_SHAPE[ID][1] == 2:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeB2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeB,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "SQR"
            elif shapeAvailable[ID][2] == True and player_SHAPE[ID][1] == 9:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeB4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeB3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "SQR"
                    
            elif shapeAvailable[ID][3] == True and player_SHAPE[ID][1] == 3:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeC2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeC,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "TRI"
            elif shapeAvailable[ID][3] == True and player_SHAPE[ID][1] == 10:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeC4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeC3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "TRI"
                    
            elif shapeAvailable[ID][4] == True and player_SHAPE[ID][1] == 4:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeD2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeD,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "DIA"
            elif shapeAvailable[ID][4] == True and player_SHAPE[ID][1] == 11:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeD4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeD3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "DIA"
                    
            elif shapeAvailable[ID][5] == True and player_SHAPE[ID][1] == 5:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeE2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeE,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "PEN"
            elif shapeAvailable[ID][5] == True and player_SHAPE[ID][1] == 12:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeE4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeE3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "PEN"
                    
            elif shapeAvailable[ID][6] == True and player_SHAPE[ID][1] == 6:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeF2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeF,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "HEX"
            elif shapeAvailable[ID][6] == True and player_SHAPE[ID][1] == 13:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeF4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeF3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "HEX"
                    
            elif shapeAvailable[ID][7] == True and player_SHAPE[ID][1] == 7:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeG2,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeG,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "HRT"
            elif shapeAvailable[ID][7] == True and player_SHAPE[ID][1] == 14:
                if iFrames_P[ID] > 0:
                    gameDisplay.blit(mainShapeG4,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                else:
                    gameDisplay.blit(mainShapeG3,(x,y))
                    weakness_P[ID][0], weakness_P[ID][1] = colorWeakness(player_SHAPE[ID][1])
                    pSHAPE[ID] = "HRT"
        
def colorWeakness(shape):
    if shape == 1 or shape == 8:
        weaknessA = "YELLOW"
        weaknessB = "VIOLET"
    elif shape == 2 or shape == 9:
        weaknessA = "BLUE"
        weaknessB = "ORANGE"
    elif shape == 3 or shape == 10:
        weaknessA = "GREEN"
        weaknessB = "RED"
    elif shape == 4 or shape == 11:
        weaknessA = "YELLOW"
        weaknessB = "RED"
    elif shape == 5 or shape == 12:
        weaknessA = "BLUE"
        weaknessB = "VIOLET"
    elif shape == 6 or shape == 13:
        weaknessA = "GREEN"
        weaknessB = "ORANGE"
    elif shape == 7 or shape == 14:
        weaknessA = "BLUE"
        weaknessB = "YELLOW"

    return weaknessA, weaknessB
        
def iFrames_Decay():
    global iFrames_P
    
    if iFrames_P[1] > 0:
        iFrames_P[1] -= 1
    if iFrames_P[2] > 0:
        iFrames_P[2] -= 1
    if iFrames_P[3] > 0:
        iFrames_P[3] -= 1
        
#----------- USER INTERFACE ------------------------------------------
def gameUI_A(formState_P1):
    avatar(formState_P1,1)
    weakness(formState_P1, 1)
    switch(1)

def gameUI_B(formState_P1, formState_P2):
    avatar(formState_P1,1)
    weakness(formState_P1, 1)
    switch(1)

    avatar(formState_P2,2)
    weakness(formState_P2, 2)
    switch(2)

def gameUI_C(formState_P1, formState_P2, formState_P3):
    avatar(formState_P1,1)
    weakness(formState_P1, 1)
    switch(1)

    avatar(formState_P2,2)
    weakness(formState_P2, 2)
    switch(2)

    avatar(formState_P3,3)
    weakness(formState_P3, 3)
    switch(3)
    
def avatar(formShape, ID):
    global play_P
    global shapeDisplay_Ticket
    global player_SHAPE
    global formState_P
    global iFrames_P
    
    invncibilityBox = pygame.Surface((57,57), pygame.SRCALPHA)
    invncibilityBox.fill((0,0,0,100))
    
    if ID == 1:
        x, y = 35, 13
    if ID == 2:
        x, y = 490, 13
    if ID == 3:
        x, y = 945, 13
        
    if play_P[ID] == True:
        if formState_P[ID] == 1:
            displayAvatar(x,y,ID,player_SHAPE[ID][0])
        if formState_P[ID] == 2:
            displayAvatar(x,y,ID,player_SHAPE[ID][1])
            
        font = pygame.font.Font('freesansbold.ttf', 35)
        
        if iFrames_P[ID] <= 90 and iFrames_P[ID] >= 60:
            gameDisplay.blit(invncibilityBox,(x+2,y+2))
            text = font.render("3", True, white)
            gameDisplay.blit(text,(x+23,y+14))
        if iFrames_P[ID] <= 60 and iFrames_P[ID] >= 30:
            gameDisplay.blit(invncibilityBox,(x+2,y+2))
            text = font.render("2", True, white)
            gameDisplay.blit(text,(x+23,y+14))
        if iFrames_P[ID] <= 30 and iFrames_P[ID] > 0:
            gameDisplay.blit(invncibilityBox,(x+2,y+2))            
            text = font.render("1", True, white)
            gameDisplay.blit(text,(x+23,y+14))

def displayAvatar(x,y, ID, shapeX):
    shapeTemp = shapeX
    
    if shapeTemp > 7:
        shapeTemp -= 7
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 1:
        circleAVATAR = pygame.image.load('img/2101 - HP1 Circle.png').convert_alpha()
        gameDisplay.blit(circleAVATAR,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 2:
        squareAVATAR = pygame.image.load('img/2102 - HP1 Square.png').convert_alpha()
        gameDisplay.blit(squareAVATAR,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 3:
        triangleAVATAR = pygame.image.load('img/2102 - HP1 Triangle.png').convert_alpha()
        gameDisplay.blit(triangleAVATAR,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 4:
        diamondAVATAR = pygame.image.load('img/2102 - HP1 Diamond.png').convert_alpha()
        gameDisplay.blit(diamondAVATAR,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 5:
        pentagonAVATAR = pygame.image.load('img/2102 - HP1 Pentagon.png').convert_alpha()
        gameDisplay.blit(pentagonAVATAR,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 6:
        hexagonAVATAR = pygame.image.load('img/2102 - HP1 Hexagon.png').convert_alpha()
        gameDisplay.blit(hexagonAVATAR,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 7:
        heartAVATAR = pygame.image.load('img/2102 - HP1 Heart.png').convert_alpha()
        gameDisplay.blit(heartAVATAR,(x,y))
        
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 8:
        circleAVATAR2 = pygame.image.load('img/2101 - HP2 Circle.png').convert_alpha()
        gameDisplay.blit(circleAVATAR2,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 9:
        squareAVATAR2 = pygame.image.load('img/2102 - HP2 Square.png').convert_alpha()
        gameDisplay.blit(squareAVATAR2,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 10:
        triangleAVATAR2 = pygame.image.load('img/2102 - HP2 Triangle.png').convert_alpha()
        gameDisplay.blit(triangleAVATAR2,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 11:
        diamondAVATAR2 = pygame.image.load('img/2102 - HP2 Diamond.png').convert_alpha()
        gameDisplay.blit(diamondAVATAR2,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 12:
        pentagonAVATAR2 = pygame.image.load('img/2102 - HP2 Pentagon.png').convert_alpha()
        gameDisplay.blit(pentagonAVATAR2,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 13:
        hexagonAVATAR2 = pygame.image.load('img/2102 - HP2 Hexagon.png').convert_alpha()
        gameDisplay.blit(hexagonAVATAR2,(x,y))
    if shapeDisplay_Ticket[ID][shapeTemp] == "ON" and shapeX == 14:
        heartAVATAR2 = pygame.image.load('img/2102 - HP2 Heart.png').convert_alpha()
        gameDisplay.blit(heartAVATAR2,(x,y))

def weakness(state, ID):
    global weakness_P
    global play_P
    
    if ID == 1:
        x,y = 320, 40
    if ID == 2:
        x,y = 775, 40
    if ID == 3:
        x,y = 1230, 40
    if play_P[ID] == True:
        colorA = weaknessColor(weakness_P[ID][0])
        colorB = weaknessColor(weakness_P[ID][1])
        pygame.draw.circle(gameDisplay, colorA, (x,y), 15)
        pygame.draw.circle(gameDisplay, colorB, (x+40,y), 15)

def weaknessColor(weakness):
    color = 0,0,0
    
    if weakness == "YELLOW":
        color = 216,213,0
    if weakness == "VIOLET":
        color = 97,0,194
    if weakness == "BLUE":
        color = 0,25,188
    if weakness == "ORANGE":
        color = 190,95,0
    if weakness == "GREEN":
        color = 31,188,0
    if weakness == "RED":
        color = 201,0,0
        
    return color

def switch(ID):
    global play_P
    if play_P[ID] == True:
        font = pygame.font.Font('rsc/Agency.ttf', 28)
        if ID == 1:
            switchZone = pygame.Surface((100,25), pygame.SRCALPHA)
            switchZone.fill(white)
            gameDisplay.blit(switchZone,(35,705))
            text = font.render("TAB", True, black)
            gameDisplay.blit(text,(68,705))
        if ID == 2:
            switchZone = pygame.Surface((65,25), pygame.SRCALPHA)
            switchZone.fill(white)
            gameDisplay.blit(switchZone,(520,705))
            text = font.render("P", True, black)
            gameDisplay.blit(text,(547,705))
        if ID == 3:
            switchZone = pygame.Surface((65,25), pygame.SRCALPHA)
            switchZone.fill(white)
            gameDisplay.blit(switchZone,(985,705))
            text = font.render("3", True, black)
            gameDisplay.blit(text,(1011,705))
        
        

#------ SWITCH SHAPE ------------------------------------------------------
def buttonSWITCH(state, ID, x, y):
    global play_P
    global shapeDisplay_Ticket
    global player_SHAPE
    global formState_P
    
    position_ShapeA = x
    position_ShapeB = y
    shape1 = player_SHAPE[ID][0]
    shape2 = player_SHAPE[ID][1]

    if play_P[ID] == True:
        if player_SHAPE[ID][0] > 7:
            shape1 = player_SHAPE[ID][0] - 7
        if player_SHAPE[ID][1] > 7:
            shape2 = player_SHAPE[ID][1] - 7
                
        if state >=1 and state <=3:
            if shapeDisplay_Ticket[ID][shape1] != "X":
                shapeDisplay_Ticket[ID][shape1] = "ON"
                shapeDisplay_Ticket[ID][shape2] = "OFF"
                formState_P[ID] = 1
            else:
                state = 4     
        if state >= 4 and state <= 6:
            if shapeDisplay_Ticket[ID][shape2] != "X":
                if shapeDisplay_Ticket[ID][shape1] != "X":
                    shapeDisplay_Ticket[ID][shape1] = "OFF"
                shapeDisplay_Ticket[ID][shape2] = "ON"
                formState_P[ID] = 2
            else:
                shapeDisplay_Ticket[ID][shape1] = "ON"
                formState_P[ID] = 1
                state = 4

        displayMiniShapes(position_ShapeA, 700, ID, player_SHAPE[ID][0], "SHAPE A:")
        displayMiniShapes(position_ShapeB, 700, ID, player_SHAPE[ID][1], "SHAPE B:")


def displayMiniShapes(x,y, ID, shapeX, msg):
    if shapeDisplay_Ticket[ID][1] == "ON" and (shapeX == 1 or shapeX == 8):
        circleB = pygame.image.load('img/2014 - Circle B.png').convert_alpha()
        gameDisplay.blit(circleB,(x,y))
    elif shapeDisplay_Ticket[ID][1] == "OFF" and (shapeX == 1 or shapeX == 8):
        circleA = pygame.image.load('img/2014 - Circle A.png').convert_alpha()
        gameDisplay.blit(circleA,(x,y))
        
    if shapeDisplay_Ticket[ID][2] == "ON" and (shapeX == 2 or shapeX == 9):
        squareB = pygame.image.load('img/2015 - Square B.png').convert_alpha()
        gameDisplay.blit(squareB,(x,y))
    elif shapeDisplay_Ticket[ID][2] == "OFF" and (shapeX == 2 or shapeX == 9):
        squareA = pygame.image.load('img/2015 - Square A.png').convert_alpha()
        gameDisplay.blit(squareA,(x,y))

    if shapeDisplay_Ticket[ID][3] == "ON" and (shapeX == 3 or shapeX == 10):
        triangleB = pygame.image.load('img/2016 - Triangle B.png').convert_alpha()
        gameDisplay.blit(triangleB,(x,y))
    elif shapeDisplay_Ticket[ID][3] == "OFF" and (shapeX == 3 or shapeX == 10):
        triangleA = pygame.image.load('img/2016 - Triangle A.png').convert_alpha()
        gameDisplay.blit(triangleA,(x,y))

    if shapeDisplay_Ticket[ID][4] == "ON" and (shapeX == 4 or shapeX == 11):
        diamondB = pygame.image.load('img/2017 - Diamond B.png').convert_alpha()
        gameDisplay.blit(diamondB,(x,y))
    elif shapeDisplay_Ticket[ID][4] == "OFF" and (shapeX == 4 or shapeX == 11):
        diamondA = pygame.image.load('img/2017 - Diamond A.png').convert_alpha()
        gameDisplay.blit(diamondA,(x,y))

    if shapeDisplay_Ticket[ID][5] == "ON" and (shapeX == 5 or shapeX == 12):
        pentagonB = pygame.image.load('img/2018 - Pentagon B.png').convert_alpha()
        gameDisplay.blit(pentagonB,(x,y))
    elif shapeDisplay_Ticket[ID][5] == "OFF" and (shapeX == 5 or shapeX == 12):
        pentagonA = pygame.image.load('img/2018 - Pentagon A.png').convert_alpha()
        gameDisplay.blit(pentagonA,(x,y))

    if shapeDisplay_Ticket[ID][6] == "ON" and (shapeX == 6 or shapeX == 13):
        hexagonB = pygame.image.load('img/2019 - Hexagon B.png').convert_alpha()
        gameDisplay.blit(hexagonB,(x,y))
    elif shapeDisplay_Ticket[ID][6] == "OFF" and (shapeX == 6 or shapeX == 13):
        hexagonA = pygame.image.load('img/2019 - Hexagon A.png').convert_alpha()
        gameDisplay.blit(hexagonA,(x,y))

    if shapeDisplay_Ticket[ID][7] == "ON" and (shapeX == 7 or shapeX == 14):
        heartB = pygame.image.load('img/2020 - Heart B.png').convert_alpha()
        gameDisplay.blit(heartB,(x,y))
    elif shapeDisplay_Ticket[ID][7] == "OFF" and (shapeX == 7 or shapeX == 14):
        heartA = pygame.image.load('img/2020 - Heart A.png').convert_alpha()
        gameDisplay.blit(heartA,(x,y))
 

#------- STAMINA ------------
def staminaHP(drain, ID):
    global play_P
    if ID == 1:
        x, y = 95, 25
    if ID == 2:
        x, y = 550, 25
    if ID == 3:
        x, y = 1005, 25
    if play_P[ID] == True:
        pygame.draw.rect(gameDisplay, gray1, (x,y,200,30))
        global stamina_P
        if drain > 0 and stamina_P[ID] >= 10:
            stamina_P[ID] -= drain
        elif drain == 0 and stamina_P[ID] <= 200:
            stamina_P[ID] += 1 
        pygame.draw.rect(gameDisplay, white, (x,y,stamina_P[ID],30))
    else:
        stamina_P[ID] = 0
    return stamina_P[ID]

#--------------- LAVA SPAWNING ------------------------------------
def lavaDisplay(x,y,r,g,b):
    lavaZone = pygame.Surface((440,221), pygame.SRCALPHA)
    global countdown
    if countdown >= 0 and countdown <= 15:
        lavaZone.fill((r,g,b,15))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 16 and countdown <= 30:
        lavaZone.fill((r,g,b,30))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 31 and countdown <= 45:
        lavaZone.fill((r,g,b,45))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 46 and countdown <= 60:
        lavaZone.fill((r,g,b,60))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 61 and countdown <= 75:
        lavaZone.fill((r,g,b,75))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 76 and countdown <= 90:
        lavaZone.fill((r,g,b,90))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 91 and countdown <= 105:
        lavaZone.fill((r,g,b,105))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 106 and countdown <= 120:
        lavaZone.fill((r,g,b,120))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 121 and countdown <= 135:
        lavaZone.fill((r,g,b,135))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 136 and countdown <= 150:
        lavaZone.fill((r,g,b,150))
        gameDisplay.blit(lavaZone,(x,y))
    elif countdown >= 151 and countdown <= 250:
        lavaZone.fill((r,g,b,200))
        gameDisplay.blit(lavaZone,(x,y))
        
def randomCord(): 
    global spotSit
    process = True
    while process:
        spot = random.randrange(1,10)
        rangeSit = range(len(spotSit))
        length = len(spotSit)
        if length > 10:
            spotSit.clear()
        for x in rangeSit:
            if spot == spotSit[x]:
                break
            if x == length-1:
                spotSit.append(spot)
                process = False    
        if length == 0:
            spotSit.append(spot)
            process = False
    if spot == 1:
        x,y = 18, 55
    elif spot == 2:
        x,y = 458, 55
    elif spot == 3:
        x,y = 898, 55
    elif spot == 4:
        x,y = 18, 276
    elif spot == 5:
        x,y = 458, 276
    elif spot == 6:
        x,y = 898, 276
    elif spot == 7:
        x,y = 18, 497
    elif spot == 8:
        x,y = 458, 497
    elif spot == 9:
        x,y = 898, 497    
    return x, y

def yellowLava():
    r,g,b = 216, 213, 0
    global xY, yY
    x, y = xY, yY
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,1)
    tileMessanger(x,y,1)
    
def violetLava():
    r,g,b = 97, 0, 194
    global xV, yV
    x, y = xV, yV
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,2)
    tileMessanger(x,y,2)
        
def blueLava(): 
    r,g,b = 0, 25, 188
    global xB, yB
    x,y = xB, yB
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,3)
    tileMessanger(x,y,3)
        
def orangeLava():
    r,g,b = 190, 95, 0
    global xO, yO
    x, y = xO, yO
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,4)
    tileMessanger(x,y,4)
        
def greenLava():
    r,g,b = 31, 188, 0
    global xG, yG
    x, y = xG, yG
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,5)
    tileMessanger(x,y,5)
    
def redLava():
    r,g,b = 201, 0, 0
    global xR, yR
    x,y = xR, yR
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,6)
    tileMessanger(x,y,6)
     
def floorLava():
    yellowLava()
    violetLava()
    blueLava()
    orangeLava()
    greenLava()
    redLava()

def randomLava(x,y,instance):
    global lavaColor, stateFloor 
    process = True
    
    if stateFloor == 0:
        process = False
        if instance == 1:
            global randomLava1
            color = randomLava1
        if instance == 2:
            global randomLava2
            color = randomLava2
        if instance == 3:
            global randomLava3
            color = randomLava3
            
    while process:
        color = random.randrange(1,7)
        rangeLavaColor = range(len(lavaColor))
        length = len(lavaColor)
        
        for x in rangeLavaColor:
            if color == lavaColor[x]:
                break
            if x == length-1:
                lavaColor.append(color)
                process = False
                
        if len(lavaColor) == 0:
            lavaColor.append(color)
            process = False
            
    if color == 1:
        yellowLavaR(x,y)
    if color == 2:
        violetLavaR(x,y)
    if color == 3:
        blueLavaR(x,y)
    if color == 4:
        orangeLavaR(x,y)
    if color == 5:
        greenLavaR(x,y)
    if color == 6:
        redLavaR(x,y)
        
    if instance == 1:
        randomLava1 = color
    if instance == 2:
        randomLava2 = color
    if instance == 3:
        randomLava3 = color
        
def yellowLavaR(x,y):
    r,g,b = 216, 213, 0
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,1)
    tileMessanger(x,y,1)

def violetLavaR(x,y):
    r,g,b = 97, 0, 194
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,2)
    tileMessanger(x,y,2)
        
def blueLavaR(x,y):
    r,g,b = 0, 25, 188
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,3)
    tileMessanger(x,y,3)
        
def orangeLavaR(x,y):
    r,g,b = 190, 95, 0
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,4)
    tileMessanger(x,y,4)
        
def greenLavaR(x,y):
    r,g,b = 31, 188, 0
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,5)
    tileMessanger(x,y,5)
        
def redLavaR(x,y):
    r,g,b = 201, 0, 0
    lavaDisplay(x,y,r,g,b)
    tileCollission(x,y,r,g,b,6)
    tileMessanger(x,y,6)
        
#-------------------- COLLISIONS ---------------------------------
def tileCollission(x,y,r,g,b,color):
    global countdown
    global hitbox
    if countdown >= 150 and countdown <= 250:
        tile_1 = pygame.Surface((440,221), pygame.SRCALPHA)
        tile_1.fill((r,g,b,150))
        hitboxTile = pygame.mask.from_surface(tile_1)
        hitbox[1] = hitboxTile
        gameDisplay.blit(tile_1,(x,y))

def tileIdentity(x,y):
    tileID = 0
    tileX, tileY = 0, 0
    if x >= 18 and x < 458 and y >= 55 and y < 276:
        tileID = 1
        tileX, tileY = 18, 55
    elif x >= 458 and x < 898 and y >= 55 and y < 276:
        tileID = 2
        tileX, tileY = 458, 55
    elif x >= 898 and y >= 55 and y < 276:
        tileID = 3
        tileX, tileY = 898, 55
    elif x >= 18 and x < 458 and y >= 276 and y < 497:
        tileID = 4
        tileX, tileY = 18, 276
    elif x >= 458 and x < 898 and y >= 276 and y < 497:
        tileID = 5
        tileX, tileY = 458, 276
    elif x >= 898 and y >= 276 and y < 497:
        tileID = 6
        tileX, tileY = 898, 276
    elif x >= 18 and x < 458 and y >= 497:
        tileID = 7
        tileX, tileY = 18, 497
    elif x >= 458 and x < 898 and y >= 497:
        tileID = 8
        tileX, tileY = 458, 497
    elif x >= 898 and y >= 497:
        tileID = 9
        tileX, tileY = 898, 497
    return tileID, tileX, tileY
    
    
def collission(x_player, y_player, ID, pSHAPE):
    global hitbox, tileColors
    global weakness_P
    global lives_P, iFrames_P,formStateLock_P
    global counter_round_total,roundX
    
    tileID, x_tile, y_tile = tileIdentity(x_player, y_player)
    xT = int(x_tile)
    yT = int(y_tile)
    xP = int(x_player)
    yP = int(y_player)

    offset = (xP - xT, yP - yT)
    result = hitbox[1].overlap(hitbox[2], offset)
    
    if result:
        if weakness_P[ID][0] == tileColors[tileID] or weakness_P[ID][1] == tileColors[tileID]:
            if ID == 1 and iFrames_P[1] == 0 and play_P[1] == True:
                SFX(4)
                print("HIT! Player ", ID)
                formStateLock_P[1] == True
                lives_P[1] -= 1
                shapeDisable(pSHAPE, ID)
                print("P1 Lives: ", lives_P[1])
                iFrames_P[1] = 90
                if lives_P[1] == 0:
                    SFX(7)
                    play_P[1] = False
                    counter_round_total[ID] = roundX
                    print("Player ", ID, " GAME OVER")
                    print(ID, counter_round_total[ID])
            if ID == 2 and iFrames_P[2] == 0 and play_P[2] == True:
                SFX(5)
                print("HIT! Player ", ID)
                formStateLock_P[2] == True
                lives_P[2] -= 1
                shapeDisable(pSHAPE, ID)
                print("P2 Lives: ", lives_P[2])
                iFrames_P[2] = 90
                if lives_P[2] == 0:
                    SFX(7)
                    play_P[2] = False
                    counter_round_total[ID] = roundX
                    print("Player ", ID, " GAME OVER")
                    print(ID, counter_round_total[ID])
            if ID == 3 and iFrames_P[3] == 0 and play_P[3] == True:
                SFX(6)
                print("HIT! Player ", ID)
                formStateLock_P[3] == True
                lives_P[3] -= 1
                shapeDisable(pSHAPE, ID)
                print("P3 Lives: ", lives_P[1])
                iFrames_P[3] = 90
                if lives_P[3] == 0:
                    SFX(7)
                    play_P[3] = False
                    counter_round_total[ID] = roundX
                    print("Player ", ID, " GAME OVER")
                    print(ID, counter_round_total[ID])

def shapeDisable(shape, ID):
    if shape == "CIR":
        shapeDisplay_Ticket[ID][1] = "X"
    if shape == "SQR":
        shapeDisplay_Ticket[ID][2] = "X"
    if shape == "TRI":
        shapeDisplay_Ticket[ID][3] = "X"
    if shape == "DIA":
        shapeDisplay_Ticket[ID][4] = "X"
    if shape == "PEN":
        shapeDisplay_Ticket[ID][5] = "X"
    if shape == "HEX":
        shapeDisplay_Ticket[ID][6] = "X"
    if shape == "HRT":
        shapeDisplay_Ticket[ID][7] = "X"

def roundCounter(roundX):
    global display_width, display_height
    if roundX < 10:
        x = display_width * 0.94
    elif roundX >= 10:
        x = display_width * 0.90
    y = display_height * 0.08
    font = pygame.font.Font('freesansbold.ttf', 100)
    text = font.render(str(roundX), True, (255,255,255,20))
    gameDisplay.blit(text,(x,y))

#--------------- TILES -------------------------------------
def tileMessanger(x,y,color):
    code = 0
    if x >= 18 and x < 458 and y >= 55 and y < 276:
        code = 1
    elif x >= 458 and x < 898 and y >= 55 and y < 276:
        code = 2
    elif x >= 898 and y >= 55 and y < 276:
        code = 3
    elif x >= 18 and x < 458 and y >= 276 and y < 497:
        code = 4
    elif x >= 458 and x < 898 and y >= 276 and y < 497:
        code = 5
    elif x >= 898 and y >= 276 and y < 497:
        code = 6
    elif x >= 18 and x < 458 and y >= 497:
        code = 7
    elif x >= 458 and x < 898 and y >= 497:
        code = 8
    elif x >= 898 and y >= 497:
        code = 9
    tileX(color, code)

def colorResponse(color):
    colorCode = "COLOR_X"
    
    if color == 1:
        colorCode = "YELLOW"
    if color == 2:
        colorCode = "VIOLET"
    if color == 3:
        colorCode = "BLUE"
    if color == 4:
        colorCode = "ORANGE"
    if color == 5:
        colorCode = "GREEN"
    if color == 6:
        colorCode = "RED"

    return colorCode
    
def tileX(color, code):
    global tileColors
    colorCode = colorResponse(color)
    tileColors[code] = colorCode

#-------------------- GAME LOOP ------------------------------------------------
def game_main():
    pygame.mixer.music.stop()
    musicBox = random.randrange(1,2)
    if musicBox == 1:
        pygame.mixer.music.load('rsc/03 - Lava Zone 1.mp3')
    if musicBox == 2:
        pygame.mixer.music.load('rsc/03 - Lava Zone 2.mp3')
    pygame.mixer.music.play(-1)

    x_P1, y_P1 = (display_width * 0.15),(display_height * 0.45)
    x_P2, y_P2 = (display_width * 0.45),(display_height * 0.45)
    x_P3, y_P3 = (display_width * 0.75),(display_height * 0.45)
    
    vel = 9
    dash = 21

    stateSHAPE_P = [0,1,1,1]
    drain_P = [0,0,0,0]

    global player_count
    global stateFloor
    global countdown, roundX
    global xY, yY, xV, yV, xB, yB, xO, yO, xG, yG, xR, yR
    global x1, y1, x2, y2, x3, y3
    global formState_P, formStateLock_P
    global pSHAPE
    global lives_P
    
    onGoing = True 
    while onGoing:
        #------------------- EVENT HANDLING ----------------------------------
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    quit()

        #--------- MOVEMENT -------------------------------------------------
        keys = pygame.key.get_pressed()
        #---------- PLAYER 1 -------------
        if keys[pygame.K_a] and x_P1 > 24:
            if keys[pygame.K_LSHIFT] and stamina_P[1] > 0:
                x_P1 -= dash
                drain_P[1] += 0.5
            else:
                x_P1 -= vel
                drain_P[1] = 0
        if keys[pygame.K_d] and x_P1 < 1255:
            if keys[pygame.K_LSHIFT] and stamina_P[1] > 10:
                x_P1 += dash
                drain_P[1] += 0.5
            else:
                x_P1 += vel
        if keys[pygame.K_s] and y_P1 < 633:
            if keys[pygame.K_LSHIFT] and stamina_P[1] > 10:
                y_P1 += dash
                drain_P[1] += 0.5
            else:
                y_P1 += vel
        if keys[pygame.K_w] and y_P1 > 60:
            if keys[pygame.K_LSHIFT] and stamina_P[1] > 10:
                y_P1 -= dash
                drain_P[1] += 0.5
            else:
                y_P1 -= vel
                
        if keys[pygame.K_TAB] and lives_P[1] == 2:
            if formStateLock_P[1] == False:
                SFX(1)
                stateSHAPE_P[1] += 1
            if stateSHAPE_P[1] > 6:
                stateSHAPE_P[1] = 1

        #---------- PLAYER 2 -------------
        if keys[pygame.K_h] and x_P2 > 24:
            if keys[pygame.K_o] and stamina_P[2] > 0:
                x_P2 -= dash
                drain_P[2] += 0.5
            else:
                x_P2 -= vel
                drain_P[2] = 0
        if keys[pygame.K_k] and x_P2 < 1255:
            if keys[pygame.K_o] and stamina_P[2] > 10:
                x_P2 += dash
                drain_P[2] += 0.5
            else:
                x_P2 += vel
        if keys[pygame.K_j] and y_P2 < 633:
            if keys[pygame.K_o] and stamina_P[2] > 10:
                y_P2 += dash
                drain_P[2] += 0.5
            else:
                y_P2 += vel
        if keys[pygame.K_u] and y_P2 > 60:
            if keys[pygame.K_o] and stamina_P[2] > 10:
                y_P2 -= dash
                drain_P[2] += 0.5
            else:
                y_P2 -= vel
                
        if keys[pygame.K_p] and lives_P[2] == 2:
            if formStateLock_P[2] == False:
                SFX(2)
                stateSHAPE_P[2] += 1
            if stateSHAPE_P[2] > 6:
                stateSHAPE_P[2] = 1

        #---------- PLAYER 3 -------------
        if keys[pygame.K_LEFT] and x_P3 > 24:
            if keys[pygame.K_KP2] and stamina_P[3] > 0:
                x_P3 -= dash
                drain_P[3] += 0.5
            else:
                x_P3 -= vel
                drain_P[3] = 0
        if keys[pygame.K_RIGHT] and x_P3 < 1255:
            if keys[pygame.K_KP2] and stamina_P[3] > 10:
                x_P3 += dash
                drain_P[3] += 0.5
            else:
                x_P3 += vel
        if keys[pygame.K_DOWN] and y_P2 < 633:
            if keys[pygame.K_KP2] and stamina_P[3] > 10:
                y_P3 += dash
                drain_P[3] += 0.5
            else:
                y_P3 += vel
        if keys[pygame.K_UP] and y_P3 > 60:
            if keys[pygame.K_KP2] and stamina_P[3] > 10:
                y_P3 -= dash
                drain_P[3] += 0.5
            else:
                y_P3 -= vel
                
        if keys[pygame.K_KP3] and lives_P[3] == 2:
            if formStateLock_P[3] == False:
                SFX(3)
                stateSHAPE_P[3] += 1
            if stateSHAPE_P[3] > 6:
                stateSHAPE_P[3] = 1
                
        #---------------------------------------------------------------------
        gameDisplay.fill(black)
        background()
    
        roundCounter(roundX)
            
        floorLava()
        randomLava(x1, y1, 1)
        randomLava(x2, y2, 2)
        randomLava(x3, y3, 3)
        
        boundariesMain()
        
        buttonSWITCH(stateSHAPE_P[1], 1, 148, 198)
        mShape_P(x_P1,y_P1,1)
        
        if player_count == 1:
            gameUI_A(formState_P[1])
            
        elif player_count == 2:
            buttonSWITCH(stateSHAPE_P[2], 2, 598, 648)
            mShape_P(x_P2,y_P2,2)
            gameUI_B(formState_P[1], formState_P[2])
            staminaHP(drain_P[2], 2)
            
            stamina_P[2] = staminaHP(drain_P[2], 2)
            
        elif player_count == 3:
            buttonSWITCH(stateSHAPE_P[2], 2, 598, 648)
            mShape_P(x_P2,y_P2,2)
            buttonSWITCH(stateSHAPE_P[3], 3, 1063, 1113)
            mShape_P(x_P3,y_P3,3)
            gameUI_C(formState_P[1], formState_P[2], formState_P[3])
            
            staminaHP(drain_P[2], 2)
            stamina_P[2] = staminaHP(drain_P[2], 2)
            staminaHP(drain_P[3], 3)
            stamina_P[3] = staminaHP(drain_P[3], 3)
        
        staminaHP(drain_P[1], 1)
        stamina_P[1] = staminaHP(drain_P[1], 1)
        
        iFrames_Decay()
        
        if roundX >= 0 and roundX <= 3:
            countdown += 1
        if roundX >= 4 and roundX <= 6:
            countdown += 2
        if roundX >= 7 and roundX <= 9:
            countdown += 3
        if roundX >= 10 and roundX <= 12:
            countdown += 4
        if roundX >= 13 and roundX <= 15:
            countdown += 5
        if roundX >= 16 and roundX <= 18:
            countdown += 6
        if roundX >= 19 and roundX <= 21:
            countdown += 7
        if roundX >= 22 and roundX <= 24:
            countdown += 8
        if roundX >= 25 and roundX <= 27:
            countdown += 9
        if roundX >= 28:
            countdown += 10
            
        stateFloor = 0

        #---------------------------------------------------------------------
        
        #----------------- LOGIC HANDLING -------------------------------------
        #------ COLLISSION -----------
        if countdown > 150 and countdown <= 250:
            collission(x_P1, y_P1, 1, pSHAPE[1])
            if player_count == 2:
                collission(x_P2, y_P2, 2, pSHAPE[2])
            if player_count == 3:
                collission(x_P2, y_P2, 2, pSHAPE[2])
                collission(x_P3, y_P3, 3, pSHAPE[3])

        #------ OTHERS ---------------
        if countdown > 250:
            countdown = 0
            roundX += 1
            stateFloor = 1
            spotSit.clear()
            lavaColor.clear()
            
        if stateFloor == 1:
            xY, yY = randomCord()
            xV, yV = randomCord()
            xB, yB = randomCord()
            xG, yG = randomCord()
            xO, yO = randomCord()
            xR, yR = randomCord()
            
            x1, y1 = randomCord()
            x2, y2 = randomCord()
            x3, y3 = randomCord()

        #------ CLOSING ---------------
        if player_count == 1:
            counter_round_total[1] = roundX
            if lives_P[1] == 0:
                closing_A()
        if player_count == 2:
            counter_round_total[0] = roundX+1
            if lives_P[1] == 0 and lives_P[2] >= 1:
                closing_B(2)
            if lives_P[2] == 0 and lives_P[1] >= 1:
                closing_B(2)
            if lives_P[1] == 0 and lives_P[2] == 0:
                closing_B(0)
        if player_count == 3:
            counter_round_total[0] = roundX+1
            if lives_P[1] >= 1 and lives_P[2] == 0 and lives_P[3] == 0:
                closing_C(1)
            if lives_P[1] == 0 and lives_P[2] >= 1 and lives_P[3] == 0:
                closing_C(2)
            if lives_P[1] == 0 and lives_P[2] == 0 and lives_P[3] >= 1:
                closing_C(3)
            if lives_P[1] == 0 and lives_P[2] == 0 and lives_P[3] == 0:
                closing_C(0)
        #----------------- END OF LOGIC HANDLING ------------------------------
        pygame.display.update()
        clock.tick(60)
        
#------------------------------------------------------------------------------
def closing_A():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('rsc/02 - Game Over.mp3')
    pygame.mixer.music.play(-1)
    
    global counter_round_total
    global closeAction
    global closing_message
    global background_INFO2
    global background_closing
    global countdown
    global roundX
    
    process = True
    while process:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    quit()
                    
        #---------------------------------------------------------------------
        gameDisplay.fill(black)
        
        if background_closing == 1:
            gameDisplay.blit(bgCA2,(15,15))
        elif background_closing == 2:
            gameDisplay.blit(bgCA3,(15,15))
        else:
            gameDisplay.blit(bgCA1,(15,15))

        if background_INFO2 == True:
            closing_statement(counter_round_total[1])
            
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        logo = pygame.image.load('img/4000 - Logo.png').convert_alpha()
        gameDisplay.blit(logo,(595,20))
        font = pygame.font.Font('rsc/LionelloR.ttf', 120)
        text_LOGO = font.render("GAME OVER", True, white)
        gameDisplay.blit(text_LOGO,(420,185))

        font1 = pygame.font.Font('rsc/Agency.ttf', 60)
        text_ROUND1 = font1.render("YOU", True, (255,255,255,20))
        text_ROUND2 = font1.render("LASTED", True, (255,255,255,20))
        gameDisplay.blit(text_ROUND1,(530,315))
        gameDisplay.blit(text_ROUND2,(470,370))

        if roundX >= 2 or roundX == 0:
            text_ROUND = font1.render("ROUNDS", True, (255,255,255,20))
            gameDisplay.blit(text_ROUND,(750,340))
        elif roundX == 1:
            text_ROUND = font1.render("ROUND", True, (255,255,255,20))
            gameDisplay.blit(text_ROUND,(750,340))
        
        font = pygame.font.Font('rsc/Agency.ttf', 130)
        text_ROUND = font.render(str(counter_round_total[1]), True, (255,255,255,20))
        textRECT = text_ROUND.get_rect()
        textRECT.center = (1355/2.02, 750/2)
        gameDisplay.blit(text_ROUND,textRECT)
        
        closing_buttons("RESTART", 502, 602, 490, 460, 1)
        closing_buttons("QUIT", 789, 602, 750, 460, 3)
        
        if closeAction != "none":
            process = False

        #---------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)

    if closeAction == "restart":
        reinitialization()
        prePlay()
    
def closing_buttons(msg,x_msg,y_msg,x_button,y_button,imgCode):
    global background_INFO2
    global background_closing
    global closeAction
    
    closingButton_Shape = [0,0,0,0,0,0]
    closingButton_Shape[1] = pygame.image.load('img/3311 - Diamond 4.png').convert_alpha()
    closingButton_Shape[2] = pygame.image.load('img/3311 - Diamond.png').convert_alpha()
    closingButton_Shape[3] = pygame.image.load('img/3311 - Hexagon 4.png').convert_alpha()
    closingButton_Shape[4] = pygame.image.load('img/3311 - Hexagon.png').convert_alpha()

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    font = pygame.font.Font('rsc/Agency.ttf', 40)
    text = font.render(msg, True, white)
    gameDisplay.blit(text,(x_msg,y_msg))

    font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
    text_INFO1 = font5.render("Prepare and try again.", True, white)
    text_INFO2 = font5.render("Leave the game.", True, white)

    if x_button+130 > mouse[0] > x_button and y_button+130 > mouse[1] > y_button:
        gameDisplay.blit(closingButton_Shape[imgCode+1],(x_button-15,y_button-20))
        if imgCode == 1:
            gameDisplay.blit(text_INFO1,(500,670))
            background_closing = 1
            background_INFO2 = False
        if imgCode == 3:
            gameDisplay.blit(text_INFO2,(550,670))
            background_closing = 2
            background_INFO2 = False

        if click[0] == 1 and imgCode == 1 and closeAction == "none":
            SFX(0)
            closeAction = "restart"
        elif click[0] == 1 and imgCode == 3 and closeAction == "none":
            pygame.quit()
            quit()
    else:
        gameDisplay.blit(closingButton_Shape[imgCode],(x_button,y_button))
        
    
def closing_statement(score):
    global closing_message
    
    font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
    text_FLUFF = [[0],
                  ["Don't worry. You'll get used to it.",
                  "Did you press the wrong key?",
                  "It may seem overwhelming at first.",
                  "Pathetic."],

                  ["That's an improvement, at least.",
                  "Starting to get the hang of it?",
                  "You can do better.",
                  "Is that it?"],

                  ["You're doing great.",
                  "Is it addicting?",
                  "Keep it up! You can surpass your past self!",
                  "You finally reached two digits."],

                  ["You're a pro now, You may quit anytime.",
                  "Amazing! Be proud of yourself.",
                  "You used to suck so bad.",
                  "Wonderful. Your price is an imaginary upvote."]]
        
    if score >= 0 and score <= 1:
        text_message = font5.render(text_FLUFF[1][closing_message], True, (255,255,255,20))
        textRECT = text_message.get_rect()
        textRECT.center = (1355/2.02, 690)
        gameDisplay.blit(text_message,textRECT)
    if score >= 2 and score <= 9:
        text_message = font5.render(text_FLUFF[2][closing_message], True, (255,255,255,20))
        textRECT = text_message.get_rect()
        textRECT.center = (1355/2.02, 690)
        gameDisplay.blit(text_message,textRECT)
    if score >= 10 and score <= 20:
        text_message = font5.render(text_FLUFF[3][closing_message], True, (255,255,255,20))
        textRECT = text_message.get_rect()
        textRECT.center = (1355/2.02, 690)
        gameDisplay.blit(text_message,textRECT)
    if score >= 21:
        text_message = font5.render(text_FLUFF[4][closing_message], True, (255,255,255,20))
        textRECT = text_message.get_rect()
        textRECT.center = (1355/2.02, 690)
        gameDisplay.blit(text_message,textRECT)

def closing_B(player):
    pygame.mixer.music.stop()
    pygame.mixer.music.load('rsc/02 - Game Over.mp3')
    pygame.mixer.music.play(-1)
    
    global counter_round_total
    global closeAction
    global closing_message
    global background_INFO2
    
    process = True
    while process:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    quit()
                    
        #---------------------------------------------------------------------
        gameDisplay.fill(black)
        
        if background_closing == 1:
            gameDisplay.blit(bgCA2,(15,15))
        elif background_closing == 2:
            gameDisplay.blit(bgCA3,(15,15))
        else:
            gameDisplay.blit(bgCA1,(15,15))
            
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        logo = pygame.image.load('img/4000 - Logo.png').convert_alpha()
        gameDisplay.blit(logo,(595,20))
        font = pygame.font.Font('rsc/LionelloR.ttf', 120)
        text_LOGO = font.render("GAME", True, white)
        gameDisplay.blit(text_LOGO,(553,205))
        text_LOGO = font.render("OVER", True, white)
        gameDisplay.blit(text_LOGO,(565,305))

        font1 = pygame.font.Font('rsc/Agency.ttf', 60)
        font2 = pygame.font.Font('rsc/Agency.ttf', 120)
        if player != 0:
            text_ROUND1 = font1.render("PLAYER", True, (255,255,255,20))
            text_ROUND2 = font2.render(str(player), True, (255,255,255,20))
            text_ROUND3 = font1.render("WON", True, (255,255,255,20))
            gameDisplay.blit(text_ROUND1,(610,400))
            gameDisplay.blit(text_ROUND2,(650,450))
            gameDisplay.blit(text_ROUND3,(635,550))
        else:
            text_ROUND1 = font2.render("DRAW", True, (255,255,255,20))
            text_ROUND2 = font1.render("NO ONE WON", True, (255,255,255,20))
            gameDisplay.blit(text_ROUND1,(576,415))
            gameDisplay.blit(text_ROUND2,(567,520))

        if background_INFO2 == True:
            font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
            if counter_round_total[0] == 0:
                text_roundEnd = "The game immediately ended."
            elif counter_round_total[0] == 1:
                text_roundEnd = "The game only lasted 1 round."
            else:
                text_roundEnd = "The game lasted for {} rounds."
            text_message = font5.render(text_roundEnd.format(counter_round_total[0]), True, (255,255,255,20))
            textRECT = text_message.get_rect()
            textRECT.center = (1355/2.02, 690)
            gameDisplay.blit(text_message,textRECT)
        
        closing_buttons("RESTART", 112, 680, 96, 540, 1)
        closing_buttons("QUIT", 1172, 680, 1132, 540, 3)
        
        if closeAction != "none":
            process = False

        #---------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)

    if closeAction == "restart":
        reinitialization()
        prePlay()

def closing_C(player):
    pygame.mixer.music.stop()
    pygame.mixer.music.load('rsc/02 - Game Over.mp3')
    pygame.mixer.music.play(-1)
    
    global counter_round_total
    global closeAction
    global closing_message
    global background_INFO2
    
    process = True
    while process:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pygame.quit()
                    quit()
                    
        #---------------------------------------------------------------------
        gameDisplay.fill(black)
        
        if background_closing == 1:
            gameDisplay.blit(bgCA2,(15,15))
        elif background_closing == 2:
            gameDisplay.blit(bgCA3,(15,15))
        else:
            gameDisplay.blit(bgCA1,(15,15))
            
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        logo = pygame.image.load('img/4000 - Logo 2.png').convert_alpha()
        gameDisplay.blit(logo,(25,20))
        font1 = pygame.font.Font('rsc/LionelloR.ttf', 80)
        text_LOGO = font1.render("GAME OVER", True, white)
        gameDisplay.blit(text_LOGO,(125,27))

        font1 = pygame.font.Font('rsc/Agency.ttf', 60)
        font2 = pygame.font.Font('rsc/Agency.ttf', 120)
        font3 = pygame.font.Font('rsc/Agency.ttf', 50)
        if player != 0:
            txt = "PLAYER {} WON!"
            text_LOBBY = font3.render(txt.format(player), True, white)
            gameDisplay.blit(text_LOBBY,(465,47))
            
        else:
            txt = "DRAW. NO ONE WON."
            text_LOBBY = font3.render(txt.format(player), True, white)
            gameDisplay.blit(text_LOBBY,(465,47))

        text_ROUND1 = font1.render("PLAYER 1", True, (255,255,255,20))
        gameDisplay.blit(text_ROUND1,(105,150))
        text_ROUND2 = font3.render("SHAPES:", True, (255,255,255,20))
        gameDisplay.blit(text_ROUND2,(105,200))

        closing_shapeDisplay(1)

        txt_P1 = "ROUNDS: {}"
        if player == 1:
            text_ROUND3 = font3.render(txt_P1.format(counter_round_total[0]), True, (255,255,255,20))
        else:
            text_ROUND3 = font3.render(txt_P1.format(counter_round_total[1]), True, (255,255,255,20))
        gameDisplay.blit(text_ROUND3,(105,380))

        #-------------------------------------------------------------
        text_ROUND4 = font1.render("PLAYER 2", True, (255,255,255,20))
        gameDisplay.blit(text_ROUND4,(105+420,150))
        text_ROUND5 = font3.render("SHAPES:", True, (255,255,255,20))
        gameDisplay.blit(text_ROUND5,(105+420,200))

        closing_shapeDisplay(2)

        txt_P2 = "ROUNDS: {}"
        if player == 2:
            text_ROUND6 = font3.render(txt_P2.format(counter_round_total[0]), True, (255,255,255,20))
        else:
            text_ROUND6 = font3.render(txt_P2.format(counter_round_total[2]), True, (255,255,255,20))
        gameDisplay.blit(text_ROUND6,(105+420,380))

        #-------------------------------------------------------------
        text_ROUND7 = font1.render("PLAYER 3", True, (255,255,255,20))
        gameDisplay.blit(text_ROUND7,(105+420+420,150))
        text_ROUND8 = font3.render("SHAPES:", True, (255,255,255,20))
        gameDisplay.blit(text_ROUND8,(105+420+420,200))

        closing_shapeDisplay(3)

        txt_P3 = "ROUNDS: {}"
        if player == 3:
            text_ROUND9 = font3.render(txt_P3.format(counter_round_total[0]), True, (255,255,255,20))
        else:
            text_ROUND9 = font3.render(txt_P3.format(counter_round_total[3]), True, (255,255,255,20))
        gameDisplay.blit(text_ROUND9,(105+420+420,380))

        #-------------------------------------------------------------
        if background_INFO2 == True:
            font5 = pygame.font.Font('rsc/CaviarDreams.ttf', 35)
            if counter_round_total[0] == 0:
                text_roundEnd = "The game immediately ended."
            elif counter_round_total[0] == 1:
                text_roundEnd = "The game only lasted 1 round."
            else:
                text_roundEnd = "The game lasted for {} rounds."
            text_message = font5.render(text_roundEnd.format(counter_round_total[0]), True, (255,255,255,20))
            textRECT = text_message.get_rect()
            textRECT.center = (1355/2.02, 690)
            gameDisplay.blit(text_message,textRECT)
        
        closing_buttons("RESTART", 112, 680, 96, 540, 1)
        closing_buttons("QUIT", 1172, 680, 1132, 540, 3)
        
        if closeAction != "none":
            process = False

        #---------------------------------------------------------------------
        pygame.display.update()
        clock.tick(60)

    if closeAction == "restart":
        reinitialization()
        prePlay()

def closing_shapeDisplay(ID):
    global player_SHAPE
    global customShape

    if ID == 1:
        x = 135
        y = 260
    if ID == 2:
        x = 135+420
        y = 260
    if ID == 3:
        x = 135+420+420
        y = 260
        
    ctr = 1
    while ctr <= 14:
        if player_SHAPE[ID][0] == ctr:
            gameDisplay.blit(customShape[ctr],(x,y))
        if player_SHAPE[ID][1] == ctr:
            gameDisplay.blit(customShape[ctr],(x+120,y))
        ctr += 1

def reinitialization():
    global roundX,player_count,player_SHAPE,stamina_P,stateFloor,countdown
    global customShape_Ticket,armory_Ticket,dress_Ticket,spot1_TAKEN,background_menu
    global background_INFO1,menuAction,closeAction,background_INFO2,start_game
    global shape_on_play,counter_round_total,lives_P,play_P,iFrames_P,pSHAPE,background_closing

    roundX = 0
    player_count = 1
    player_SHAPE = [[0],[0,0],[0,0],[0,0]]
    stamina_P = [0,200,200,200]
    stateFloor = 0
    countdown = 0
    customShape_Ticket = [[0],
                   ["X","X","X","X","X","X","X","X"],
                   ["X","X","X","X","X","X","X","X"],
                   ["X","X","X","X","X","X","X","X"]] 
    armory_Ticket = [0,0,0,0]
    dress_Ticket = [[0],
                    [0,1,1,1,1,1,1,1],
                    [0,1,1,1,1,1,1,1],
                    [0,1,1,1,1,1,1,1]]
    spot1_TAKEN = [[0],
                   ["NO",0,0,0,0,0,0,0],
                   ["NO",0,0,0,0,0,0,0],
                   ["NO",0,0,0,0,0,0,0]] 
    background_menu = 0
    background_INFO1 = True
    menuAction = "none"
    closeAction = "none"
    background_INFO2 = True 
    start_game = False
    shape_on_play = 0
    counter_round_total = [0,0,0,0]
    lives_P = [0,2,2,2]
    play_P = [0,True,True,True]
    iFrames_P = [0,0,0,0]
    pSHAPE = ["X","X","X","X"]
    background_closing = 0

    pygame.mixer.music.stop()
    pygame.mixer.music.load('rsc/01 - Main Menu.mp3')
    pygame.mixer.music.play(-1)
    
#------------------------------------------------------------------------------        
game_intro()

#- END --------------------------
pygame.quit()
quit()
