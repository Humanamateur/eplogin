#!/usr/bin/env python3
from tkinter import *
from functools import partial
import os
import time
import threading

def rememberSetup(username, server):
    initFile = open("init.txt", "w")
    initFile.writelines([username.get(), server.get()])
    initFile.close()
    return

def autoLoginSetup(username, server, password, adminAccess):
    initFile = open("init.txt", "w")
    initFile.writelines([username.get(), server.get(), password.get()])
    initFile.close()

    autoLoginFile = open("autoLogin.txt", "w")
    autoLoginFile.write(adminAccess.get())
    autoLoginFile.close()

    return

def reconnectInfoUpdate(reconnectInfo, seconds):
    reconnectInfo.set("Reconnect in: " + str(seconds))
    return

def validateLogin(username, password, server, remember, autoLogin, adminAccess, reconnectInfo):
        connectToServerPartial = partial(connectToServer, username, password, server)
        connectTimer = threading.Timer(10, connectToServerPartial)

        if remember.get():
                rememberSetup(username, server)

        if autoLogin.get():
                autoLoginSetup(username, server, password, adminAccess)
                reconnectInfo.set("Reconnect in 10 seconds")
                connectTimer.start()
        else:
                connectToServer(username, password, server)
        return

def connectToServer(username, password, server):
        #os.system('xfreerdp /u:' + username.get() + ' /p:' + password.get() + ' /v:' + server.get()  + ' /f /cert-ignore')
        username.set("prihlasuju")
        return

def autoLoginValidate():
        if os.path.exists("autoLogin.txt"):
                tmp = open("autoLogin.txt", "r")
                tmpContents = tmp.read()
                tmp.close()

                if tmpContents == "disovimx":        
                        return 1

        return 0

def credRemembered():
        if os.path.exists("init.txt"):
                tmp = open("init.txt", "r")
                tmpContents = tmp.readlines()
                tmp.close()

                if len(tmpContents) >= 2:
                        return 1

        return 0

def init():
        #window
        mainWindow = Tk()
        mainWindow.geometry('1920x1080')
        mainWindow.title('Tkinter Login Form - pythonexamples.org')

        #check boxes autologin/remember
        autoLogin = IntVar()
        Checkbutton(mainWindow, text="Autologin", variable=autoLogin).grid(row=3,column=0)

        remember = IntVar()
        Checkbutton(mainWindow, text="Remember me", variable=remember).grid(row=4,column=0)

        #username label and text entry box
        Label(mainWindow, text="User Name").grid(row=0, column=0)
        username = StringVar()
        Entry(mainWindow, textvariable=username).grid(row=0, column=1)

        #password label and password entry box
        Label(mainWindow,text="Password").grid(row=1, column=0)
        password = StringVar()
        Entry(mainWindow, textvariable=password, show='*').grid(row=1, column=1)

        #server entry box
        Label(mainWindow,text="Server").grid(row=2, column=0)
        server = StringVar()
        Entry(mainWindow, textvariable = server).grid(row=2, column=1)

        #admin password for autologin
        Label(mainWindow,text="Admin password").grid(row=6, column=0)
        adminAccess = StringVar()
        Entry(mainWindow, textvariable = adminAccess).grid(row=6, column=1)
        #adminAccessHnd['status'] = DISABLED

        #reconnect info
        reconnectInfo = StringVar()
        Label(mainWindow, textvariable = reconnectInfo).grid(row=7, column=0)
        reconnectInfo.set("Autologin off")

        if credRemembered():
                initFile = open("init.txt", "r")
                content = initFile.readlines()
                initFile.close()
                username.set(content[0])
                server.set(content[1])

                if autoLoginValidate():
                        password.set(content[2])
                        autoLogin.set(1)
                        validateLogin(username, password, server, remember, autoLogin, adminAccess, reconnectInfo)

        validateLoginPartial = partial(validateLogin, username, password, server, remember, autoLogin, adminAccess, reconnectInfo)        

        #login button
        Button(mainWindow, text="Login", command=validateLoginPartial).grid(row=5, column=1)

        mainWindow.mainloop()
        return

init()