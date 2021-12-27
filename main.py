import keyboard
import pyautogui as pg
import time
import cv2
import numpy as np


img = cv2.imread("input/owl-vector-cliart-black-white-cute-owl-vector-black-white-115463524.png")
img = cv2.resize(img, (0, 0), fx=0.8, fy=0.8)
white = np.where((img[:, :, 0] < 200) & (img[:, :, 1] < 200) & (img[:, :, 2] < 200))
black = np.where((img[:, :, 0] >= 200) & (img[:, :, 1] >= 200) & (img[:, :, 2] >= 200))

img[black] = (255, 255, 255)
img[white] = (0, 0, 0)
pg.PAUSE = 0.001
pg.FAILSAFE = True


def draw(number_of_pixel):
    pg.dragTo(pg.position()[0] + number_of_pixel, pg.position()[1], duration=0, button='left')


def next_line():
    pg.moveTo(starting_x, pg.position()[1] + 1)


time.sleep(4)
currentMouseX, currentMouseY = pg.position()
starting_x = currentMouseX
for row in img:
    length_draw = 0
    length_move = 0
    for pixel in row:
        if keyboard.is_pressed('q'):
            quit()
        if list(pixel) == [0, 0, 0]:
            if length_move > 0:
                pg.move(length_move, 0)
            length_move = 0
            length_draw += 1
        else:
            if length_draw > 0:
                draw(length_draw)

            length_draw = 0
            length_move += 1
    if list(pixel) == [0, 0, 0]:
        pg.move(length_move, 0)
        draw(length_draw)
    next_line()
