import time
import displayio, terminalio, adafruit_imageload
from adafruit_display_text import label
from random import choice as rc

def total(hand):
    if len(hand) >= 3 and 11 in hand:
        t = sum(hand) - 10
    else:
        t = sum(hand)
    return t

def cardmap(value):
    thisdict = {
    2: 0,
    3: 1,
    4: 2,
    5: 3,
    6: 4,
    7: 5,
    8: 6,
    9: 7,
    10: 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    11: 12
    }
    cardIndex = thisdict[value]
    return cardIndex

def playHand(minitft, companbot_x):
    #----------------------------------
    bj_screen = displayio.Group(max_size=8)
    cardslot1 = displayio.Group(max_size=2)
    cardslot2 = displayio.Group(max_size=1)
    cardslot3 = displayio.Group(max_size=1)
    cardslot4 = displayio.Group(max_size=1)
    cardslot5 = displayio.Group(max_size=1)
    text_group_bj = displayio.Group(max_size=3)
    card2BMP = "/bmp/cards.bmp"

    color_bitmap = displayio.Bitmap(160, 80, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0x20c040

    bjbgDisp = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

    text_area1_bj = label.Label(terminalio.FONT, text="Dealing", color=0xFFFFFF, max_glyphs=20, x=5, y=55)
    text_area2_bj = label.Label(terminalio.FONT, text="Cards", color=0xFFFFFF, max_glyphs=20, x=80, y=55)
    text_area3_bj = label.Label(terminalio.FONT, text=" ", color=0xFFFFFF, max_glyphs=20, x=50, y=70)

    card2_SP, card2_Pal = adafruit_imageload.load(card2BMP,bitmap=displayio.Bitmap,palette=displayio.Palette)
    cardSlot1_Disp = displayio.TileGrid(card2_SP, pixel_shader=card2_Pal, width = 1, height = 1, tile_width = 25, tile_height = 30, x=5, y=2)
    cardSlot2_Disp = displayio.TileGrid(card2_SP, pixel_shader=card2_Pal, width = 1, height = 1, tile_width = 25, tile_height = 30, x=35, y=2)
    cardSlot3_Disp = displayio.TileGrid(card2_SP, pixel_shader=card2_Pal, width = 1, height = 1, tile_width = 25, tile_height = 30, x=65, y=2)
    cardSlot4_Disp = displayio.TileGrid(card2_SP, pixel_shader=card2_Pal, width = 1, height = 1, tile_width = 25, tile_height = 30, x=95, y=2)
    cardSlot5_Disp = displayio.TileGrid(card2_SP, pixel_shader=card2_Pal, width = 1, height = 1, tile_width = 25, tile_height = 30, x=125, y=2)
    cardslot1.append(cardSlot1_Disp)
    cardslot2.append(cardSlot2_Disp)
    cardslot3.append(cardSlot3_Disp)
    cardslot4.append(cardSlot4_Disp)
    cardslot5.append(cardSlot5_Disp)

    text_group_bj.append(text_area1_bj)
    text_group_bj.append(text_area2_bj)
    text_group_bj.append(text_area3_bj)

    #text_area2_bj.x = 80
    #text_area2_bj.y = 55
    #text_area3_bj.x = 50
    #text_area3_bj.y = 70

    bj_screen.append(bjbgDisp)
    bj_screen.append(cardslot1)
    bj_screen.append(cardslot2)
    bj_screen.append(cardslot3)
    bj_screen.append(cardslot4)
    bj_screen.append(cardslot5)
    bj_screen.append(text_group_bj)
    #----------------------------------
    minitft.display.show(bj_screen)
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    player = []
    # draw 2 cards for the player to start
    player.append(rc(cards))
    player.append(rc(cards))
    pbust = False  # player busted flag
    cbust = False  # computer busted flag
    playerTurn = True
    #text_area1_bj.text = " "
    #text_area2_bj.text = " "
    cardslot1.hidden = True
    cardslot2.hidden = True
    cardslot3.hidden = True
    cardslot4.hidden = True
    cardslot5.hidden = True

    cardSlot1_Disp[0] = cardmap(int(player[0]))
    cardslot1.hidden = False
    time.sleep(1)
    cardSlot2_Disp[0] = cardmap(int(player[1]))
    cardslot2.hidden = False
    time.sleep(1)

    #Input eater
    #time.sleep(0.4)

    while playerTurn:
        playerInput = False
        tp = total(player)
        text_area1_bj.text = " "
        text_area2_bj.text = " "
        text_area3_bj.text = "Total: {}".format(tp)
        time.sleep(2)
        if tp > 21:
            text_area1_bj.text = "Player bust!"
            time.sleep(2)
            pbust = True
            playerTurn = False
        elif tp == 21:
            text_area1_bj.text = "BLACKJACK!!!"
            time.sleep(2)
            playerTurn = False
        else:
            text_area1_bj.text = "Hit (A)"
            text_area2_bj.text = "Stand (B)"
            while not playerInput:
                buttons = minitft.buttons
                if buttons.a:
                    print("Awaiting User")
                    playerInput = True
                    text_area1_bj.text = "Hit"
                    text_area2_bj.text = ""
                    player.append(rc(cards))
                    if len(player) == 3:
                        cardslot3.hidden = False
                        cardSlot3_Disp[0] = cardmap(int(player[2]))
                        time.sleep(1)
                    elif len(player) == 4:
                        cardslot4.hidden = False
                        cardSlot4_Disp[0] = cardmap(int(player[3]))
                        time.sleep(1)
                    elif len(player) == 5:
                        cardslot5.hidden = False
                        cardSlot5_Disp[0] = cardmap(int(player[4]))
                        time.sleep(1)
                        playerTurn = False
                if buttons.b:
                    text_area1_bj.text = "Stand"
                    text_area2_bj.text = ""
                    time.sleep(1)
                    playerInput = True
                    playerTurn = False
    while True:
        # loop for the computer's play ...
        cardslot1.hidden = True
        cardslot2.hidden = True
        cardslot3.hidden = True
        cardslot4.hidden = True
        cardslot5.hidden = True
        text_area1_bj.text = "Dealer's Turn"
        text_area2_bj.text = " "
        text_area3_bj.text = " "
        comp = []
        time.sleep(1)
        comp.append(rc(cards))
        cardslot1.hidden = False
        cardSlot1_Disp[0] = cardmap(int(comp[0]))
        time.sleep(1)
        comp.append(rc(cards))
        cardslot2.hidden = False
        cardSlot2_Disp[0] = cardmap(int(comp[1]))
        time.sleep(1)
        while not pbust or cbust:
            tc = total(comp)
            text_area3_bj.text = "Total: {}".format(tc)
            if tc < 17:
                comp.append(rc(cards))
                if cardslot3.hidden:
                    cardslot3.hidden = False
                    cardSlot3_Disp[0] = cardmap(int(comp[2]))
                    time.sleep(2)
                elif cardslot4.hidden and not cardslot3.hidden:
                    cardslot4.hidden = False
                    cardSlot4_Disp[0] = cardmap(int(comp[3]))
                    time.sleep(2)
                elif cardslot5.hidden and not cardslot4.hidden:
                    cardslot5.hidden = False
                    cardSlot5_Disp[0] = cardmap(int(comp[4]))
                    time.sleep(2)
            else:
                break
        text_area3_bj.text = " "
        # now figure out who won ...
        if tc > 21:
            text_area1_bj.text = "Dealer bust!"
            cbust = True
            if pbust == False:
                text_area1_bj.text = "Player wins!"
                companbot_x.cred = companbot_x.cred + 20
        elif tc > tp:
            text_area1_bj.text = "Dealer Wins!"
        elif tc == tp:
            text_area1_bj.text = "It's a draw!"
        elif tp > tc:
            if pbust == False:
                text_area1_bj.text = "Player wins!"
                companbot_x.cred = companbot_x.cred + 10
            elif cbust == False:
                text_area1_bj.text = "Dealer Wins!"
        break
    time.sleep(2)
    return companbot_x