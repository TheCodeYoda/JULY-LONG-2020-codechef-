t=int(input())
for _ in range(t):
	n,x=map(int,input().split())
	a=list(map(int,input().split()))
	a.sort()
	dp=[0 for i in range(n)]
	c=1
	t=x
	while(a[0]>t):
		t*=2
		c+=1
	dp[0]=c
	rem=0
	temp1=t
	c2=c
	for i in range(1,n):
		c1=1
		temp=a[i-1]*2
		while(a[i]>temp):
			temp*=2
			c1+=1
		while(a[i]>temp1):
			temp1*=2
			c2+=1
		dp[i]=min(dp[i-1]+c1,c2)
		if(c2<c1+dp[i-1]):
			rem+=1
	print(dp[n-1]+rem)