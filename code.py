import board, time, random, neopixel, displayio, terminalio, adafruit_imageload
import helper, sandman, companion, menu
from adafruit_display_text import label
from adafruit_featherwing import minitft_featherwing

def getX(newX, nextMove):
    if newX < 1:
        newX = 1
        nextMove = 0
    if newX > 139:
        newX = 139
        nextMove = 1
    return newX, nextMove

def getY(newY, nextMove):
    if newY < 21:
        newY = 21
        nextMove = 0
    if newY > 42:
        newY = 42
        nextMove = 1
    return newY, nextMove

def walk(curPos, steps, nextMove):
    if steps <= 0:
        steps = random.randint(4, 12)
        nextMove = random.randint(0, 2)
    else:
        steps = steps - 1
    if nextMove == 0:
        curPos = curPos + 1
    elif nextMove == 1:
        curPos = curPos - 1
    else:
        curPos = curPos
    return curPos, steps, nextMove

def digest(companbot_x, food):
    if companbot_x.hunger < 10:
        text_area.text = "Feed Me!"
        error = [0,4,0,4,0,4]
        animate(error)
    if companbot_x.hunger <= 0:
        companbot_x.hunger = 0
    if food:
        text_area.text = "Yummy!"
        companbot_x.hunger = 100
        maxHP = 10 + (int(companbot_x.lvl) * 2)
        if companbot_x.hp < maxHP:
            companbot_x.hp = maxHP
        idle = [0,2,0,2,0,2]
        animate(idle)
    return companbot_x

def animate(routine):
    for r in routine:
        companbot_Sprite_Disp[0] = r
        time.sleep(0.4)
    return

led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.01

text_group = displayio.Group(max_size=10, scale=1, x=5, y=5)
text_area = label.Label(terminalio.FONT, text="Press a Button", color=0xFFFFFF, max_glyphs=60)
text_group.append(text_area)

bg_bitmap = displayio.Bitmap(160, 80, 4)
bg_color_palette = displayio.Palette(4)
bg_color_palette[0] = 0x00e000
bg_color_palette[1] = 0x00c000
bg_color_palette[2] = 0x80fe55
bg_color_palette[3] = 0x005f00

for y in range(0, 80, 8):
    for x in range(160):
        bg_bitmap[x, y + 2] = 1
        bg_bitmap[x, y + 3] = 1
        bg_bitmap[x, y + 6] = 1
        bg_bitmap[x, y + 7] = 1

color_bitmap = displayio.Bitmap(160, 20, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0x000000

bgDisp = displayio.TileGrid(bg_bitmap, pixel_shader=bg_color_palette, x=0, y=0)
textbg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)

companbot_Sprite = "/bmp/bot_16.bmp"
companbot_Sprite, companbot_Sprite_pal = adafruit_imageload.load(companbot_Sprite,bitmap=displayio.Bitmap,palette=displayio.Palette)
companbot_Sprite_Disp = displayio.TileGrid(companbot_Sprite, pixel_shader=companbot_Sprite_pal, width = 1, height = 1, tile_width = 20, tile_height = 40, x = 80, y = 32)
companbot_Sprite_pal.make_transparent(13)

splash = displayio.Group(max_size=10)
splash.append(bgDisp)
splash.append(companbot_Sprite_Disp)
splash.append(textbg_sprite)
splash.append(text_group)

minitft = minitft_featherwing.MiniTFTFeatherWing()
minitft.display.show(splash)

monoClk_last = 0
AFKTimer = 0
user_AFK = False
ani = 0
lastFrame = 0
frame = False
randomEvent = 0
xsteps = 1
ysteps = 1
nextXMove = 1
nextYMove = 1
idle = [0,2,0,2,0,2]
error = [0,4,0,4,0,4]
dance = [0,1,0,1,0,1,0,3,0,3,0,3,2,1,2,3,2,3,0,2,0,2]
companbot_x = companion.companbot(1, 0, 0, 100, 10, 1, 1)
companbot_x = helper.load(companbot_x)

#Input eater
print("Eating Inputs")
time.sleep(0.6)
# Main Loop
while True:
    try:
        buttons = minitft.buttons
        if not user_AFK:
            minitft.display.show(splash)
            minitft.backlight = 0.2
            text_area.text = "Hunger:" + str(companbot_x.hunger) + " Level:" + str(companbot_x.lvl) + " Exp:" + str(companbot_x.xp)
            digest(companbot_x, False)
            if text_area.x > -168:
                text_area.x = text_area.x - 1
            else:
                text_area.x = 160
            if buttons.a:
                if companbot_x.hunger <= 100:
                    digest(companbot_x, True)
                AFKTimer = 0
            if buttons.b:
                animate(error)
                AFKTimer = 0
            if buttons.up:
                companbot_Sprite_Disp.y, nextYMove = getY(int(companbot_Sprite_Disp.y) - 2, nextYMove)
                AFKTimer = 0
            if buttons.down:
                companbot_Sprite_Disp.y, nextYMove = getY(int(companbot_Sprite_Disp.y) + 2, nextYMove)
                AFKTimer = 0
            if buttons.left:
                companbot_Sprite_Disp.x, nextXMove = getX(companbot_Sprite_Disp.x - 2, nextXMove)
                AFKTimer = 0
            if buttons.right:
                companbot_Sprite_Disp.x, nextXMove = getX(companbot_Sprite_Disp.x + 2, nextXMove)
                AFKTimer = 0
            if buttons.select:
                menu.menu(minitft, companbot_x)
                AFKTimer = 0

            #Slow down animation
            lastFrame, frame = helper.doframe(lastFrame, frame)
            if int(companbot_x.hp) > 0:
                if frame:
                    companbot_Sprite_Disp[0] = ani
                    companbot_Sprite_Disp.x, xsteps, nextXMove = walk(companbot_Sprite_Disp.x, xsteps, nextXMove)
                    companbot_Sprite_Disp.y, ysteps, nextMove = walk(companbot_Sprite_Disp.y, ysteps, nextYMove)
                    companbot_Sprite_Disp.x, nextXMove = getX(companbot_Sprite_Disp.x, nextXMove)
                    companbot_Sprite_Disp.y, nextYMove = getY(companbot_Sprite_Disp.y, nextYMove)
                    if ani < 3:
                        ani = ani + 1
                    else:
                        ani = 0
            else:
                error = [4]
                animate(error)

            randomEvent = random.randint(0, 500)
            if randomEvent == 1:
                companbot_x.hunger = companbot_x.hunger - 1
            if randomEvent == 7:
                companbot_x.cred = int(companbot_x.cred) + 1
                text_area.x = 5
                text_area.text = "I found treasure!"
                animate(idle)
                time.sleep(0.4)
            if randomEvent == 12:
                companbot_x.xp = int(companbot_x.xp) + random.randint(1, 2)
                time.sleep(0.4)
            if randomEvent == 22:
                text_area.x = 5
                text_area.text = helper.chat()
                animate(idle)
            if randomEvent == 42:
                text_area.x = 5
                text_area.text = "Dance Time!"
                animate(dance)
            if int(companbot_x.xp) > 100:
                print("Level Up")
                companbot_x = companion.companbot.levelUp(companbot_x)
                helper.save(companbot_x)
            led[0] = (helper.get_rndRGB())
        else:
            helper.save(companbot_x)
            user_AFK, AFKTimer = sandman.sleep(minitft, user_AFK, AFKTimer)

        monoClk_last, AFKTimer, user_AFK = helper.timelasp(monoClk_last, AFKTimer, user_AFK)

    except Exception as e:
        print("Error Main: " + str(e))
        led[0] = (255, 0, 0)