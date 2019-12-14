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

import numpy as np

Moon_pos=np.array([[3,-6,6],[10,7,-9],[-3,-7,9],[-8,0,4]])
Moon_vel=np.zeros((4,3))

for z in range(1000):
    for x in range(4):
        for y in range(3):
            y_compare=Moon_pos[:,y]
            for i in y_compare:
                if Moon_pos[x][y]>i:
                    Moon_vel[x][y]-=1
                elif Moon_pos[x][y]<i:
                    Moon_vel[x][y]+=1
    Moon_pos=np.add(Moon_pos,Moon_vel)

print(Moon_vel)
kinetic=np.sum(abs(Moon_vel),axis=1)
potential=np.sum(abs(Moon_pos),axis=1)
total=np.multiply(kinetic,potential)
print(np.sum(total))
