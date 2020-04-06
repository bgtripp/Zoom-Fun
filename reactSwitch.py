#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:23:28 2020

@author: Ben
"""

import pyautogui as pg

def reactSwitch(n = 20):
    
    reactBox = pg.locateOnScreen("react.png", grayscale=True)
    
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
        
reactSwitch()