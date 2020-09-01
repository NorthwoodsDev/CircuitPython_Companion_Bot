import time
import random
import displayio
import terminalio
import adafruit_imageload
from adafruit_display_text.label import Label

def fight(minitft, companbot_x):

    uiGroup = displayio.Group(max_size=6)

    bg_bitmap = displayio.Bitmap(160, 80, 4)
    move_bitmap = displayio.Bitmap(2, 80, 4)
    bg_color_palette = displayio.Palette(4)
    bg_color_palette[0] = 0x000000
    bg_color_palette[1] = 0xff0000
    bg_color_palette[2] = 0x00ff00
    bg_color_palette[3] = 0x0000ff
    bgDisp = displayio.TileGrid(bg_bitmap, pixel_shader=bg_color_palette, x=0, y=0)
    moveDisp = displayio.TileGrid(move_bitmap, pixel_shader=bg_color_palette, x=0, y=0)

    text_area = Label(terminalio.FONT, text='A: Attack', max_glyphs=12)
    text_area.x = 5
    text_area.y = 60
    #text_area.scale = 2

    text_area2 = Label(terminalio.FONT, text='B: Run', max_glyphs=12)
    text_area2.x = 90
    text_area2.y = 60

    text_area3 = Label(terminalio.FONT, text='HP', max_glyphs=12)
    text_area3.x = 5
    text_area3.y = 30

    text_area4 = Label(terminalio.FONT, text='Enemy', max_glyphs=12)
    text_area4.x = 90
    text_area4.y = 30

    uiGroup.append(bgDisp)
    uiGroup.append(moveDisp)
    uiGroup.append(text_area)
    uiGroup.append(text_area2)
    uiGroup.append(text_area3)
    uiGroup.append(text_area4)

    fightJudge = True
    enemyHP = int((int(companbot_x.hp) / random.randint(1,4)) + random.randint(0,5))
    enemyAtk = (int(companbot_x.pAtk) / random.randint(1,2)) + random.randint(0,5)
    enemyDef = (int(companbot_x.pDef) / random.randint(1,2)) + random.randint(0,5)
    print("Enemy HP:" + str(enemyHP) + " Atk:" + str(enemyAtk) + " Def:" + str(enemyDef))

    #Input eater
    time.sleep(0.4)
    print("Fight")
    while fightJudge:
        moveDisp.hidden = False
        bg_bitmap.fill(0)
        move_bitmap.fill(random.randint(1,3))
        moveDisp.x = random.randint(70,85)
        buttons = minitft.buttons
        minitft.display.show(uiGroup)
        text_area.text = "A:Attack"
        text_area2.text = "B:Run"
        text_area3.text = "HP:" + str(companbot_x.hp)
        text_area4.text = "Enemy:" + str(enemyHP)
        if buttons.a:
            print("Pressed A")
            bg_bitmap.fill(1)
            moveDisp.hidden = True
            text_area.text = "Attacking!"
            text_area2.text = " "
            enemyHP = int(enemyHP) - int(companbot_x.pAtk)
            if enemyHP >= 1:
                icd = int(enemyAtk) - int(companbot_x.pDef)
                print("Incoming Damage:" + str(icd))
                if icd >= 0:
                    companbot_x.hp = int(companbot_x.hp) - icd
            time.sleep(1)
        if buttons.b:
            print("Pressed B")
            bg_bitmap.fill(3)
            moveDisp.hidden = True
            text_area.text = "Running!"
            text_area2.text = " "
            time.sleep(1)
            run_roll = random.randint(0,1)
            if(int(companbot_x.pDef) >= int(enemyAtk) or run_roll == 1):
                bg_bitmap.fill(2)
                text_area.text = "Got away!"
                time.sleep(1)
                fightJudge = False
            else:
                bg_bitmap.fill(1)
                text_area.text = "Failed!"
                time.sleep(1)
                icd = int(companbot_x.pDef) - (int(enemyAtk) * 1.5)
                if icd >= 0:
                    companbot_x.hp = int(companbot_x.hp) - icd
            time.sleep(1)
        if int(enemyHP) <= 0:
            fightJudge = False
            bg_bitmap.fill(2)
            text_area.text = " "
            text_area2.text = " "
            text_area3.x = 50
            text_area3.text = "You"
            text_area4.text = "Win"
            time.sleep(2)
            companbot_x.xp = companbot_x.xp + random.randint(10,40)
            companbot_x.hunger = companbot_x.hunger - 10
            break
        if int(companbot_x.hp) <= 0:
            fightJudge = False
            bg_bitmap.fill(1)
            text_area.text = " "
            text_area2.text = " "
            text_area3.x = 50
            text_area3.text = "You"
            text_area4.text = "Lose"
            time.sleep(2)
            companbot_x.hp = 10
            break
    return companbot_x
