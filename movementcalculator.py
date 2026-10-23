import numpy as np
import os
import sys

arr = np.array([['AR', 'D', 'DE', 'JG', 'PR', 'SW', 'TU','BR','PI','PPR', 'AH', 'DH', 'CH', 'JH', 'GH', 'RH', 'BH', 'SH', 'GHP', 'LCM', 'LVM', 'LJM', 'LSM', 'LAM'], [3, 5, 5, 5, 3, 8, 4, 4, 7, 3, 5, 6, 6, 6, 5, 6, 6, 7, 5, 10, 10, 10, 10, 9]])
maxMove = int(input("Enter total movement points: ").strip())

def calculate():
    terrain = 'start'
    runningTotal = 0
    addition = 0
    while terrain:
        terrain = input("Enter terrain of destination:").strip()
        if not terrain:
            display(runningTotal)

        elif (int(addition) + int(runningTotal)) <= maxMove:
            index = np.where(arr[0] == terrain)[0][0]
            addition = int(arr[1,index])
            runningTotal = runningTotal + addition

            if int(runningTotal) >= maxMove:
                print("Limit reached! Movement used:" + str(runningTotal))
                endTask()

        else:
            print("Limit reached! Last move excluded. Movement used:" + str(runningTotal))
            endTask()

def display(runningTotal):
    print("Total movement points used: " + str(runningTotal))

def endTask():
    os.system('pause')
    sys.exit(0)

calculate()
endTask()
