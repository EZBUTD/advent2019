# --- Day 2: 1202 Program Alarm ---
# instructions: https://adventofcode.com/2019/day/2
import os
import sys

f=open(os.path.join(sys.path[0],"input.txt"),"r")
data=f.read().split(",")
f.close()

data=[int(i) for i in data]



def alarm(data:list,input1:int,input2:int):
    data[1]=input1
    data[2]=input2
    i=0
    while i < len(data):
        if data[i]==1:
            data[data[i+3]]=data[data[i+1]]+data[data[i+2]]
        elif data[i]==2:
            data[data[i+3]]=data[data[i+1]]*data[data[i+2]]
        elif data[i]==99:
            break
        i+=4
    return(data[0])

for i in range(99):
    for j in range(99):
        passinglist=data[:]
        output=alarm(passinglist,i,j)
        if output==19690720:
            print("i,j",i,j)
            quit()
