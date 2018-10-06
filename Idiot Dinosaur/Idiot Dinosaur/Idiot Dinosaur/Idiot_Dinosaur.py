import pyautogui
import time
import numpy as np
import cv2

import win32gui
import win32api

from mss import mss

TIME_BETWEEN_FRAMES = 0.01
TIME_BETWEEN_GAMES = 0.5

class Cordinates(object):
    #vi tri cua cac object
    replay_pos = (390,410) # vi tri cua button replay
    # replay_pos = (520, 390)

def restart_game():
    pyautogui.click(Cordinates.replay_pos)

def press_up():
    pyautogui.keyDown("up") # press a key down
    time.sleep(0.02)
    print("Jump")
    pyautogui.keyUp("up") # release a key

BLANK_BOX = 247000

def get_cactus_box_value():
    cactus_box = {'left': 270, 'top':420, 'width': 50, 'height': 20}
    sct = mss()
    img = np.array(sct.grab(cactus_box))[:,:,:3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #dc = win32gui.GetDC(1)
    #red = win32api.RGB(255,0,0)
    #win32gui.SetPixel(dc,0,0,red)

    return gray.sum()

GAMEOVER_RANGE = [620000, 660000]

def check_gameover(gameover_range = GAMEOVER_RANGE):
    result = False
    gameover_box = {'left': 290, 'top': 360, 'width': 200, 'height': 15}

    sct = mss()
    img = np.array(sct.grab(gameover_box))[:,:,:3]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    curr_state = gray.sum()
    if curr_state < GAMEOVER_RANGE[1] and curr_state > GAMEOVER_RANGE[0]:
        result = True
    return result

def mai2n():
    while True:
        gameover_state = check_gameover()
        print("Game over: " + str(gameover_state))
        if gameover_state:
            time.sleep(TIME_BETWEEN_GAMES)
            print("Game over. Restart game")
            restart_game()
        cactus_state = get_cactus_box_value()
        if(cactus_state != BLANK_BOX):
            press_up()
            time.sleep(TIME_BETWEEN_FRAMES)
#mai2n()



#import win32gui
#import sys

#from re import match
#def draw_line():
#    print ('x1,y1,x2,y2?')
#    s=input()
#    if match('\d+,\d+,\d+,\d+',s):
#        x1,y1,x2,y2=s.split(',')
#        x1=int(x1)
#        y1=int(y1)
#        x2=int(x2)
#        y2=int(y2)
#        hwnd=win32gui.WindowFromPoint((x1,y1))
#        hdc=win32gui.GetDC(hwnd)
#        x1c,y1c=win32gui.ScreenToClient(hwnd,(x1,y1))
#        x2c,y2c=win32gui.ScreenToClient(hwnd,(x2,y2))
#        win32gui.MoveToEx(hdc,x1c,y1c)
#        win32gui.LineTo(hdc,x2c,y2c)
#        win32gui.ReleaseDC(hwnd,hdc)
#    main()
#def draw_point():
#    print ('x,y,color?')
#    s=input()
#    if match('\d+,\d+,\d+',s):
#        x,y,color=s.split(',')
#        x=int(x)
#        y=int(y)
#        color=int(color)
#        hwnd=win32gui.WindowFromPoint((x,y))
#        hdc=win32gui.GetDC(hwnd)
#        x1,y1=win32gui.ScreenToClient(hwnd,(x,y))
#        win32gui.SetPixel(hdc,x1,y1,color)
#        win32gui.ReleaseDC(hwnd,hdc)
#    main()
#def get_pixel_col():
#    print ('x,y?')
#    s=input()
#    if match('\d+,\d+',s):
#        x,y=s.split(',')
#        x=int(x)
#        y=int(y)
#        hwnd=win32gui.WindowFromPoint((x,y))
#        hdc=win32gui.GetDC(hwnd)
#        x1,y1=win32gui.ScreenToClient(hwnd,(x,y))
#        color=win32gui.GetPixel(hdc,x1,y1)
#        win32gui.ReleaseDC(hwnd,hdc)
#        print (color)
#    main()
#def get_current_pos_info():
#    x,y=win32gui.GetCursorPos()
#    hwnd=win32gui.WindowFromPoint((x,y))
#    hdc=win32gui.GetDC(hwnd)
#    x1,y1=win32gui.ScreenToClient(hwnd,(x,y))
#    print( x,y,win32gui.GetPixel(hdc,x1,y1))
#    win32gui.ReleaseDC(hwnd,hdc)
#    main()
#def main():
#    print ('''l. draw line
#p. draw point
#g. get pixel color
#c. get current mouse position's info''')
#    s = input()
#    if s.lower()=='l':
#        draw_line()
#    if s.lower()=='p':
#        draw_point()
#    if s.lower()=='g':
#        get_pixel_col()
#    if s.lower()=='c':
#        get_current_pos_info()
#main()