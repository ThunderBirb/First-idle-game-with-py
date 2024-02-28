from replit import db
import sys
import time
import threading
#import pygame
#from pygame.locals import QUIT
#pygame.init()

TPS = 1


#background processes
def background():
  bcount = 0
  while True:
    bcount += 1
    print(f"background {bcount}")
    time.sleep(1)
      
b = threading.Thread(name='background', target=background)



def main():
  b.start()
  


if __name__ == '__main__':
  main()

