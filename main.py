import time
import threading
import pygame, sys
from pygame.locals import QUIT

bcount = 1
fcount = 1



def background():
    while True:
        print(f"background {bcount}")
        bcount += 1



def foreground():
    while True:
        print(f"foreground {fcount}")
        fcount += 1


b.start()
f.start()