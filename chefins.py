from collections import defaultdict
t=int(input())

for _ in range(t):
	n=int(input())
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	da=defaultdict(lambda:0)
	db=defaultdict(lambda:0)
	s=list(set(a+b))
	for i in range(n):
		da[a[i]]+=1
		da[b[i]]+=0
		db[b[i]]+=1
		db[a[i]]+=0
	flag=1
	for i in s:
		if((da[i]+db[i])&1==1):
			print(-1)
			flag=0
			break
	if(flag):
		i=0
		j=0
		a.sort()
		b.sort(reverse=True)
		#print(a)
		#print(b)
		mi=min(s)
		cost=0
		while(i<n and j<n):
			while(i<n and (da[a[i]]<=db[a[i]])):
				i+=1
			while(j<n and (db[b[j]]<=da[b[j]])):
				j+=1
			#print(i,j)
			if((i<n and j<n) and (a[i]!=b[j])):
				c1=mi*2
				c2=min(a[i],b[j])
				if(c2<=c1):
					#a[i],b[j]=b[j],a[i]
					da[a[i]]-=1
					db[a[i]]+=1
					db[b[j]]-=1
					da[b[j]]+=1
					cost+=c2
				else:
					da[a[i]]-=1
					db[a[i]]+=1
					db[b[j]]-=1
					da[b[j]]+=1
					cost+=c1
				#print(da)
				#print(db)
				#print("cost: ",cost)
				i+=1
				j+=1
			else:
				i+=1
				j+=1
		print(cost)