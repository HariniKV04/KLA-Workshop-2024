import re
from math import sin,cos,radians,sqrt
f = open("D:\KLA-Workshop-2024-1\Input\Workshop2024\Milestone2\Input\Testcase3.txt", "r")

input=f.readlines()

wafer={}

wafer["WaferDiameter"]=int(re.findall('[-+]?\d+', input[0])[0])

temp = re.findall('[-+]?\d+', input[1])
wafer["DieSize"]=list(map(int, temp))

temp = re.findall('[-+]?\d+', input[2])
wafer["DieShiftVector"]=list(map(int, temp))

temp = re.findall('[-+]?\d+', input[3])
wafer["ReferenceDie"]=list(map(int, temp))


DieL=wafer["DieSize"][0]
DieH=wafer["DieSize"][1]

l=DieL
h=DieH

xshift=wafer["DieShiftVector"][0]
yshift=wafer["DieShiftVector"][1]


print(xshift)
print(yshift)

limitl=wafer["ReferenceDie"][0]-wafer["DieSize"][0]//2
limith=wafer["ReferenceDie"][1]-wafer["DieSize"][1]//2



print(limitl,limith)

def distanceCheck(x,y):
    return sqrt(x*x+y*y)<wafer["WaferDiameter"]/2
referenceDie=(0,0)

resultantPoints=[]
c=c1=c2=c3=c4=0
l=-wafer["WaferDiameter"]//2-xshift
while(l<=wafer["WaferDiameter"]//2-DieL-xshift):
    h=-wafer["WaferDiameter"]//2-yshift
    while(h<=wafer["WaferDiameter"]//2-DieH-yshift):
        print(l,h)
        if distanceCheck(l,h):
            c+=1
            resultantPoints.append("(%d,%d):(%.4f,%.4f)"%((l-limitl)//DieL,(h-limith)//DieH,l,h))
        else:
            if l<0 and h<0:
                if distanceCheck(l+DieL,h+DieH) or distanceCheck(l+DieL,h) or distanceCheck(l,h+DieH):
                    c1+=1
                    resultantPoints.append("(%d,%d):(%.4f,%.4f)"%((l-limitl)//DieL,(h-limith)//DieH,l,h))
            elif l<0 and h>0:
                if distanceCheck(l+DieL,h):
                    c2+=1
                    resultantPoints.append("(%d,%d):(%.4f,%.4f)"%((l-limitl)//DieL,(h-limith)//DieH,l,h))
            elif l>0 and h<0:
                if distanceCheck(l,h+DieH):
                    c3+=1
                    resultantPoints.append("(%d,%d):(%.4f,%.4f)"%((l-limitl)//DieL,(h-limith)//DieH,l,h))

        h+=DieH
    l+=DieL
print(c,c1,c2,c3,c4)

# print(len(resultantPoints))


with open('output23.txt', 'w') as f:
    for result in resultantPoints:
        f.write(result)
        f.write("\n")
    