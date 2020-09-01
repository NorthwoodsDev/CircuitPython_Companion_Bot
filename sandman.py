import displayio

def sleep(minitft, user_AFK, AFKTimer):
    print("Going to Sleep")
    try:
        color_bitmap = displayio.Bitmap(160, 80, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0x000000

        bg_sleep = displayio.TileGrid(color_bitmap,pixel_shader=color_palette,x=0, y=0)
        sleepScreen = displayio.Group(max_size=1)
        sleepScreen.append(bg_sleep)

        while user_AFK:
            buttons = minitft.buttons
            minitft.display.show(sleepScreen)
            minitft.backlight = 0
            if buttons.a:
                print("Waking Up")
                user_AFK = False
                AFKTimer = 0
                break
            if buttons.b:
                print("Waking Up")
                user_AFK = False
                AFKTimer = 0
                break
            if buttons.up:
                print("Waking Up")
                user_AFK = False
                AFKTimer = 0
                break
            if buttons.down:
                print("Waking Up")
                user_AFK = False
                AFKTimer = 0
                break
            if buttons.left:
                print("Waking Up")
                user_AFK = False
                AFKTimer = 0
                break
            if buttons.right:
                print("Waking Up")
                user_AFK = False
                AFKTimer = 0
                break
            if buttons.select:
                print("Waking Up")
                user_AFK = False
                AFKTimer = 0
                break
        print("Blap")
    except Exception as e:
        print("Error Main: " + str(e))
        minitft.backlight = 1
        #user_AFK = False
    minitft.backlight = 1
    return user_AFK, AFKTimer