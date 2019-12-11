# --- Day 2: 1202 Program Alarm ---
# instructions: https://adventofcode.com/2019/day/2
import os
import sys

f=open(os.path.join(sys.path[0],"input.txt"),"r")
data=f.read().split(",")
f.close()

data=[int(i) for i in data]

data[1]=12
data[2]=2 #following instructions to replace these values


i=0
while i < len(data):
    if data[i]==1:
        data[data[i+3]]=data[data[i+1]]+data[data[i+2]]
    elif data[i]==2:
        data[data[i+3]]=data[data[i+1]]*data[data[i+2]]
    elif data[i]==99:
        break
    i+=4
print(data)
print(data[0])
