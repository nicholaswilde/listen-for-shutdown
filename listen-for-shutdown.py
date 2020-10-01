#!/usr/bin/env python

from gpiozero   import Button
from signal     import pause
from subprocess import call
import os

PIN_NO = 18
HOLD_TIME=2

def longpress():
    print("Shutting down")
    os.system('sudo turn-off-nodes.sh')
    call(['shutdown', '-h', 'now'], shell=False)

def main():
    button = Button(PIN_NO, hold_time=HOLD_TIME)
    button.when_held = longpress
    print("Staring listen for shutdown")
    pause()

if __name__ == "__main__":
    main()
