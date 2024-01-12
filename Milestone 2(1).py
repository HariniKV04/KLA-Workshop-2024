import re
from math import sin,cos,radians,sqrt
f = open("D:\KLA-Workshop-2024-1\Input\Workshop2024\Milestone2\Input\Testcase1.txt", "r")

input=f.readlines()

wafer={}

wafer["WaferDiameter"]=int(re.findall(r'\d+', input[0])[0])

temp = re.findall(r'\d+', input[1])
wafer["DieSize"]=list(map(int, temp))

temp = re.findall(r'\d+', input[2])
wafer["DieShiftVector"]=list(map(int, temp))

temp = re.findall(r'\d+', input[3])
wafer["ReferenceDie"]=list(map(int, temp))


DieL=wafer["DieSize"][0]
DieH=wafer["DieSize"][1]

l=30
h=30

def distanceCheck(x,y):
    return sqrt(x*x+y*y)<wafer["WaferDiameter"]/2
referenceDie=(0,0)

resultantPoints=[]
c=c1=c2=c3=c4=0
l=-wafer["WaferDiameter"]//2
while(l<=wafer["WaferDiameter"]//2-DieL):
    h=-wafer["WaferDiameter"]//2
    while(h<=wafer["WaferDiameter"]//2-DieL):
        if l>0 and h>0 and not distanceCheck(l,h):
            print(l,h)
        if distanceCheck(l,h):
            if l>=0 and h>=0:
                c1+=1
            elif l<0 and h>=0:
                c2+=1
            elif l<0 and h<0:
                c3+=1
            else:
                c4+=1
            resultantPoints.append("(%d,%d):(%.4f,%.4f)"%(l//DieL,h//DieH,l,h))
        else:
            if l<0 and h<0:
                if distanceCheck(l+DieL,h+DieH) :
                    if l>=0 and h>=0:
                        c1+=1
                    elif l<0 and h>=0:
                        c2+=1
                    elif l<0 and h<0:
                        c3+=1
                    else:
                        c4+=1
                    resultantPoints.append("(%d,%d):(%.4f,%.4f)"%(l//DieL,h//DieH,l,h))
            elif l<0 and h>0:
                if distanceCheck(l+DieL,h):
                    if l>=0 and h>=0:
                        c1+=1
                    elif l<0 and h>=0:
                        c2+=1
                    elif l<0 and h<0:
                        c3+=1
                    else:
                        c4+=1
                    resultantPoints.append("(%d,%d):(%.4f,%.4f)"%(l//DieL,h//DieH,l,h))
            elif l>0 and h<0:
                if distanceCheck(l,h+DieH):
                    if l>=0 and h>=0:
                        c1+=1
                    elif l<0 and h>=0:
                        c2+=1
                    elif l<0 and h<0:
                        c3+=1
                    else:
                        c4+=1
                    resultantPoints.append("(%d,%d):(%.4f,%.4f)"%(l//DieL,h//DieH,l,h))
        h+=DieH
    l+=DieL

if l>=0 and h>=0:
    c1+=1
elif l<0 and h>=0:
    c2+=1
elif l<0 and h<0:
    c3+=1
else:
    c4+=1
print(c,c1,c2,c3,c4)

print(len(resultantPoints))


with open('output21.txt', 'w') as f:
    for result in resultantPoints:
        f.write(result)
        f.write("\n")
    