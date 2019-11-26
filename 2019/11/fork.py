#!/usr/bin/python3
# filename: fork.py
# Author: lufei
# Date: 20191126 08:56:24

import platform
import os

def showinfo():
    print('Forked PID: ', os.fork())
    print('Parent PID: ', os.getpid())
    print("Python version: ",platform.python_version())



if __name__ == '__main__':
    showinfo()
