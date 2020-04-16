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
        
        self.scroll = False
        
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text="Zoom Fun").grid(row=0, column=0)
        
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        ttk.Label(self.frame_content, text="Name Flasher").grid(row=0, column=1)
        ttk.Label(self.frame_content, text="Name 1:").grid(row=1, column=0)
        ttk.Label(self.frame_content, text="Name 2:").grid(row=2, column=0)
        
        self.entry_name1 = ttk.Entry(self.frame_content, width = 24)
        self.entry_name1.grid(row=1, column=1)
        self.entry_name2 = ttk.Entry(self.frame_content, width = 24)
        self.entry_name2.grid(row=2, column=1)
        self.scroll = BooleanVar()
        self.scroll_button = ttk.Checkbutton(self.frame_content, text="Scroll On", variable = self.scroll)
        self.scroll_button.grid(row=1, column = 2)

        ttk.Button(self.frame_content, text='Go', command= self.rename).grid(row=3, column=1)
        
        
    def rename(self):
    
        name1 = self.entry_name1.get()
        name2 = self.entry_name2.get()
        
        scroll = self.scroll
        
        
        name1Last = True
        
        muteBtn = pg.locateOnScreen("mute.png", grayscale=True)
            
        while muteBtn == None:
            muteBtn = pg.locateOnScreen("mute.png", grayscale=True)
             
        mutePt = pg.center(muteBtn)
        
        if (scroll):
            while True:
                
                name1 = name1[2:] + name1[0:2]
                
                pg.click(mutePt.x/2 + 20, mutePt.y/2) #For little settings menu
                
                time.sleep(0.1)
                
                pg.click(mutePt.x/2 + 20, mutePt.y/2 + 85) #For rename
                
                pg.press('backspace', 10)
                
                pg.write('**'+name1+'**')
                pg.press('enter')
        else:
            while True:
                
                
                pg.click(mutePt.x/2 + 20, mutePt.y/2) #For little settings menu
                
                time.sleep(0.1)
                
                pg.click(mutePt.x/2 + 20, mutePt.y/2 + 85) #For rename
                
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