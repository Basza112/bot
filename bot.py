import os, sys, time

def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

bot = raw_input ("You : ")

if bot == 3:
        os.system ("cat support.txt")
else:
        os.system ("cat support.txt")
        restart_program()
