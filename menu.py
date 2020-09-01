import time
import displayio
import terminalio
import blackjack
import combat
import store
from adafruit_display_text.label import Label

def menu(minitft, companbot_x):

    menuScreen = displayio.Group(max_size=10)

    text_area = Label(terminalio.FONT, text='(A)Fight', max_glyphs=20)
    text_area.x = 5
    text_area.y = 12

    text_area2 = Label(terminalio.FONT, text='(B)Blackjack', max_glyphs=20)
    text_area2.x = 60
    text_area2.y = 12

    text_area3 = Label(terminalio.FONT, text='(Select)Home', max_glyphs=20)
    text_area3.x = 5
    text_area3.y = 24

    text_area4 = Label(terminalio.FONT, text="Lvl:" + str(companbot_x.lvl) + " Xp:" + str(companbot_x.xp) + " Cred:" + str(companbot_x.cred), max_glyphs=32)
    text_area4.x = 5
    text_area4.y = 52

    text_area5 = Label(terminalio.FONT, text=' ', max_glyphs=32)
    text_area5.x = 5
    text_area5.y = 67
    text_area5.text = "Hp:" + str(companbot_x.hp) + " Atk:" + str(companbot_x.pAtk) + " Def:" + str(companbot_x.pDef)

    text_area6 = Label(terminalio.FONT, text='(Up)Store', max_glyphs=20)
    text_area6.x = 80
    text_area6.y = 24

    menuScreen.append(text_area)
    menuScreen.append(text_area2)
    menuScreen.append(text_area3)
    menuScreen.append(text_area4)
    menuScreen.append(text_area5)
    menuScreen.append(text_area6)
    menuChoice = True

    time.sleep(0.5)
    try:
        while menuChoice:
            buttons = minitft.buttons
            minitft.display.show(menuScreen)
            if buttons.a:
                print("Pressed A")
                menuChoice = False
                time.sleep(0.1)
                companbot_x = combat.fight(minitft, companbot_x)
            if buttons.b:
                print("Pressed B")
                menuChoice = False
                time.sleep(0.1)
                companbot_x = blackjack.playHand(minitft, companbot_x)
            if buttons.up:
                print("Pressed Up")
                menuChoice = False
                time.sleep(0.1)
                companbot_x = store.clerk(minitft, companbot_x)
            if buttons.select:
                print("Pressed Select")
                menuChoice = False
                time.sleep(0.2)
                break
    except Exception as e:
        print("Error Menu: " + str(e))
    return