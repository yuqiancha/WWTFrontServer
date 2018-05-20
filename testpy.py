import os

from os import path

with open(file=os.getcwd() + '/FrontServerID', mode='r') as file:
    t1 = file.read()
    print(t1)


with open(file=os.getcwd() + '/WaitCarComeTime', mode='r') as file:
    t1 = file.read()
    print(t1)

with open(file=os.getcwd() + '/WaitCarLeaveTime', mode='r') as file:
    t1 = file.read()
    print(t1)

with open(file=os.getcwd() + '/AfterCarLeaveTime', mode='r') as file:
    t1 = file.read()
    print(t1)