
#!/usr/bin/env python3
from tkinter import *
import os
import platform
from tkinter import font as tkFont

def getEthMac():
  try:
    mac = open('/sys/class/net/eth0/address').readline()
  except:
    mac = "00:00:00:00:00:00"
  return mac[0:17]
def getWifiMac():
  try:
    mac = open('/sys/class/net/wlan0/address').readline()
  except:
    mac = "00:00:00:00:00:00"
  return mac[0:17]
def hostNameSet(hostname):
    initFile = open("/etc/hostname", "w")
    initFile.write(hostname.get)
    initFile.close()
    return
def switch(mode.get):
        switcher={
                0:"RD_STATION_MODE",
                1:"KIOSK_MODE",
                2:"COMANDLINE_MODE",
                3:"CREATIVE_MODE",
                }
        func=mode.get(i,lambda :'Invalid')
        return func()

def init():
    #colors
    bgColor = "#E34432"
    fgColor = "#F5B111"
    bgEntryColor = "#381610"
    fgEntryColor = "#D1D1C2"
    #window
    mainWindow = Tk()
    screenW = mainWindow.winfo_screenwidth()
    screenH = mainWindow.winfo_screenheight()
    mainWindow.geometry(str(screenW) + 'x' + str(screenH))
    mainWindow.title('ELECTROPOLI_RPI_CONFIG')
    mainWindow['bg'] = fgEntryColor
    #mainWindow.overrideredirect(True)
    #fonts
    Gothic7B = tkFont.Font(family="Gothic", size=int(screenH/15), weight="bold")
    Gothic54 = tkFont.Font(family="Gothic", size=int(screenH/54))
    Gothic30B = tkFont.Font(family="Gothic", size=int(screenH/30), weight="bold")
    #Title 
    titleLabel = Label(mainWindow, text="ELECTROPOLI_RPI_CONFIG")
    titleLabel.place(relx=0.2, rely=0.1)
    titleLabel['font'] = Gothic7B
    titleLabel['bg'] = fgEntryColor
    titleLabel['fg'] = bgEntryColor
    #Mac label and text entry box
    lMacNameLabelHnd = Label(mainWindow, text="eth0 : " + getEthMac() )
    lMacNameLabelHnd.place(relx=0.75, rely=0.6)
    lMacNameLabelHnd['font'] = Gothic54
    lMacNameLabelHnd['bg'] = fgEntryColor
    lMacNameLabelHnd['fg'] = bgEntryColor
    wMacNameLabelHnd = Label(mainWindow, text="wlan0: " + getWifiMac() )
    wMacNameLabelHnd.place(relx=0.75, rely=0.65)
    wMacNameLabelHnd['font'] = Gothic54
    wMacNameLabelHnd['bg'] = fgEntryColor
    wMacNameLabelHnd['fg'] = bgEntryColor
    #hostNeme label and text entry box
    hostNemeLabelHnd = Label(mainWindow, text="HOSTNAME:", )
    hostNemeLabelHnd.place(relx=0.35, rely=0.4)
    hostNemeLabelHnd['font'] = Gothic30B
    hostNemeLabelHnd['bg'] = fgEntryColor
    hostNemeLabelHnd['fg'] = bgEntryColor
    hostname = StringVar()
    hostNemeEntryHnd = Entry(mainWindow, textvariable=hostname)
    hostNemeEntryHnd.place(relx=0.35, rely=0.47)
    hostNemeEntryHnd['font'] = Gothic30B
    hostNemeEntryHnd['bg'] = bgEntryColor
    hostNemeEntryHnd['fg'] = fgEntryColor
    
    #Mode Switch button
    mode = StringVar()
    modeSwitchButtonHnd = Radiobutton(mainWindow, text="RD_STATION_MODE", variable=mode, value ="RD_STATION_MODE")
    modeSwitchButtonHnd.place(relx=0.35, rely=0.53)
    modeSwitchButtonHnd['font'] = Gothic54
    modeSwitchButtonHnd['bg'] = bgColor
    modeSwitchButtonHnd['fg'] = fgColor
    modeSwitchButtonHnd['activebackground'] = bgColor
    modeSwitchButtonHnd['activeforeground'] = fgColor
    modeSwitchButtonHnd2 = Radiobutton(mainWindow, text="LINUX_KIOSK_MODE", variable=mode, value ="LINUX_KIOSK_MODE")
    modeSwitchButtonHnd2.place(relx=0.35, rely=0.57)
    modeSwitchButtonHnd2['font'] = Gothic54
    modeSwitchButtonHnd2['bg'] = bgColor
    modeSwitchButtonHnd2['fg'] = fgColor
    modeSwitchButtonHnd2['activebackground'] = bgColor
    modeSwitchButtonHnd2['activeforeground'] = fgColor
    modeSwitchButtonHnd3 = Radiobutton(mainWindow, text="COMANDLINE_MODE", variable=mode, value ="COMANDLINE_MODE")
    modeSwitchButtonHnd3.place(relx=0.35, rely=0.61)
    modeSwitchButtonHnd3['font'] = Gothic54
    modeSwitchButtonHnd3['bg'] = bgColor
    modeSwitchButtonHnd3['fg'] = fgColor
    modeSwitchButtonHnd3['activebackground'] = bgColor
    modeSwitchButtonHnd3['activeforeground'] = fgColor
    modeSwitchButtonHnd4 = Radiobutton(mainWindow, text="CREATIVE_MODE", variable=mode, value ="CREATIVE_MODE")
    modeSwitchButtonHnd4.place(relx=0.35, rely=0.65)
    modeSwitchButtonHnd4['font'] = Gothic54
    modeSwitchButtonHnd4['bg'] = bgColor
    modeSwitchButtonHnd4['fg'] = fgColor
    modeSwitchButtonHnd4['activebackground'] = bgColor
    modeSwitchButtonHnd4['activeforeground'] = fgColor

    #Konfig button
    konfigButtonHnd = Button(mainWindow, text="KONFIGUROVAT" )# command=configurate)
    konfigButtonHnd.place(relx=0.4, rely=0.8)
    konfigButtonHnd['font'] = Gothic30B
    konfigButtonHnd['bg'] = bgEntryColor
    konfigButtonHnd['fg'] = fgEntryColor


    #mainLoop
    mainWindow.mainloop()
    return         
init()