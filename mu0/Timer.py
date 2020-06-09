import time
from Gates import *
from Mu0 import *

HIGH_EDGE = 1

def timer():
    t = 0
    while True:
        #time.sleep(1)
        t = not_gate(t)
        if t == HIGH_EDGE:
            mu0_proceed()




if __name__ == '__main__':
    timer()

