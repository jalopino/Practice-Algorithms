import pymem
import pymem.process
import time
import keyboard
import psutil
import os
import sys
from tkinter import *
from threading import Thread

#CopyPasted
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
#Check for process ID

#Offsets
dwLocalPlayer = (0xD892AC)
dwForceJump = (0x524ACB4)
m_fFlags = (0x104)
m_flFlashMaxAlpha = (0xA41C)
m_iTeamNum = (0xF4)
dwEntityList = (0x4DA0D54)
m_bSpotted = (0x93D)
dwGlowObjectManager = (0x52E9348)
m_bDormant = (0xED)
m_iGlowIndex = (0xA438)

#BunnyHop
def bunnyHop():
    forceJump = client + dwForceJump
    localPlayer = window.read_int(client + dwLocalPlayer)
    while True:
        if (enableBunny):
            if keyboard.is_pressed("space"):
                flags = window.read_int(localPlayer + m_fFlags)
                if (localPlayer and (flags == 257 or flags == 263)):
                    window.write_int(forceJump, 6)
                    time.sleep(0.2)
                    window.write_int(forceJump, 4)

#RadarHack
def radarHack():
    while True:
        if (enableRadar):
            if window.read_int(client + dwLocalPlayer):
                localPlayer = window.read_int(client + dwLocalPlayer)
                myTeam = window.read_int(localPlayer + m_iTeamNum)
                for i in range(64):
                    if window.read_int(client + dwEntityList + i * 0x10):
                        entity = window.read_int(client + dwEntityList + i * 0x10)
                        entity_team = window.read_int(entity + m_iTeamNum)
                        if entity_team != myTeam:
                            window.write_int(entity + m_bSpotted, 1)

#GlowHack
global R, G, B, A
global glowCurrentPlayer
global glowCurrentPlayerTeam

def glowHack():
    while True:
        if (enableGlow):
            localPlayer = window.read_int(client + dwLocalPlayer)
            glowObj = window.read_int(client + dwGlowObjectManager)
            myTeam = window.read_int(localPlayer + m_iTeamNum)
            for x in range(32):
                glowCurrentPlayer = window.read_int(client + dwEntityList + x * 0x10)
                if glowCurrentPlayer:
                    entity_glow = window.read_int(glowCurrentPlayer + m_iGlowIndex)
                    glowCurrentPlayerTeam = window.read_int(glowCurrentPlayer + m_iTeamNum)
                    glowCurrentPlayerDormant = window.read_int(glowCurrentPlayer + m_bDormant);
                    if (glowCurrentPlayerDormant == False):
                        if glowCurrentPlayerTeam != myTeam:  # Enemy Team Glow
                            time.sleep(0.002)
                            window.write_float(glowObj + entity_glow * 0x38 + 0x4, float(1))  # R
                            window.write_float(glowObj + entity_glow * 0x38 + 0x8, float(0))  # G
                            window.write_float(glowObj + entity_glow * 0x38 + 0xC, float(0))  # B
                            window.write_float(glowObj + entity_glow * 0x38 + 0x10, float(1))  # Alpha
                            window.write_int(glowObj + entity_glow * 0x38 + 0x24, 1)  # Enable glow

#Buttons
def enableBunnyHopHack():
    global enableBunny
    if (enableBunny):
        enableBunny = False
        strBunny = Label(GUI, text='DISABLED', fg="red")
        strBunny.grid(row=3, column=3)
    else:
        enableBunny = True
        strBunny = Label(GUI, text='ENABLED', fg="green")
        strBunny.grid(row=3, column=3)


def enableRadarHack():
    global enableRadar
    if (enableRadar):
        enableRadar = False
        strRadar = Label(GUI, text='DISABLED', fg="red")
        strRadar.grid(row=5, column=3)
    else:
        enableRadar = True
        strRadar = Label(GUI, text='ENABLED', fg="green")
        strRadar.grid(row=5, column=3)

def enableGlowhack():
    global enableGlow
    if (enableGlow):
        enableGlow = False
        strGlow = Label(GUI, text='DISABLED', fg="red")
        strGlow.grid(row=7, column=3)
    else:
        enableGlow = True
        strGlow = Label(GUI, text='ENABLED', fg="green")
        strGlow.grid(row=7, column=3)

def exitHack():
    global enableBunny
    global enableRadar
    global enableGlow
    enableRadar = False
    enableBunny = False
    enableGlow = False
    GUI.destroy()

#Main Func
def main():
    # Variables
    global client
    global window
    # Booleans--------
    global enableBunny
    global enableRadar
    global enableGlow
    enableRadar = True
    enableBunny = True
    enableGlow = True
    #-----------------
    while True:
        os.system("cls")
        print("Python BunnyHop Script!")
        if checkIfProcessRunning("csgo"):
            window = pymem.Pymem("csgo.exe")
            client = pymem.process.module_from_name(window.process_handle, "client.dll").lpBaseOfDll
            break
        else:
            print("Could not find process! Checking....")
            time.sleep(1)

    Thread(target= bunnyHop).start()
    Thread(target= radarHack).start()
    Thread(target= glowHack).start()

    # GUI
    global GUI
    GUI = Tk(className="Private Hack by Jalo")
    BUNNYHOP = Button(GUI, text="Bunny Hop", fg="green", command=enableBunnyHopHack)
    RADAR = Button(GUI, text="Radar Hack", fg="green", command=enableRadarHack)
    GLOWHACK = Button(GUI, text="Glow Hack", fg="green", command=enableGlowhack)
    CREDS = Label(GUI, text='Jalopino Hack!', fg="blue")
    EXIT = Button(GUI, text="CLOSE HACK", fg="red", command=exitHack)
    FAGGOT = Label(GUI, text='MADE BY JALOPINO', fg="red", font="Times 22 bold")
    FAGGOT.grid(row=3, column=6)
    EXIT.grid(row=9, column=1)
    CREDS.grid(row=1, column=1)
    BUNNYHOP.grid(row=3, column=1)
    RADAR.grid(row=5, column=1)
    GLOWHACK.grid(row=7, column=1)
    GUI.mainloop()
    sys.exit(0)

if __name__ == '__main__':
    main()







