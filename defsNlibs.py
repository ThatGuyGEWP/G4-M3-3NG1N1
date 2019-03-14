import time, random, sys, keyboard
from colorama import Fore
import subprocess as sp
sp.call('clear',shell=True)
#Please refer to the Read me file
#For instructions on use


def openz():
 green()
 clear()
 typeEffect("Powered by G4M3 3NG1N3 V0.6",0.1,0.8)
 white()
 clear()

def repeat(num,code):
 for x in range(0,num):
   code

def clear():
  tmp = sp.call('clear',shell=True)

def wait(oof):
  time.sleep(oof)


def typeEffect(string,spd,waip):
 for char in string:
    sys.stdout.write(char)
    sys.stdout.flush() 
    wait(spd)
 wait(waip)
 print('')

def test():
 clear()
 print("Testing libs")
 wait(0.4)
 clear()
 white()
 wait(0.1)
 print("w")
 yellow()
 wait(0.1)
 print("y")
 green()
 wait(0.1)
 print("G")
 clear()

def white():
  print(Fore.WHITE)


def yellow():
 print(Fore.YELLOW)


def green():
 print(Fore.GREEN)

def typeEffect2(a,b,spd,waip):
  words = a,b
  text = ""
  for char in words:
    text = text + char
    print(text) 
    wait(spd)
    clear()
  print(a,b)
  wait(waip)


def testlibs():
 white()
 typeEffect("G4M3 3NG1N3 V0.6",0.1,1)
 yellow()
 test()
 green()
 print("No Errors Found In Data")
 print("All Libs Loaded Thank you")
 print("For using Game Engine V0.5!")
 wait(2.2)
 clear()
