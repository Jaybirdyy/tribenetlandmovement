import numpy as np
import os

arr = np.array([['AR', 'D', 'DE', 'JG', 'PR', 'SW', 'TU','BR','PI','PPR', 'AH', 'DH', 'CH', 'JH', 'GH', 'RH', 'BH', 'SH', 'GHP', 'LCM', 'LVM', 'LJM', 'LSM', 'LAM'], [3, 5, 5, 5, 3, 8, 4, 4, 7, 3, 5, 6, 6, 6, 5, 6, 6, 7, 5, 10, 10, 10, 10, 9]])

def calculate():
    terrain = 'start'
    runningTotal = 0
    while terrain:
        terrain = input("Enter terrain of move:").strip()
        if not terrain:
            display(runningTotal)
        else:
            index = np.where(arr[0] == terrain)[0][0]
            addition = arr[1,index]
            runningTotal = runningTotal + int(addition)

def display(runningTotal):
    print("Total movement points used: " + str(runningTotal))

calculate()
os.system('pause')