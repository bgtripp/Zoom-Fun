#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 15:20:16 2020

@author: Benjamin Tripp
"""

import pyautogui as pg
import time
from tkinter import *
from tkinter import ttk



class ZoomFun:
    
    def __init__(self, master):
        
        self.font = 'Arial'
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text="ZoomFun", font = (self.font, 48)).grid(row=1, column=0)
        
        
        self.frame_rename = ttk.Frame(master)
        self.frame_rename.pack()
        ttk.Label(self.frame_rename, text="Name Flasher", font = (self.font, 20)).grid(row=0, column=1)
        ttk.Label(self.frame_rename, text="Name 1:", font = (self.font, 16)).grid(row=1, column=0)
        ttk.Label(self.frame_rename, text="Name 2:", font = (self.font, 16)).grid(row=2, column=0)
        
        self.entry_name1 = ttk.Entry(self.frame_rename, width = 24)
        self.entry_name1.grid(row=1, column=1)
        self.entry_name2 = ttk.Entry(self.frame_rename, width = 24)
        self.entry_name2.grid(row=2, column=1)
        
        self.scroll = BooleanVar()
        self.scroll_button = ttk.Checkbutton(self.frame_rename, text="Scroll", variable = self.scroll)
        self.scroll_button.grid(row=1, column = 2)
        
        self.muted = BooleanVar()
        self.muted_button = ttk.Checkbutton(self.frame_rename, text="Muted", variable = self.muted)
        self.muted_button.grid(row=2, column = 2)

        ttk.Button(self.frame_rename, text='Go', command= self.rename).grid(row=3, column=1)
        
        self.frame_footer = ttk.Frame(master)
        self.frame_footer.pack()
        ttk.Label(self.frame_footer, text="©2020, Benjamin Tripp. All rights reserved. | v0.9.5", font = (self.font, 10, 'italic')).grid(row=1, column=0)
        
        
    def rename(self):
    
        name1 = self.entry_name1.get()
        name2 = self.entry_name2.get()
        
        scroll = self.scroll.get()
        muted = self.muted.get()
        
        
        name1Last = True
        
        if (muted):
            muteBtn = pg.locateOnScreen("unmute.png", grayscale=True)
                
            while muteBtn == None:
                muteBtn = pg.locateOnScreen("unmute.png", grayscale=True)
                 
            mutePtMis = pg.center(muteBtn)
            mutePt = (mutePtMis.x + 20, mutePtMis.y)

            
        else:  
            muteBtn = pg.locateOnScreen("mute.png", grayscale=True)
                
            while muteBtn == None:
                muteBtn = pg.locateOnScreen("mute.png", grayscale=True)
                 
            mutePt = pg.center(muteBtn)
        
        if (scroll):
            while True:
                
                name1 = name1[2:] + name1[0:2]
                
                pg.click(mutePt[0]/2 + 20, mutePt[1]/2) #For little settings menu
                
                time.sleep(0.1)
                
                pg.click(mutePt[0]/2 + 20, mutePt[1]/2 + 85) #For rename
                
                pg.press('backspace', 10)
                
                pg.write('**'+name1+'**')
                pg.press('enter')
        else:
            while True:
                
                
                pg.click(mutePt[0]/2 + 20, mutePt[1]/2) #For little settings menu
                
                time.sleep(0.1)
                
                pg.click(mutePt[0]/2 + 20, mutePt[1]/2 + 85) #For rename
                
                pg.press('backspace', 10)
                
                if (name1Last):
                    name = name1
                else:
                    name = name2
                
                pg.write(name)
                pg.press('enter')
                
                name1Last = not name1Last
        
    
def main():
    
    root = Tk()
    zoomFun = ZoomFun(root)
    root.mainloop()
    
if __name__ == "__main__": main()