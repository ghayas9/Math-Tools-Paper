import math
fil=open(f"abc.txt","w")
m=1.2
s=2
for x in range(-20,21): 
    a=1/((2*math.pi*x)**0.5)*math.exp(-1/2*((x-m)/s)**2)
    fil.writelines(f"{a} \n")

fil.close()
