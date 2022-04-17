def isPrime(x):
	x=int(x)
	for i in range(2,x):
		if x%i==0:
			return False
	return True

list1=[]
list2=[]

for i in range(500,5000):
	if isPrime(i):
		list1.append(i)

for i in list1:
	for j in range(0,i):
		if i==2*j+1:
			list2.append(i)
print(list2)
