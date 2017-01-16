from time import sleep
import random
from graphics import *
import winsound

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#
# THIS WAS CREATED BEFORE I LEARNED OOP OR PROPER FUNCTIONAL PROGRAMMING. IT SUCKS, WHICH IS WHY IT IS UNFINISHED
#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

gamewin = GraphWin("                                                                                                        Colwell's Quest!",800,608)
colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
#char.setFill('#000000')
overworld = Image(Point(-496,1006),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\OverworldFORREAL(WIP)3.gif')
overworld.draw(gamewin)
colwell.draw(gamewin)
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#           START OF CONTROLLER CODE            START OF CONTROLLER CODE
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#CONTROLLER DEFAULT ELEMENTS
MES = GraphWin('MES Controller',324,150)
Controller = Image(Point(162,75),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\MES CONTROLLER.gif')
Controller.draw(MES)
dpadLEFT = Text(Point(42,91),'A')
dpadRIGHT = Text(Point(74,91),'D')
dpadUP = Text(Point(58,75),'W')
dpadDOWN = Text(Point(58,107),'S')
dpadLEFT.setTextColor('#ffffff')
dpadRIGHT.setTextColor('#ffffff')
dpadUP.setTextColor('#ffffff')
dpadDOWN.setTextColor('#ffffff')
dpadLEFT.draw(MES)
dpadRIGHT.draw(MES)
dpadUP.draw(MES)
dpadDOWN.draw(MES)
START = Text(Point(188,119),'RETURN')
SELECT = Text(Point(132,119),'SHIFT_L')
START.setTextColor('#ff0000')
SELECT.setTextColor('#ff0000')
START.draw(MES)
SELECT.draw(MES)
B_BUTTON = Text(Point(240,108),'K')
A_BUTTON = Text(Point(288,108),'L')
A_BUTTON.setTextColor('#ffffff')
B_BUTTON.setTextColor('#ffffff')
A_BUTTON.draw(MES)
B_BUTTON.draw(MES)
MONID = 0

#DEFAULT BUTTON MAPPING - - - - - - - - - - - - - - - - - -
NEWdpadLEFT = 'a'
NEWdpadRIGHT = 'd'
NEWdpadUP = 'w'
NEWdpadDOWN = 's'
NEWSTART = 'Return'
NEWSELECT = 'Shift_L'
NEWA_BUTTON = 'l'
NEWB_BUTTON = 'k'
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Default stats - - - - - - - - - - - - - - - - - - - - - - -
HPtotal = 10#10
ATK = 3#3
DEF = 1#1
MATK = 2#2
MDEF = 0#0
SPD = 7#7
MPtotal = 15#15
EXP = 0#0
EXPnext = 17#17
LVL = 1#1
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


def ControllerMapping():
    global NEWdpadLEFT
    global NEWdpadRIGHT
    global NEWdpadUP
    global NEWdpadDOWN
    global NEWSTART
    global NEWSELECT
    global NEWA_BUTTON
    global NEWB_BUTTON
    click = MES.checkMouse()
    try:
        clickx = click.getX()
        clicky = click.getY()
        if clickx >= 24:
            if clickx <= 43:
                if clicky >= 77:
                    if clicky <= 104:
                        dpadLEFT.setTextColor('#ff0000')
                        NEWdpadLEFT = MES.getKey()
                        dpadLEFT.setText(NEWdpadLEFT.upper())
                        dpadLEFT.setTextColor('#ffffff')
        if clickx >= 72:
            if clickx <= 91:
                if clicky >= 77:
                    if clicky <= 104:
                        dpadRIGHT.setTextColor('#ff0000')
                        NEWdpadRIGHT = MES.getKey()
                        dpadRIGHT.setText(NEWdpadRIGHT.upper())
                        dpadRIGHT.setTextColor('#ffffff')
        if clickx >= 44:
            if clickx <= 71:
                if clicky >= 57:
                    if clicky <= 76:
                        dpadUP.setTextColor('#ff0000')
                        NEWdpadUP = MES.getKey()
                        dpadUP.setText(NEWdpadUP.upper())
                        dpadUP.setTextColor('#ffffff')
                if clicky >= 105:
                    if clicky <=124:
                        dpadDOWN.setTextColor('#ff0000')
                        NEWdpadDOWN = MES.getKey()
                        dpadDOWN.setText(NEWdpadDOWN.upper())
                        dpadDOWN.setTextColor('#ffffff')
        if clickx >= 120:
            if clickx <= 148:
                if clicky >= 100:
                    if clicky <= 109:
                        SELECT.setTextColor('#ffffff')
                        NEWSELECT = MES.getKey()
                        SELECT.setText(NEWSELECT.upper())
                        SELECT.setTextColor('#ff0000')
        if clickx >= 166:
            if clickx <= 194:
                if clicky >= 100:
                    if clicky <= 109:
                        START.setTextColor('#ffffff')
                        NEWSTART = MES.getKey()
                        START.setText(NEWSTART.upper())
                        START.setTextColor('#ff0000')
        if clicky >= 87:
            if clicky <= 129:
                if clickx >= 219:
                    if clickx <= 261:
                        B_BUTTON.setTextColor('#000000')
                        NEWB_BUTTON = MES.getKey()
                        B_BUTTON.setText(NEWB_BUTTON.upper())
                        B_BUTTON.setTextColor('#ffffff')
                if clickx >= 267:
                    if clickx <= 309:
                        A_BUTTON.setTextColor('#000000')
                        NEWA_BUTTON = MES.getKey()
                        A_BUTTON.setText(NEWA_BUTTON.upper())
                        A_BUTTON.setTextColor('#ffffff')
            
    except:
        pass

def Battle():
    global HPtotal
    global HP
    global MPtotal
    global MP
    global ATK
    global DEF
    global MATK
    global MDEF
    global SPD
    global EXP
    global LVL
    global EXPnext
    global MONID
    MONHPD = {0:1, 1:3, 2:4, 11:25, 21:337}
    MONMPD = {0:12, 1:0, 2:0, 11:0, 21:7000}
    MONATKD = {0:1, 1:2, 2:3, 11:3, 21:24}
    MONDEFD = {0:1, 1:1, 2:1, 11:2, 21:14}
    MONMATKD = {0:2, 1:3, 2:1, 11:1, 21:69}
    MONMDEFD = {0:0, 1:0, 2:1, 11:1, 21:23}
    MONSPDD = {0:5, 1:6, 2:8, 11:1, 21:1234567890}
    MEXPD = {0:12, 1:5, 2:11, 11:25, 21:666}
    MONHP = MONHPD[MONID]
    MONMP = MONMPD[MONID]
    MONATK = MONATKD[MONID]
    MONDEF = MONDEFD[MONID]
    MONMATK = MONMATKD[MONID]
    MONMDEF = MONMDEFD[MONID]
    MONSPD = MONSPDD[MONID]
    MEXP = MEXPD[MONID]
    MONHPtotal = MONHP
    BattleBG = Rectangle(Point(0,0),Point(800,608))
    BattleBG.setFill('#000000')
    BattleBG.draw(gamewin)
    if MONID == 0:
        Enemy = Image(Point(400,202),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\NotFound.gif')
    if MONID == 1:
        Enemy = Image(Point(400,202),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Bat.gif')
    if MONID == 2:
        Enemy = Image(Point(400,202),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Sailor Spectre.gif')
    if MONID == 11:
        Enemy = Image(Point(400,202),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\LightHouseKeeperBATTLE.gif')
    if MONID == 21:
        Enemy = Image(Point(400,202),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Nathan.gif')
    Enemy.draw(gamewin)
    BattleBox = Rectangle(Point(0,400),Point(800,408))
    BattleBox.setOutline('#ffffff')
    BattleBox.setFill('#ffffff')
    BattleBox.draw(gamewin)
    BattleBox2 = Rectangle(Point(496,404),Point(504,608))
    BattleBox2.setFill('#ffffff')
    BattleBox2.setOutline('#ffffff')
    BattleBox2.draw(gamewin)
    ATKtext = Text(Point(100,450),'Attack')
    MGCtext = Text(Point(100,500),'Magic')
    DEFtext = Text(Point(100,550),'Defense')
    ATKtext.setTextColor('#ffffff')
    MGCtext.setTextColor('#ffffff')
    DEFtext.setTextColor('#ffffff')
    ATKtext.setSize(30)
    DEFtext.setSize(30)
    MGCtext.setSize(30)
    ATKtext.draw(gamewin)
    MGCtext.draw(gamewin)
    DEFtext.draw(gamewin)
    SelectionBox = Rectangle(Point(20,420),Point(180,475))
    SelectionBox.setOutline('#ffffff')
    SelectionBox.draw(gamewin)
    HPtext = Text(Point(550,500),'HP: ')
    HPtext.setTextColor('#ffffff')
    HPtext.setSize(25)
    HPtext.draw(gamewin)
    MPtext = Text(Point(550,550),'MP: ')
    MPtext.setTextColor('#ffffff')
    MPtext.setSize(25)
    MPtext.draw(gamewin)
    HPvalue = Text(Point(610,500), HP)
    MPvalue = Text(Point(610,550), MP)
    HPvalue.setTextColor('#ffffff')
    MPvalue.setTextColor('#ffffff')
    HPvalue.setSize(23)
    MPvalue.setSize(23)
    HPvalue.draw(gamewin)
    MPvalue.draw(gamewin)
    BTLx = 0
    BTLy = 0
    Defended = 0
    Battleover = 0
    BATTLEISGO = 1
    if SPD > MONSPD:
        PLYRturnOver = 0
    else:
        PLYRturnOver = 1
    while BATTLEISGO == 1:
        ControllerMapping()
        keypress = MES.checkKey()
        try:
            if keypress == NEWdpadDOWN:
                if BTLx < 2:
                    SelectionBox.move(0,50)
                    BTLx = BTLx + 1
                if BTLx > 2:
                    SelectionBox.move(0,-100)
                    BTLx = BTLx - 2
            if keypress == NEWdpadUP:
                if BTLx > 0:
                    SelectionBox.move(0,-50)
                    BTLx = BTLx - 1
                if BTLx < 0:
                    SelectionBox.move(0,100)
                    BTLx = BTLx + 2
        except:
            pass
        try:
            if keypress == NEWA_BUTTON:
                if BTLx == 0:
                    if Battleover == 0:
                        time.sleep(0.5)
                        EnemyDMGtext = Text(Point(random.randrange(450,475,1),random.randrange(200,250,1)),ATK-MONDEF)
                        EnemyDMGtext.setTextColor('#ff0000')
                        EnemyDMGtext.setSize(36)
                        EnemyDMGtext.draw(gamewin)
                        MONHP = MONHP - (ATK - MONDEF)
                        time.sleep(0.4)
                        EnemyDMGtext.undraw()
                        PLYRturnOver = 1
                if BTLx == 1:
                    if Battleover == 0:
                        MBTLx = 0
                        MagicCanceled = 0
                        MGChealtext = Text(Point(300,425),'Heal')
                        MGChealtext.setTextColor('#ffffff')
                        MGChealtext.setSize(15)
                        MGChealtext.draw(gamewin)
                        MGCfiretext = Text(Point(300,465),'Fire Blast')
                        MGCfiretext.setTextColor('#ffffff')
                        MGCfiretext.setSize(15)
                        MGCfiretext.draw(gamewin)
                        if MGCtremor == 1:
                            MGCtremortext = Text(Point(300,505),'Tremor')
                            MGCtremortext.setTextColor('#ffffff')
                            MGCtremortext.setSize(15)
                            MGCtremortext.draw(gamewin)
                        if MGCflood == 1:
                            MGCfloodtext = Text(Point(300,545),'Flood')
                            MGCfloodtext.setTextColor('#ffffff')
                            MGCfloodtext.setSize(15)
                            MGCfloodtext.draw(gamewin)
                        if MGClifedrain == 1:
                            MGClifedraintext = Text(Point(300,585),'Life Drain')
                            MGClifedraintext.setTextColor('#ffffff')
                            MGClifedraintext.setSize(15)
                            MGClifedraintext.draw(gamewin)
                        Magicbox = Rectangle(Point(200,415),Point(400,435))
                        Magicbox.setOutline('#ffffff')
                        Magicbox.draw(gamewin)
                        while MagicCanceled == 0:
                            ControllerMapping()
                            keypress = MES.checkKey()
                            try:
                                if keypress == NEWB_BUTTON:
                                    MagicCanceled = 1
                                    Magicbox.undraw()
                                    MGCfiretext.undraw()
                                    MGChealtext.undraw()
                                    try:
                                        MGCtremortext.undraw()
                                    except:
                                        pass
                                    try:
                                        MGCfloodtext.undraw()
                                    except:
                                        pass
                                    try:
                                        MGClifedraintext.undraw()
                                    except:
                                        pass
                                if keypress == NEWdpadDOWN:
                                    if MBTLx < 4:
                                        Magicbox.move(0,40)
                                        MBTLx = MBTLx + 1
                                    if MBTLx > 4:
                                        Magicboxox.move(0,-160)
                                        MBTLx = MBTLx - 3
                                if keypress == NEWdpadUP:
                                    if MBTLx > 0:
                                        Magicbox.move(0,-40)
                                        MBTLx = MBTLx - 1
                                    if MBTLx < 0:
                                        Magicbox.move(0,160)
                                        MBTLx = MBTLx + 3
                            except:
                                pass
                            try:
                                if keypress == NEWA_BUTTON:
                                    if MBTLx == 0:
                                        if MP > 2:
                                            time.sleep(0.5)
                                            HPgained = HPtotal//4
                                            Health1 = Image(Point(400,286),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\health+1.gif')
                                            Health1.draw(gamewin)
                                            time.sleep(0.1)
                                            Health1.undraw()
                                            Health2 = Image(Point(400,286),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\health+2.gif')
                                            Health2.draw(gamewin)
                                            time.sleep(0.1)
                                            Health2.undraw()
                                            Health3 = Image(Point(400,286),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\health+3.gif')
                                            Health3.draw(gamewin)
                                            time.sleep(0.1)
                                            Health3.undraw()
                                            Health4 = Image(Point(400,286),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\health+4.gif')
                                            Health4.draw(gamewin)
                                            time.sleep(0.1)
                                            Health4.undraw()
                                            Health5 = Image(Point(400,286),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\health+5.gif')
                                            Health5.draw(gamewin)
                                            time.sleep(0.1)
                                            Health5.undraw()
                                            PlayerHPtext = Text(Point(random.randrange(450,475,1),random.randrange(200,250,1)),HPgained)
                                            PlayerHPtext.setTextColor('#00ffff')
                                            PlayerHPtext.setSize(36)
                                            PlayerHPtext.draw(gamewin)
                                            time.sleep(0.4)
                                            PlayerHPtext.undraw()
                                            MagicCanceled = 1
                                            PLYRturnOver = 1
                                            HP = HP + HPgained
                                            MP = MP - 2
                                            if MP < 0:
                                                MP = 0
                                            if HP > HPtotal:
                                                HP = HPtotal
                                            HPvalue.setText(HP)
                                            MPvalue.setText(MP)
                                    if MBTLx == 1:
                                        if MP >= 3:
                                            time.sleep(0.5)
                                            Fire1 = Image(Point(370,350),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Fire.gif')
                                            Fire1.draw(gamewin)
                                            time.sleep(0.05)
                                            Fire2 = Image(Point(400,350),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Fire.gif')
                                            Fire2.draw(gamewin)
                                            time.sleep(0.05)
                                            Fire1.undraw()
                                            Fire3 = Image(Point(430,350),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Fire.gif')
                                            Fire3.draw(gamewin)
                                            time.sleep(0.05)
                                            Fire2.undraw()
                                            time.sleep(0.2)
                                            Fire3.undraw()
                                            EnemyDMGtext = Text(Point(random.randrange(450,475,1),random.randrange(200,250,1)),MATK-MONMDEF)
                                            EnemyDMGtext.setTextColor('#ff0000')
                                            EnemyDMGtext.setSize(36)
                                            EnemyDMGtext.draw(gamewin)
                                            MONHP = MONHP - (MATK - MONMDEF)
                                            time.sleep(0.4)
                                            EnemyDMGtext.undraw()
                                            PLYRturnOver = 1
                                            MagicCanceled = 1
                                            MP = MP - 3
                                            if MP < 0:
                                                MP = 0
                                            MPvalue.setText(MP)
                                    if MBTLx == 2:
                                        if MGCtremor == 1:
                                            if MP >= 6:
                                                time.sleep(0.5)
                                                EnemyShake = 10
                                                while EnemyShake > 0:
                                                    Enemy.move(5,0)
                                                    time.sleep(0.033)
                                                    Enemy.move(-5,0)
                                                    time.sleep(0.033)
                                                    Enemy.move(-5,0)
                                                    time.sleep(0.033)
                                                    Enemy.move(5,0)
                                                    time.sleep(0.033)
                                                    EnemyShake = EnemyShake - 1
                                                EnemyDMGtext = Text(Point(random.randrange(450,475,1),random.randrange(200,250,1)),(MATK + 3)-MONMDEF)
                                                EnemyDMGtext.setTextColor('#ff0000')
                                                EnemyDMGtext.setSize(36)
                                                EnemyDMGtext.draw(gamewin)
                                                MONHP = MONHP - ((MATK * (MATK/MDEF) - MONMDEF))
                                                time.sleep(0.4)
                                                EnemyDMGtext.undraw()
                                                MagicCanceled = 1
                                                PLYRturnOver = 1
                                                MP = MP - 6
                                                if MP < 0:
                                                    MP = 0
                                                MPvalue.setText(MP)
                                    if MBTLx == 3:
                                        if MGCflood == 1:
                                            if MP >= 11:
                                                time.sleep(0.5)
                                                Flood1 = Image(Point(400,350),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Water.gif')
                                                Flood1.draw(gamewin)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                time.sleep(0.033)
                                                Flood2 = Image(Point(400,350),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Water.gif')
                                                Flood2.draw(gamewin)
                                                Flood1.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                Flood2.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                Flood2.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                Flood2.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                Flood2.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                Flood2.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.move(0,-4)
                                                Flood2.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3 = Image(Point(400,350),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Water.gif')
                                                Flood3.draw(gamewin)
                                                Flood1.move(0,-4)
                                                Flood2.move(0,-4)
                                                time.sleep(0.033)
                                                Flood1.undraw()
                                                Flood2.move(0,-4)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood2.move(0,-4)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood2.move(0,-4)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood2.move(0,-4)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood2.move(0,-4)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood2.move(0,-4)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood2.undraw()
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3.move(0,-4)
                                                time.sleep(0.033)
                                                Flood3.undraw()
                                                EnemyDMGtext = Text(Point(random.randrange(450,475,1),random.randrange(200,250,1)),(MATK+7)-MONMDEF)
                                                EnemyDMGtext.setTextColor('#ff0000')
                                                EnemyDMGtext.setSize(36)
                                                EnemyDMGtext.draw(gamewin)
                                                MONHP = MONHP - ((MATK * (MATK-MONMDEF)) - MONMDEF)
                                                time.sleep(0.4)
                                                EnemyDMGtext.undraw()
                                                PLYRturnOver = 1
                                                MagicCanceled = 1
                                                MP = MP - 11
                                                if MP < 0:
                                                    MP = 0
                                                MPvalue.setText(MP)
                                    if MBTLx == 4:
                                        if MGClifedrain == 1:
                                            if MP >= 25:
                                                time.sleep(0.5)
                                                Drain1 = Image(Point(400,300),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Drain1.gif')
                                                Drain1.draw(gamewin)
                                                time.sleep(0.033)
                                                Drain1.undraw()
                                                Drain2 = Image(Point(400,300),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Drain2.gif')
                                                Drain2.draw(gamewin)
                                                time.sleep(0.033)
                                                Drain2.undraw()
                                                Drain3 = Image(Point(400,300),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Drain3.gif')
                                                Drain3.draw(gamewin)
                                                time.sleep(0.033)
                                                Drain3.undraw()
                                                Drain4 = Image(Point(400,300),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Drain4.gif')
                                                Drain4.draw(gamewin)
                                                time.sleep(0.033)
                                                Drain4.undraw()
                                                Drain5 = Image(Point(400,300),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Drain5.gif')
                                                Drain5.draw(gamewin)
                                                time.sleep(0.033)
                                                Drain5.undraw()
                                                Drain6 = Image(Point(400,300),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Drain6.gif')
                                                Drain6.draw(gamewin)
                                                time.sleep(0.033)
                                                Drain6.undraw()
                                                EnemyDMGtext = Text(Point(random.randrange(450,475,1),random.randrange(200,250,1)),(MATK * 2)-MONMDEF)
                                                EnemyDMGtext.setTextColor('#ff0000')
                                                EnemyDMGtext.setSize(36)
                                                EnemyDMGtext.draw(gamewin)
                                                MONHP = MONHP - ((MATK * 2) - MONMDEF)
                                                HP = HP + (((MATK * 2) - MONMDEF)//3)
                                                time.sleep(0.4)
                                                EnemyDMGtext.undraw()
                                                PLYRturnOver = 1
                                                MagicCanceled = 1
                                                MP = MP - 17
                                                if MP < 0:
                                                    MP = 0
                                                if HP > HPtotal:
                                                    HP = HPtotal
                                                MPvalue.setText(MP)
                                                HPvalue.setText(HP)
                                    if MagicCanceled == 1:
                                        Magicbox.undraw()
                                        MGCfiretext.undraw()
                                        MGChealtext.undraw()
                                        try:
                                            MGCtremortext.undraw()
                                        except:
                                            pass
                                        try:
                                            MGCfloodtext.undraw()
                                        except:
                                            pass
                                        try:
                                            MGClifedraintext.undraw()
                                        except:
                                            pass
                            except:
                                pass
                            time.sleep(0.0166)
                if BTLx == 2:
                    if Battleover == 0:
                        DEFDEF = DEF + (DEF//5)
                        PLYRturnOver = 1
                        Defended = 1
                        Shield = Image(Point(400,250),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\Sheild.gif')
                        Shield.draw(gamewin)
                        time.sleep(0.5)
                        Shield.undraw()
        except:
            pass
        if MONHP <= 0:
            Battleover = 1
            Enemy.undraw()
            EXP = EXP + MEXP
            EXPtext = Text(Point(650,585),'You gained      EXP')
            EXPtext.setTextColor('#ffffff')
            EXPtext.setSize(25)
            EXPtext.draw(gamewin)
            EXPgained = Text(Point(700,585),MEXP)
            EXPgained.setTextColor('#ffffff')
            EXPgained.setSize(25)
            EXPgained.draw(gamewin)
            time.sleep(1)
            if EXP > EXPnext:
                EXPgained.undraw()
                EXPtext.undraw()
                Leveled = Text(Point(650,585),'You Leveled up!')
                Leveled.setTextColor('#ffffff')
                Leveled.setSize(25)
                Leveled.draw(gamewin)
                time.sleep(1)
                Leveled.undraw()
                NewLevel = 'You are LVL: ' + str(LVL+1)
                NewLeveled = Text(Point(650,585), NewLevel)
                NewLeveled.setTextColor('#ffffff')
                NewLeveled.setSize(25)
                NewLeveled.draw(gamewin)
                time.sleep(1)
                NewLeveled.undraw()
                LVL = LVL + 1
                LevelUp()
            EXPgained.undraw()
            EXPtext.undraw()
            BATTLEISGO = 0
        if PLYRturnOver == 1:
            if MP < MPtotal:
                time.sleep(0.5)
                MP = MP + 1
                MPvalue.setText(MP)
            if Battleover == 0:
                time.sleep(0.5)
                if Defended == 0:
                    HP = HP - (MONATK - DEF)
                    Dealt = Text(Point(random.randrange(645,656,1),random.randrange(370,380,1)),(MONATK-DEF))
                    Dealt.setTextColor('#ff0000')
                    Dealt.setSize(36)
                    Dealt.draw(gamewin)
                    time.sleep(0.4)
                    Dealt.undraw()
                    HPvalue.setText(HP) 
                if Defended == 1:
                    HP = HP - (MONATK - DEFDEF)
                    Dealt = Text(Point(random.randrange(645,656,1),random.randrange(370,380,1)),(MONATK-DEFDEF))
                    Dealt.setTextColor('#ff0000')
                    Dealt.setSize(36)
                    Dealt.draw(gamewin)
                    time.sleep(0.4)
                    Dealt.undraw()
                    HPvalue.setText(HP)
                    Defended = 0
                PLYRturnOver = 0
        if HP <= 0:
            HPvalue.setText(0)
            time.sleep(0.4)
            DEAD = Text(Point(400,304),'GAMEOVER!')
            DEAD.setTextColor('#ff0000')
            DEAD.setSize(36)
            Cover = Rectangle(Point(0,0),Point(800,608))
            Cover.setFill('#000000')
            Cover.draw(gamewin)
            DEAD.draw(gamewin)
            time.sleep(1)
            DEAD.setSize(35)
            time.sleep(0.033)
            DEAD.setSize(33)
            time.sleep(0.033)
            DEAD.setSize(30)
            time.sleep(0.033)
            DEAD.setSize(26)
            time.sleep(0.033)
            DEAD.setSize(21)
            time.sleep(0.033)
            DEAD.setSize(15)
            time.sleep(0.033)
            DEAD.setSize(8)
            time.sleep(0.033)
            DEAD.undraw()
            time.sleep(3)
            END = Text(Point(400,456),'You are dead, Nathan reigns supreme...')
            END.setTextColor('#ffffff')
            END.setSize(16)
            END.draw(gamewin)
            time.sleep(5)
            END.setTextColor('#eeeeee')
            time.sleep(0.033)
            END.setTextColor('#dddddd')
            time.sleep(0.033)
            END.setTextColor('#cccccc')
            time.sleep(0.033)
            END.setTextColor('#bbbbbb')
            time.sleep(0.033)
            END.setTextColor('#aaaaaa')
            time.sleep(0.033)
            END.setTextColor('#999999')
            time.sleep(0.033)
            END.setTextColor('#888888')
            time.sleep(0.033)
            END.setTextColor('#777777')
            time.sleep(0.033)
            END.setTextColor('#666666')
            time.sleep(0.033)
            END.setTextColor('#555555')
            time.sleep(0.033)
            END.setTextColor('#444444')
            time.sleep(0.033)
            END.setTextColor('#333333')
            time.sleep(0.033)
            END.setTextColor('#222222')
            time.sleep(0.033)
            END.setTextColor('#111111')
            time.sleep(0.033)
            END.undraw()
            time.sleep(1)
            gamewin.close()
            MES.close()
            BATTLEISGO = 0
            time.sleep(1)
        if HP >= HPtotal:
            HP = HPtotal
            HPvalue.setText(HP)
        time.sleep(0.0166)
    BattleBG.undraw()
    BattleBox.undraw()
    BattleBox2.undraw()
    Enemy.undraw()
    ATKtext.undraw()
    MGCtext.undraw()
    DEFtext.undraw()
    SelectionBox.undraw()
    HPvalue.undraw()
    HPtext.undraw()
    MPvalue.undraw()
    MPtext.undraw()
        
def LevelUp():
    global HPtotal
    global HP
    global MPtotal
    global MP
    global ATK
    global DEF
    global MATK
    global MDEF
    global SPD
    global EXP
    global LVL
    global EXPnext
    NEXP = EXP - EXPnext
    EXPnext = EXPnext + (EXPnext//4)
    EXP = 0 + NEXP
    NEXP = 0
    HPtotal = HPtotal + random.randrange(1,3,1)
    HP = HPtotal
    MPtotal = MPtotal + random.randrange(0,2,1)
    ATK = ATK + random.randrange(1,3,1)
    DEF = DEF + random.randrange(0,2,1)
    MATK = MATK + random.randrange(0,2,1)
    MDEF = MDEF + random.randrange(0,2,1)
    SPD = SPD + random.randrange(0,2,1)
    
def LightHouse(): #Draw map, copy movement over with new map coords AND mon IDs
    global EnterDungeon
    global playsceneB1
    global colwell
    global MONID
    EnterDungeon = 0
    F1 = Image(Point(401,140),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\LightHouse F1.gif')
    NotEnoughBlackFix = Rectangle(Point(0,0),Point(800,100))
    NotEnoughBlackFix.setFill('#000000')
    NotEnoughBlackFix.draw(gamewin)
    F1.draw(gamewin)
    colwell.undraw()
    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
    colwell.draw(gamewin)
    RNGcheck = 0
    RNG = random.randrange(6,13,1)
    INDUNGEON = 1
    DMAPX = 0
    DMAPY = 0
    F = 1
    while INDUNGEON == 1:
        ControllerMapping()
        keypress = MES.checkKey()
        try:
            if keypress == NEWdpadUP:
                if DMAPX == 0 and DMAPY == -288:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == -32 and DMAPY == -256 and F == 1:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == -64 and DMAPY == -224:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == -96 and DMAPY == -192:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == -128 and DMAPY == -160:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == 64 and DMAPY == -256:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == 96 and DMAPY == -224:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == 128 and DMAPY == -192:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == 160 and DMAPY == -160:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif F == 1 and DMAPY == -96 and DMAPX >= -32 and DMAPX <= 64:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif F == 2 and DMAPX == 32 and DMAPY == -288 or F == 2 and DMAPX == 96 and DMAPY == -96 or F == 2 and DMAPX == 64 and DMAPY == -64 or F == 2 and DMAPX == 32 and DMAPY == -32 or F == 2 and DMAPX == 0 and DMAPY == -32 or F == 2 and DMAPX == -32 and DMAPY == -64 or F == 2 and DMAPX == -64 and DMAPY == -96:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif F == 2 and DMAPX == 32 and DMAPY == -288:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif F == 3 and DMAPX == 32 and DMAPY == -288:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == 32 and DMAPY == -288 and F == 1:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    F2 = Image(Point(369
                                     ,460),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\LightHouse F2.gif')
                    F2.draw(gamewin)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    DMAPY = DMAPY + 32
                    RNGcheck = RNGcheck + 1
                    F = 2
                elif DMAPX == 32 and DMAPY == -256 and F == 2:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    F2.undraw()
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    DMAPY = DMAPY - 32
                    RNGcheck = RNGcheck + 1
                    F = 1
                elif F == 2 and DMAPX == -32 and DMAPY == -256:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    F3 = Image(Point(433
                                     ,460),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\LightHouse F3.gif')
                    F3.draw(gamewin)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    DMAPY = DMAPY + 32
                    RNGcheck = RNGcheck + 1
                    F = 3
                    if playsceneB1 == 1:
                        Keeper = Image(Point(496,393),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\LightHouseKeeperMAP.gif')
                        Keeper.draw(gamewin)
                    else:
                        pass
                elif F == 3 and DMAPX == -32 and DMAPY == -224:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    F3.undraw()
                    try:
                        Keeper.undraw()
                    except:
                        pass
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    DMAPY = DMAPY - 32
                    RNGcheck = RNGcheck + 1
                    F = 2
                else:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,8)
                    try:
                        F2.move(0,8)
                        F3.move(0,8)
                        Keeper.move(0,8)
                    except:
                        pass
                    DMAPY = DMAPY - 32
                    RNGcheck = RNGcheck + 1
            if keypress == NEWdpadDOWN:
                if F == 1 and DMAPX == 0 and DMAPY == -32 or F == 1 and DMAPX == 32 and DMAPY == -32:
                    INDUNGEON = 0
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                elif F == 1 and DMAPY == 0 and DMAPX == 0 or DMAPX == 32 and DMAPY == 32:
                    INDUNGEON = 0
                elif DMAPX == -32 and DMAPY == -32 or DMAPX == -64 and DMAPY == -64 or DMAPX == -96 and DMAPY == -96 or DMAPX == -128 and DMAPY == -128 or DMAPX == 64 and DMAPY == -32 or DMAPX == 96 and DMAPY == -64 or DMAPX == 128 and DMAPY == -96 or DMAPX == 160 and DMAPY == -128:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                elif F == 1 and DMAPY == -192 and DMAPX >= -32 and DMAPX <= 64:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                elif F == 2 and DMAPX == 32 and DMAPY == -256 or F == 2 and DMAPX == 64 and DMAPY == -224 or F == 2 and DMAPX == 96 and DMAPY == -192 or F == 2 and DMAPX == 32 and DMAPY == -32 or F == 2 and DMAPX == 0 and DMAPY == -32 or F == 2 and DMAPX == -64 and DMAPY == -192 or F == 2 and DMAPX == -32 and DMAPY == -224 :
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                else:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown3.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                    colwell.draw(gamewin)
                    F1.move(0,-8)
                    try:
                        F2.move(0,-8)
                        F3.move(0,-8)
                        Keeper.move(0,-8)
                    except:
                        pass
                    DMAPY = DMAPY + 32
                    RNGcheck = RNGcheck + 1
            if keypress == NEWdpadLEFT:
                if F == 1 and DMAPX == 96 and DMAPY >= -160 and DMAPY <= -128:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == -128 and DMAPY == -160 or DMAPX == -128 and DMAPY == -128 or DMAPX == -96 and DMAPY == -96 or DMAPX == -64 and DMAPY == -64 or DMAPX == -32 and DMAPY == -32 or DMAPX == 0 and DMAPY == -288 or DMAPX == -32 and DMAPY == -256 or DMAPX == -64 and DMAPY == -224 or DMAPX == -96 and DMAPY == -192 or DMAPX == 0 and DMAPY == 0:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft2.gif')
                    colwell.draw(gamewin)
                elif F == 2 and DMAPX == 32 and DMAPY == -288 or F == 2 and  DMAPX == 32 and DMAPY == -256 or F == 2 and  DMAPX == 64 and DMAPY == -224 or F == 2 and  DMAPX == 96 and DMAPY == -192 or DMAPX == 128 and DMAPY == -160 or F == 2 and  DMAPX == 128 and DMAPY == -128 or F == 2 and DMAPX == 96 and DMAPY == -96 or F == 2 and  DMAPX == 64 and DMAPY == -64 or F == 2 and  DMAPX == -96 and DMAPY == -128 or  F == 2 and DMAPX == -96 and DMAPY == -160:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft2.gif')
                    colwell.draw(gamewin)
                elif F == 3 and DMAPX == 0 and DMAPY == -256:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft2.gif')
                    colwell.draw(gamewin)
                else:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft2.gif')
                    colwell.draw(gamewin)
                    F1.move(8,0)
                    try:
                        F2.move(8,0)
                        F3.move(8,0)
                        Keeper.move(8,0)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                    colwell.draw(gamewin)
                    F1.move(8,0)
                    try:
                        F2.move(8,0)
                        F3.move(8,0)
                        Keeper.move(8,0)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft3.gif')
                    colwell.draw(gamewin)
                    F1.move(8,0)
                    try:
                        F2.move(8,0)
                        F3.move(8,0)
                        Keeper.move(8,0)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                    colwell.draw(gamewin)
                    F1.move(8,0)
                    try:
                        F2.move(8,0)
                        F3.move(8,0)
                        Keeper.move(8,0)
                    except:
                        pass
                    DMAPX = DMAPX - 32
                    RNGcheck = RNGcheck + 1
            if keypress == NEWdpadRIGHT:
                if F == 1 and DMAPX == -64 and DMAPY >= -160 and DMAPY <= -128:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight2.gif')
                    colwell.draw(gamewin)
                elif DMAPX == 32 and DMAPY == -288 or DMAPX == 64 and DMAPY == -256 or DMAPX == 96 and DMAPY == -224 or DMAPX == 128 and DMAPY == -192 or DMAPX == 160 and DMAPY == -160 or DMAPX == 160 and DMAPY == -128 or DMAPX == 128 and DMAPY == -96 or DMAPX == 96 and DMAPY == -64 or DMAPX == 64 and DMAPY == -32 or DMAPX == 32 and DMAPY == 0:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight2.gif')
                    colwell.draw(gamewin)
                elif F == 2 and DMAPX == -32 and DMAPY == -256 or F == 2 and DMAPX == -32 and DMAPY == -244 or F == 2 and DMAPX == -64 and DMAPY == -192 or F == 2 and DMAPX == -96 and DMAPY == -160 or F == 2 and DMAPX == -96 and DMAPY == -128 or F == 2 and DMAPX == -64 and DMAPY == -96 or F == 2 and DMAPX == -32 and DMAPY == -64 or F == 2 and DMAPX == 128 and DMAPY == -128 or F == 2 and DMAPX == 128 and DMAPY == -160 or F == 2 and DMAPX == -32 and DMAPY == -224:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight2.gif')
                    colwell.draw(gamewin) 
                else:
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight2.gif')
                    colwell.draw(gamewin)
                    F1.move(-8,0)
                    try:
                        F2.move(-8,0)
                        F3.move(-8,0)
                        Keeper.move(-8,0)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                    colwell.draw(gamewin)
                    F1.move(-8,0)
                    try:
                        F2.move(-8,0)
                        F3.move(-8,0)
                        Keeper.move(-8,0)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight3.gif')
                    colwell.draw(gamewin)
                    F1.move(-8,0)
                    try:
                        F2.move(-8,0)
                        F3.move(-8,0)
                        Keeper.move(-8,0)
                    except:
                        pass
                    time.sleep(0.033)
                    colwell.undraw()
                    colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                    colwell.draw(gamewin)
                    F1.move(-8,0)
                    try:
                        F2.move(-8,0)
                        F3.move(-8,0)
                        Keeper.move(-8,0)
                    except:
                        pass
                    DMAPX = DMAPX + 32
                    RNGcheck = RNGcheck + 1
            if keypress == NEWA_BUTTON:
                print(DMAPX,DMAPY)
            if RNGcheck > RNG:
                RNGcheck = 0
                RNG = random.randrange(6,13,1)
                MONIDchance = random.randrange(1,4,1)
                print('-')
                if MONIDchance >= 2:
                    MONID = 1
                    print('1')
                elif MONIDchance == 1:
                    MONID = 2
                    print('2')
                else:
                    MONID = 0
                    print('ERROR: Monster ID not found')
                Battle()
                MONID = 0
            if F == 3 and DMAPX == 32 and DMAPY == -160 and playsceneB1 == 1:
                MONID = 11
                Battle()
                Keeper.undraw()
                playsceneB1 = 0
            else:
                pass
        except:
            pass
    F1.undraw()
    NotEnoughBlackFix.undraw()
    
def ForestMaze():
    pass
def PirateShip():
    pass
def Underground():
    pass

def UnlockFlood():
    global MGCflood
    global NEWA_BUTTON
    global playsceneF
    Textbox = Rectangle(Point(0,445),Point(800,608))
    Textbox.setFill('#000000')
    Textbox.draw(gamewin)
    Border = Rectangle(Point(0,443),Point(800,447))
    Border.setFill('#ffffff')
    Border.setOutline('#ffffff')
    Border.draw(gamewin)
    Text2 = Text(Point(400,495),'Discovered Flood spell!')
    Text1 = Text(Point(400,465),'A tattered spell book lies upon the rocks')
    Text1.setSize(16)
    Text1.setTextColor('#ffffff')
    Text1.draw(gamewin)
    time.sleep(1)
    Text2.setSize(16)
    Text2.setTextColor('#ffffff')
    Text2.draw(gamewin)
    while playsceneF == 1:
        keypress = MES.checkKey()
        try:
            if keypress == NEWA_BUTTON:
                Next = 1
                Textbox.undraw()
                Border.undraw()
                Text1.undraw()
                Text2.undraw()
                MGCflood = 1
                playsceneF = 0
        except:
            pass

def UnlockLifedrain():
    global MGClifedrain
    global NEWA_BUTTON
    global playsceneL
    Textbox = Rectangle(Point(0,445),Point(800,608))
    Textbox.setFill('#000000')
    Textbox.draw(gamewin)
    Border = Rectangle(Point(0,443),Point(800,447))
    Border.setFill('#ffffff')
    Border.setOutline('#ffffff')
    Border.draw(gamewin)
    Text2 = Text(Point(400,495),'Discovered Life Drain spell!')
    Text1 = Text(Point(400,465),'A mossy spell book lies upon the forest floor')
    Text1.setSize(16)
    Text1.setTextColor('#ffffff')
    Text1.draw(gamewin)
    time.sleep(1)
    Text2.setSize(16)
    Text2.setTextColor('#ffffff')
    Text2.draw(gamewin)
    while playsceneL == 1:
        keypress = MES.checkKey()
        try:
            if keypress == NEWA_BUTTON:
                Next = 1
                Textbox.undraw()
                Border.undraw()
                Text1.undraw()
                Text2.undraw()
                MGClifedrain = 1
                playsceneL = 0
        except:
            pass

def UnlockTremor():
    global MGCtremor
    global NEWA_BUTTON
    global playsceneT
    Textbox = Rectangle(Point(0,445),Point(800,608))
    Textbox.setFill('#000000')
    Textbox.draw(gamewin)
    Border = Rectangle(Point(0,443),Point(800,447))
    Border.setFill('#ffffff')
    Border.setOutline('#ffffff')
    Border.draw(gamewin)
    Text2 = Text(Point(400,495),'Discovered Tremor spell!')
    Text1 = Text(Point(400,465),'A dusty spell book lies in the rubble')
    Text1.setSize(16)
    Text1.setTextColor('#ffffff')
    Text1.draw(gamewin)
    time.sleep(1)
    Text2.setSize(16)
    Text2.setTextColor('#ffffff')
    Text2.draw(gamewin)
    while playsceneT == 1:
        keypress = MES.checkKey()
        try:
            if keypress == NEWA_BUTTON:
                Next = 1
                Textbox.undraw()
                Border.undraw()
                Text1.undraw()
                Text2.undraw()
                MGCtremor = 1
                playsceneT = 0
        except:
            pass

def VisitWumee():
    global NEWA_BUTTON
    global playsceneCity1
    Textbox = Rectangle(Point(0,445),Point(800,608))
    Textbox.setFill('#000000')
    Textbox.draw(gamewin)
    Border = Rectangle(Point(0,443),Point(800,447))
    Border.setFill('#ffffff')
    Border.setOutline('#ffffff')
    Border.draw(gamewin)
    Text2 = Text(Point(400,495),'Defeat him and his three minions to free our land!')
    Text1 = Text(Point(400,465),'The evil Nathan has cursed the land of Pythonia!')
    DemoText = Text(Point(400,525),'In this demo only the Lighthouse dungeon is available.')
    DemoText.setSize(16)
    DemoText.setTextColor('#ffffff')
    Text1.setSize(16)
    Text1.setTextColor('#ffffff')
    Text1.draw(gamewin)
    time.sleep(1)
    Text2.setSize(16)
    Text2.setTextColor('#ffffff')
    Text2.draw(gamewin)
    DemoText.draw(gamewin)
    while playsceneCity1 == 1:
        keypress = MES.checkKey()
        try:
            if keypress == NEWA_BUTTON:
                Next = 1
                Textbox.undraw()
                Border.undraw()
                Text1.undraw()
                Text2.undraw()
                DemoText.undraw()
                HP = HPtotal
                MP = MPtotal
                playsceneCity1 = 0
        except:
            pass
def VisitErubin():
    global NEWA_BUTTON
    global playsceneCity4
    Textbox = Rectangle(Point(0,445),Point(800,608))
    Textbox.setFill('#000000')
    Textbox.draw(gamewin)
    Border = Rectangle(Point(0,443),Point(800,447))
    Border.setFill('#ffffff')
    Border.setOutline('#ffffff')
    Border.draw(gamewin)
    Text2 = Text(Point(400,495),'The entrance is sealed by the powers of his minions!')
    Text1 = Text(Point(400,465),"Nathan's base is in the heart of the mine")
    Text1.setSize(16)
    Text1.setTextColor('#ffffff')
    Text1.draw(gamewin)
    time.sleep(1)
    Text2.setSize(16)
    Text2.setTextColor('#ffffff')
    Text2.draw(gamewin)
    while playsceneCity4 == 1:
        keypress = MES.checkKey()
        try:
            if keypress == NEWA_BUTTON:
                Next = 1
                Textbox.undraw()
                Border.undraw()
                Text1.undraw()
                Text2.undraw()
                HP = HPtotal
                MP = MPtotal
                playsceneCity4 = 0
        except:
            pass
def VisitPyrigg():
    global NEWA_BUTTON
    global playsceneCity2
    Textbox = Rectangle(Point(0,445),Point(800,608))
    Textbox.setFill('#000000')
    Textbox.draw(gamewin)
    Border = Rectangle(Point(0,443),Point(800,447))
    Border.setFill('#ffffff')
    Border.setOutline('#ffffff')
    Border.draw(gamewin)
    Text2 = Text(Point(400,495),'He resides at the end of the forest maze!')
    Text1 = Text(Point(400,465),'A dark force controls the forest')
    Text1.setSize(16)
    Text1.setTextColor('#ffffff')
    Text1.draw(gamewin)
    time.sleep(1)
    Text2.setSize(16)
    Text2.setTextColor('#ffffff')
    Text2.draw(gamewin)
    while playsceneCity2 == 1:
        keypress = MES.checkKey()
        try:
            if keypress == NEWA_BUTTON:
                Next = 1
                Textbox.undraw()
                Border.undraw()
                Text1.undraw()
                Text2.undraw()
                HP = HPtotal
                MP = MPtotal
                playsceneCity2 = 0
        except:
            pass
def VisitFogiv():
    global NEWA_BUTTON
    global playsceneCity3
    Textbox = Rectangle(Point(0,445),Point(800,608))
    Textbox.setFill('#000000')
    Textbox.draw(gamewin)
    Border = Rectangle(Point(0,443),Point(800,447))
    Border.setFill('#ffffff')
    Border.setOutline('#ffffff')
    Border.draw(gamewin)
    Text2 = Text(Point(400,495),'Be wary of loose platflorms floating in the water')
    Text1 = Text(Point(400,465),'The pirate ship is haunted by an old sea captain!')
    Text1.setSize(16)
    Text1.setTextColor('#ffffff')
    Text1.draw(gamewin)
    time.sleep(1)
    Text2.setSize(16)
    Text2.setTextColor('#ffffff')
    Text2.draw(gamewin)
    while playsceneCity3 == 1:
        keypress = MES.checkKey()
        try:
            if keypress == NEWA_BUTTON:
                Next = 1
                Textbox.undraw()
                Border.undraw()
                Text1.undraw()
                Text2.undraw()
                HP = HPtotal
                MP = MPtotal
                playsceneCity3 = 0
        except:
            pass
#Magic attack variables - - - - - - - - - - - - -
MGCfire = 1
MGCtremor = 1
MGCflood = 1
MGClifedrain = 1
# - - - - - - - - - - - - - - - - - - - - - - - -

#Cutscene flags - - - - - - - - - - - - - - - - -
EnterDungeon = 1
playsceneE = 1
playsceneT = 1
playsceneF = 1
playsceneL = 1
playsceneB1 = 1
playsceneB2 = 1
playsceneB3 = 1
playsceneB4 = 1
playsceneCity1 = 1
playsceneCity2 = 1
playsceneCity3 = 1
playsceneCity4 = 1
# - - - - - - - - - - - - - - - - - - - - - - - -
                          
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#           END OF DEFINITIONS                      END OF DEFINITIONS
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



    
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   WELCOME TO THE WONDERFUL WORLD OF GAME CODE, SCREW THE FUNCTIONS ABOVE
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
GAMEISGO = 1
RNGbattle = 0
RNGcheck = 0
HP = HPtotal
MP = MPtotal
MAPX = 0    
MAPY = 0

while GAMEISGO == 1:
    ControllerMapping()
    keypress = MES.checkKey()
    #if RNGbattle < 1:          #Move to dungeons later
        #RNGbattle = random.randrange(15,60,1)
    #if RNGcheck >= RNGbattle:
        #Battle()
        #RNGcheck = 0
    try:
        if keypress == NEWdpadLEFT:
            if MAPX == -1824:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
            elif MAPX == -192 and MAPY <=832 and MAPY >= 480:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
            elif MAPY == -64 and MAPX == -608:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
            elif MAPX == -576 and MAPY == -64:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
            elif MAPX == -1216 and MAPY <= 32 and MAPY >= -64:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
            elif MAPX == -160 and MAPY <= 448:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
            elif MAPX == -64 and MAPY >= 864 and MAPY <= 896:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
            else:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft2.gif')
                colwell.draw(gamewin)
                overworld.move(8,0)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
                overworld.move(8,0)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft3.gif')
                colwell.draw(gamewin)
                overworld.move(8,0)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
                overworld.move(8,0)
                MAPX = MAPX - 32
                playsceneCity1 = 1
                playsceneCity2 = 1
                playsceneCity3 = 1
                playsceneCity4 = 1
        if keypress == NEWdpadRIGHT:
            if MAPX == 64:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
            elif MAPX == -608 and MAPY <= 32 and MAPY >= -64:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
            elif MAPX == -1248 and MAPY == -64:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
            elif MAPX == -64 and MAPY >= 864 and MAPY <= 896:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
            elif MAPX == -256 and MAPY == 896:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
            elif MAPX == -288 and MAPY >= -64 and MAPY <= 384:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
            elif MAPX == -320 and MAPY >= 416 and MAPY <= 864:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
            else:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight2.gif')
                colwell.draw(gamewin)
                overworld.move(-8,0)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
                overworld.move(-8,0)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight3.gif')
                colwell.draw(gamewin)
                overworld.move(-8,0)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColRight1.gif')
                colwell.draw(gamewin)
                overworld.move(-8,0)
                MAPX = MAPX + 32
                playsceneCity1 = 1
                playsceneCity2 = 1
                playsceneCity3 = 1
                playsceneCity4 = 1
        if keypress == NEWdpadUP:
            if MAPY == -64:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
            elif MAPY == 480 and MAPX == -192:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
            elif MAPY == -32 and MAPX >= -1216 and MAPX <= -640:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
            elif MAPY == 928 and MAPX >= -32 and MAPX <= 64:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
            elif MAPY == 928 and MAPX >= -224 and MAPX <= -96:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
            elif MAPY == 896 and MAPX >= -288 and MAPX <= - 256:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
            else:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp2.gif')
                colwell.draw(gamewin)
                overworld.move(0,8)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
                overworld.move(0,8)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp3.gif')
                colwell.draw(gamewin)
                overworld.move(0,8)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColUp1.gif')
                colwell.draw(gamewin)
                overworld.move(0,8)
                MAPY = MAPY - 32
                playsceneCity1 = 1
                playsceneCity2 = 1
                playsceneCity3 = 1
                playsceneCity4 = 1
        if keypress == NEWdpadDOWN:
            if MAPY == 1472:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                colwell.draw(gamewin)
            elif MAPX >= -32 and MAPY == 832:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                colwell.draw(gamewin)
            elif MAPX <= - 96 and MAPX >= -192 and MAPY == 832:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                colwell.draw(gamewin)
            elif MAPX == -288 and MAPY == 384:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                colwell.draw(gamewin)
            else:
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown2.gif')
                colwell.draw(gamewin)
                overworld.move(0,-8)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                colwell.draw(gamewin)
                overworld.move(0,-8)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown3.gif')
                colwell.draw(gamewin)
                overworld.move(0,-8)
                time.sleep(0.033)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColDown1.gif')
                colwell.draw(gamewin)
                overworld.move(0,-8)
                MAPY = MAPY + 32
                playsceneCity1 = 1
                playsceneCity2 = 1
                playsceneCity3 = 1
                playsceneCity4 = 1
        if keypress == NEWSTART:
            Save()
        if keypress == NEWSELECT:
            Paused = 1
            PAUSED = Text(Point(400,304),'PAUSED')
            PAUSED.setSize(36)
            PAUSED.draw(gamewin)
            while Paused == 1:
                keypress = MES.checkKey()
                try:
                    if keypress == NEWSELECT:
                        Paused = 0
                except:
                    pass
            PAUSED.undraw()
        if keypress == NEWA_BUTTON:
            print(MAPX, MAPY)
        if keypress == NEWB_BUTTON:
            print(HPtotal,HP,MPtotal,MP,ATK,DEF,MATK,MDEF,SPD,EXP,EXPnext)
            MONID = 21
            Battle()
        if MAPY == -64 and MAPX == -608:
            if playsceneF == 1:
                UnlockFlood()
                playsceneF = 0
            else:
                pass
        if MAPX == -1728 and MAPY == 1280:
            if playsceneL == 1:
                UnlockLifedrain()
                playsceneL = 0
            else:
                pass
        if MAPX == -864 and MAPY ==1216:
            if playsceneT == 1:
                UnlockTremor()
                playsceneT = 0
            else:
                pass
        if MAPX == 0 and MAPY == 0:
            if playsceneCity1 == 1:
                VisitWumee()
                playsceneCity1 = 0
            else:
                pass
        if MAPX == -384 and MAPY == 704:
            if playsceneCity4 == 1:
                VisitErubin()
                playsceneCity4 = 0
            else:
                pass
        if MAPX == -1408 and MAPY == 512:
            if playsceneCity2 == 1:
                VisitPyrigg()
                playsceneCity2 = 0
            else:
                pass
        if MAPX == -1280 and MAPY == 0:
            if playsceneCity3 == 1:
                VisitFogiv()
                playsceneCity3 = 0
            else:
                pass
        if MAPX == 64 and MAPY == 1472:
            if EnterDungeon == 1:
                LightHouse()
                overworld.move(32,0)
                colwell.undraw()
                colwell = Image(Point(384,284),r'C:\Users\Mitchell\Desktop\Coding and Programming\Games\Colwell Quest\ColLeft1.gif')
                colwell.draw(gamewin)
                MAPX = MAPX - 32
                EnterDungeon = 1
            else:
                pass
    except:
        pass
    time.sleep(0.0166)
            
