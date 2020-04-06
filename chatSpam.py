#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:24:00 2020

@author: Ben
"""
import pyautogui as pg

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
    
    
    
chatSpam()