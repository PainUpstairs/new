import matplotlib.pyplot as plt
import numpy as np
import random

def getRightSide(data, s, e):
    listR = []
    for j in range (s, e):
        for i in range(0, len(data)):
            if data[i] == j:
                listR.append(data[i])
# fsgfg
    return listR

def getLeftSide(data, s, e):
    listL =[]
    for j in range(s, e, -1):
        for i in range(0, len(data)):
            if data[i] == j:
                listL.append(data[i])
    
    return listL

data = []
for i in range(0, 15):
    # Random numbers 
    data.append(random.randint(0,99))

print("Original String: ",data)

start_val= 50
right_side = []
left_side = []
end_track = 99
start_track = 0

for i in range( 0, len(data)):
    if start_val == data[i]:
        data.remove(start_val)

mainSeq = []
mainSeq.append(start_val)

right_side = getRightSide(data, start_val, end_track)
left_side = getLeftSide(data, start_val, start_track)

print("Right Side",right_side)
print("Left Side", left_side)

for i in range ( 0, len(right_side)):
    mainSeq.append(right_side[i])

for i in range ( 0, len(left_side)):
    mainSeq.append(left_side[i])

print("Look Disk Scheduling Algorthm:", mainSeq)

y = []
for i in range( 0 , len(data)+1):
    y.append(-(i+1))

print(y)

print( max(data))
print(min(data))
totalStepsMoved = (max(data)-start_val) + (max(data)-min(data)) 
print(totalStepsMoved)

fig, ax = plt.subplots()
ax.plot(mainSeq, y)
ax.axes.yaxis.set_visible(False)
ax.xaxis.tick_top()
for i in range(len(mainSeq)):
    ax.text(mainSeq[i], y[i], mainSeq[i])

plt.title("Disk-scheduling algorithm->Look\n")
plt.xticks(np.arange(0, end_track+1, 10))
plt.show()


# data.append(90)
# data.append(22)
# data.append(78)
# data.append(45)
# data.append(64)
# data.append(42)
# data.append(31)
# data.append(12)
# data.append(5)
# data.append(3)
# data.append(69)
# data.append(50)