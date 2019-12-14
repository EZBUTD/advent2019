#prompt https://adventofcode.com/2019/day/12
#Need to find position, velocity, kinetic energy, potential energy, total energy in system
#kinetic energy=abs(velocity)
#potential energy=abs(position)
#total=kinetic*potential

#beginning positions
# <x=3, y=-6, z=6>
# <x=10, y=7, z=-9>
# <x=-3, y=-7, z=9>
# <x=-8, y=0, z=4>

#find an efficient way to determine the day when moons return to exact same position as before.
#x,y,z axis don't influence each other
#First see if I can find how long it takes for each axis to cycle by brute force



#found individual axis cylce to be: x-268296 days, y-22958 days,z=231614 days
from math import gcd

l = [268296,22958,231614]
first=int(l[0]*l[1]/gcd(l[0],l[1]))
lcm=first*l[2]/gcd(first,l[2])
print(lcm)

##find cycle by axis, reuse code from part 1
# import numpy as np
# Orig_pos=np.array([[3,-6,6],[10,7,-9],[-3,-7,9],[-8,0,4]])
# Moon_pos=np.array([[3,-6,6],[10,7,-9],[-3,-7,9],[-8,0,4]])
#
# Moon_vel=np.zeros((4,3))

# for days in range(1,4368):
#     for x in range(4):
#
#         y_compare=Moon_pos[:,2]
#         for i in y_compare:
#             if Moon_pos[x][2]>i:
#                 Moon_vel[x][2]-=1
#             elif Moon_pos[x][2]<i:
#                 Moon_vel[x][2]+=1
#     Moon_pos=np.add(Moon_pos,Moon_vel)
#     if np.array_equal(Moon_pos[:,2],Orig_pos[:,2]):
#         print(Moon_pos)
#         print("days",days+1)
#         break

# kinetic=np.sum(abs(Moon_vel),axis=1)
# potential=np.sum(abs(Moon_pos),axis=1)
# total=np.multiply(kinetic,potential)
# print(np.sum(total))
