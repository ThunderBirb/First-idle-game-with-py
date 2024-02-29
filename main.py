import replit
from replit import db
import sys
import time
import threading
TPS = 1


class Player():
  def __init__(self, name, money, exp, level, boosts: list):



#background processes
def background():
  global bcount
  bcount = 0
  while True:
    bcount += 1
    print(f"background count: {bcount}")
    time.sleep(1/TPS)


b = threading.Thread(name='background', target=background)




"""main stand-in"""
b.start()

