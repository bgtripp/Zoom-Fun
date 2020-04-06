#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:20:16 2020

@author: Benjamin Tripp
"""

import pyautogui as pg
import time

def bgSwitch(n = 20):
    for i in range(n):
        pg.press('right')
        time.sleep(0.25)
        pg.press('left')
        time.sleep(0.25)

#bgSwitch()




def reactSwitch(n = 100):
    
    reactBox = pg.locateOnScreen("react.png", grayscale=True)
    print(n)
    while reactBox == None:
        reactBox = pg.locateOnScreen("react.png", grayscale=True)
    
    
    reactPt = pg.center(reactBox)
    
    clapPt = (reactPt.x/2 - 20, reactPt.y/2 - 60)
    thumbPt = ((reactPt.x/2 + 20, reactPt.y/2 - 60))
    
    for i in range(n):
        pg.click(reactPt.x/2, reactPt.y/2)
        pg.click(clapPt[0], clapPt[1])
        pg.click(reactPt.x/2, reactPt.y/2)
        pg.click(thumbPt[0], thumbPt[1])
        
#reactSwitch()

def chatSpam(spam = 'npaj npaj npaj npaj npaj npaj', n = 50, find=False):
    
    if (find):
        #Open chat
        
        chatBtn = pg.locateOnScreen("chat.png", grayscale=True)
        
        while chatBtn == None:
            chatBtn = pg.locateOnScreen("chat.png", grayscale=True)
        
        
        chatPt = pg.center(chatBtn)
        pg.click(chatPt.x/2, chatPt.y/2)
        
        
        #Click in text box
        
        toBox = pg.locateOnScreen("toEveryone.png", grayscale=True)
        
        while toBox == None:
            toBox = pg.locateOnScreen("toEveryone.png", grayscale=True)
        
        
        toBox = pg.center(toBox)
        pg.click(toBox.x/2, toBox.y/2 + 40)
    
    #Type spam
    
    for i in range(n):
        pg.write(spam)
        pg.press('enter')
    
    
    
#chatSpam()
        
def rename(name='Fat Susan'):
    
    muteBtn = pg.locateOnScreen("mute.png", grayscale=True)
        
    while muteBtn == None:
        muteBtn = pg.locateOnScreen("mute.png", grayscale=True)
         
    mutePt = pg.center(muteBtn)
    pg.click(mutePt.x/2 + 20, mutePt.y/2) #For little settings menu
    
    time.sleep(0.1)
    
    pg.click(mutePt.x/2 + 20, mutePt.y/2 + 85) #For rename
    
    
    pg.keyDown('delete')
    time.sleep(0.5)
    pg.keyUp('delete')
    
    pg.write(name)
    pg.press('enter')

rename()
        

    