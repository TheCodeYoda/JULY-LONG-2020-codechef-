t=int(input())

for _ in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	su=0
	for i in range(n-1):
		su+=abs(a[i]-a[i+1])-1
	print(su)