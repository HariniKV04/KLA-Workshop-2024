import re
from math import sin,cos,radians
f = open("D:\KLA-Workshop-2024-1\Input\Workshop2024\Milestone1\Input\Testcase4.txt", "r")

input=f.readlines()

wafer={"WaferDiameter":0,"NumberOfPoints":0,"Angle":0}

for i in range(len(input)):
    wafer[list(wafer)[i]]=int(re.findall(r'\d+', input[i])[0])

equiDistance=wafer['WaferDiameter']/(wafer[ 'NumberOfPoints']-1)

print(wafer)
print(equiDistance)

resultantPoints=[]
theta=radians(wafer["Angle"])

radii=[]

r=-wafer["WaferDiameter"]//2
while(r<=wafer["WaferDiameter"]//2+0.0000001):
    radii.append(r)
    r+=equiDistance
    

resultantPoints=[]

for r in radii:
    resultantPoints.append("(%f,%f)"%(r*cos(theta),r*sin(theta)))


#print(resultantPoints)



with open('output4.txt', 'w') as f:
    for result in resultantPoints:
        f.write(result)
        f.write("\n")
    



