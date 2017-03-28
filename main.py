# ############################################################## #
#                  - ABOUT THE PROGRAM -
# Program name : pyMsPaint main file
# Program description : changes program background on radio button
#                       click
# Author : Abdur-Rahmaan Janhangeer
# Date : 26th of March 2017
# License : MIT with emphasis :
# You are free to modify and distribute the program provided that
# attribution is  C L E A R L Y  made.
# Python version : Python 3.4
# ############################################################# #
# ############################################################# #
#                      - INDEX -
# 1 paintC class
#    -1 ellipse
#    -2 hexagon
#    -3 star5p
#    -4 line
#    -5 noFill
#    -6 solidFill
#    -7 fillColour
#    -8 strokeColour
#    -9 noStroke
#    -10 markerStroke
#    -11 solidStroke
# ############################################################# #
# ############################################################# #
#                   - CONVENTIONS USED -
# --- naming ---
# classes end with C
# ############################################################# #
# ############################################################# #
#                  - NOTES AND WARNINGS -
# ---warning---
# use a time.sleep() in your code to have time to switch to paint
# note : this may not work on your screen
# ---notes---
# one shot comments used
# ############################################################# #
# ############################################################# #
#                 - 3rd party modules needed -
# 1 pyautogui
# ############################################################# #

import pyautogui

class paintC(object):
    def __init__():
        pass
    
    def ellipse(x,y,rx,ry):
        real_x = int(x) + 22
        real_y = int(y) + 159
        radx = int(rx)
        rady = int(ry)
        pyautogui.click(420, 60)
        pyautogui.moveTo(real_x, real_y)
        pyautogui.dragRel( radx, rady, duration =0.2)
        pyautogui.mouseUp()
        pyautogui.moveTo(23,160)
        pyautogui.click()
    
    def hexagon(x,y,rx,ry):
        real_x = int(x) + 22
        real_y = int(y) + 159
        radx = int(rx)
        rady = int(ry)
        pyautogui.click(437, 80) #selecting hexagon
        pyautogui.moveTo(real_x, real_y)
        pyautogui.dragRel( radx, rady, duration =0.2)
        pyautogui.mouseUp()
        pyautogui.moveTo(23,160) #recalibrating
        pyautogui.click()
    
    def star5p(x,y,rx,ry):
        real_x = int(x) + 22
        real_y = int(y) + 159
        radx = int(rx)
        rady = int(ry)
        pyautogui.click(425, 100) #selecting hexagon
        pyautogui.moveTo(real_x, real_y)
        pyautogui.dragRel( radx, rady, duration =0.2)
        pyautogui.mouseUp()
        pyautogui.moveTo(23,160) #recalibrating
        pyautogui.click()
        
    def line(x1p,y1p,x2p,y2p):
        x1 =x1p + 22
        y1 =y1p + 159 
        x2 =x2p + 22
        y2 = y2p + 159
        pyautogui.click(380, 60)
        pyautogui.click(x1, y1)
        pyautogui.dragRel( x2-x1, y2-y1, duration =0.2)
        
    def noFill():
        pyautogui.click(560, 80)
        pyautogui.click(550, 105)
        pyautogui.click(23,160)#recalib
    def solidFill():
        pyautogui.click(560, 80, duration=0.2) #fillopsel
        pyautogui.click(560, 120, clicks=2, duration=0.2)
        pyautogui.click(23,125)#recalib     
    
    def fillColour(rp,gp,bp):         
        r =str(rp)
        g =str(gp)
        b =str(bp)
        pyautogui.click(730, 60)#fill sel
        pyautogui.click(990, 60)#customcolsel
        pyautogui.click(885, 432)#red
        pyautogui.typewrite(["backspace","backspace","backspace"])
        pyautogui.typewrite(r)
        pyautogui.click(885, 455)#green
        pyautogui.typewrite(["backspace","backspace","backspace"])
        pyautogui.typewrite(g)
        pyautogui.click(885, 478)#blue
        pyautogui.typewrite(["backspace","backspace","backspace"])
        pyautogui.typewrite(b)
        
        #pyautogui.click(800, 500)#add to custom colours
        pyautogui.click(500, 500)#ok    
    
    
    def strokeColour(rp,gp,bp): 
        pyautogui.click(23,125)#recalib     
        r =str(rp)
        g =str(gp)
        b =str(bp)
        pyautogui.click(700, 60)#str sel
        pyautogui.click(990, 60)
        pyautogui.click(885, 432)#red
        pyautogui.typewrite(["backspace","backspace","backspace"])
        pyautogui.typewrite(r)
        pyautogui.click(885, 455)#green
        pyautogui.typewrite(["backspace","backspace","backspace"])
        pyautogui.typewrite(g)
        pyautogui.click(885, 478)#blue
        pyautogui.typewrite(["backspace","backspace","backspace"])
        pyautogui.typewrite(b)
        
        #pyautogui.click(800, 500)#add to custom colours
        pyautogui.click(500, 500)#ok
        
    def noStroke():
        pyautogui.click(555, 60, duration=0.2)
        pyautogui.click(555,80, duration=0.2)
        pyautogui.click(23,125)#recalib  
    
    def markerStroke():
        pyautogui.click(555, 60)
        pyautogui.click(570, 150)
        pyautogui.click(23,125)#recalib  
    
    def solidStroke():
        pyautogui.click(555, 60) #strokeopsel
        pyautogui.click(570, 110)
        pyautogui.click(23,125)#recalib          
