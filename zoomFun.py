#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:20:16 2020

@author: Benjamin Tripp
"""

import pyautogui as pg
import time

def bgSwitch():
    for i in range(20):
        pg.press('right')
        pg.press('left')

#bgSwitch()




def reactSwitch():
    
    reactBox = pg.locateOnScreen("react.png", grayscale=True)
    
    while reactBox == None:
        reactBox = pg.locateOnScreen("react.png", grayscale=True)
    
    
    reactPt = pg.center(reactBox)
    
    clapPt = (reactPt.x/2 - 20, reactPt.y/2 - 60)
    thumbPt = ((reactPt.x/2 + 20, reactPt.y/2 - 60))
    
    for i in range(20):
        pg.click(reactPt.x/2, reactPt.y/2)
        pg.click(clapPt[0], clapPt[1])
        pg.click(reactPt.x/2, reactPt.y/2)
        pg.click(thumbPt[0], thumbPt[1])
        
#reactSwitch()

def chatSpam():
    
    chatBtn = pg.locateOnScreen("chat.png", grayscale=True)
    
    while chatBtn == None:
        chatBtn = pg.locateOnScreen("chat.png", grayscale=True)
    
    
    chatPt = pg.center(chatBtn)
    pg.click(chatPt.x/2, chatPt.y/2)
    
#chatSpam()
    