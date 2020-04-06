#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:23:24 2020

@author: Ben
"""

import pyautogui as pg

def bgSwitch(n = 20):
    for i in range(n):
        pg.press('right')
        pg.press('left')

bgSwitch()