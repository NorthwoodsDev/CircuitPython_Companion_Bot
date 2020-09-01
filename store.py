import time
import displayio
import terminalio
from adafruit_display_text.label import Label

def clerk(minitft, companbot_x):
    try:

        storeScreen = displayio.Group(max_size=5)

        text_area = Label(terminalio.FONT, text='A: Attack Upgrade', max_glyphs=22)
        text_area.x = 5
        text_area.y = 12

        text_area_2 = Label(terminalio.FONT, text='B: Defend Upgrade', max_glyphs=22)
        text_area_2.x = 5
        text_area_2.y = 24

        text_area_3 = Label(terminalio.FONT, text='Select: Exit', max_glyphs=20)
        text_area_3.x = 5
        text_area_3.y = 36

        text_area_4 = Label(terminalio.FONT, text=' ', max_glyphs=32)
        text_area_4.x = 5
        text_area_4.y = 60

        storeScreen.append(text_area)
        storeScreen.append(text_area_2)
        storeScreen.append(text_area_3)
        storeScreen.append(text_area_4)

        storeChoice = True

        time.sleep(0.5)
        while storeChoice:
            buttons = minitft.buttons
            minitft.display.show(storeScreen)
            text_area.text = "A: Attack Upgrade"
            text_area_2.text = "B: Defend Upgrade"
            text_area_4.text = "Cred:" + str(companbot_x.cred) + " Atk:" + str(companbot_x.pAtk) + " Def:" + str(companbot_x.pDef)
            if buttons.a:
                print("Pressed A")
                if int(companbot_x.cred) >= 20:
                    companbot_x.pAtk = int(companbot_x.pAtk) + 2
                    companbot_x.cred = int(companbot_x.cred) - 20
                    text_area.text = "Thank you"
                else:
                    text_area.text = "Need more Credits"
                time.sleep(1.0)
            if buttons.b:
                print("Pressed B")
                if int(companbot_x.cred) >= 20:
                    companbot_x.pDef = int(companbot_x.pDef) + 2
                    companbot_x.cred = int(companbot_x.cred) - 20
                    text_area_2.text = "Thank you"
                else:
                    text_area_2.text = "Need more Credits"
                time.sleep(1.0)
            if buttons.select:
                print("Exiting Shop")
                storeChoiceChoice = False
                time.sleep(0.2)
                break
    except Exception as e:
        print("Error Store: " + str(e))

    return