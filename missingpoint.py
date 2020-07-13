from collections import defaultdict
t=int(input())

for _ in range(t):
	n=int(input())
	x=defaultdict(lambda:0)
	y=defaultdict(lambda:0)
	for i in range(4*n-1):
		a,b=map(int,input().split())
		x[a]+=1
		y[b]+=1
	X=-1
	Y=-1
	for i in x:
		if(x[i]&1==1):
			X=i
	for i in y:
		if(y[i]&1==1):
			Y=i
	print(X,Y)