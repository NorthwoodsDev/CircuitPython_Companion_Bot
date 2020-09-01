import os
import storage
import time
import board
import random
import microcontroller

def get_rndRGB():
    a = (random.randint(20, 235))
    b = (random.randint(20, 235))
    c = (random.randint(20, 235))
    return (a,b,c)

def timelasp(monoClk_last, monoClk_Interact, user_AFK):
    try:
        monoClk = time.monotonic()
        monoClk_eclip = monoClk - monoClk_last
        if monoClk_eclip > 60:
            monoClk_last = monoClk
            monoClk_Interact += 1

        if monoClk_Interact > 5:
            user_AFK = True
        else:
            user_AFK = False
    except Exception as e:
        print("Error Timer:" + str(e))

    return monoClk_last, monoClk_Interact, user_AFK

def doframe(lastFrame, frame):
    try:
        frame = False
        monoClk = time.monotonic()
        frameEclip = monoClk - lastFrame
        if frameEclip > 0.3:
            lastFrame = monoClk
            frame = True
    except Exception as e:
        print("Error Frame:" + str(e))

    return lastFrame, frame

def save(companbot_x_stat):
    try:
        print ("Saving")
        storage.remount("/", False)
        eventLog = open("save.csv", "w+")
        eventLog.write(str(companbot_x_stat.xp) + "," + str(companbot_x_stat.lvl)+ "," + str(companbot_x_stat.hp) + "," + str(companbot_x_stat.pAtk) + "," + str(companbot_x_stat.pDef) + "," + str(companbot_x_stat.cred) + '\n')
        eventLog.close()
        storage.remount("/", True)
    except Exception as e:
        print ("Error writing log: " + str(e))
        storage.remount("/", True)
    return

def load(companbot_x):
    try:
        eventLog = open("save.csv", "r")
        sf = eventLog.read()
        sfa = sf.split(',')
        companbot_x.xp = sfa[0].strip()
        companbot_x.lvl = sfa[1].strip()
        companbot_x.hp = sfa[2].strip()
        companbot_x.pAtk = sfa[3].strip()
        companbot_x.pDef = sfa[4].strip()
        companbot_x.cred = sfa[5].strip()
    except Exception as e:
        print ("Error loading save: " + str(e))
    return companbot_x

def chat():
    sayWhat = ["Hello.",
    "Ahcooo!",
    "Stay cool.",
    "Just keep walking.",
    "Groovy.",
    "I'm having Fun!",
    "Have you seen my friends?",
    "Let's Adventure!",
    "Wonder what to do next?",
    "Chilldogs.",
    "Do you like to dance?",
    "When do we eat?",
    "Let's play Blackjack!",
    "Watch out for monsters.",
    "Hmm...Hm.Hmm. Oh!",
    "What you doing?"]
    say = sayWhat[random.randint(0, 15)]
    return say