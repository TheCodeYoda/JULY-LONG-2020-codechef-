t=int(input())

for _ in range(t):
	n=int(input())
	chef=0
	morty=0
	for i in range(n):
		a,b=input().split()
		su1=0
		su2=0
		n1=len(a)
		n2=len(b)
		for i in range(n1):
			su1+=int(a[i])
		for i in range(n2):
			su2+=int(b[i])
		if(su1>su2):
			chef+=1
		elif(su2>su1):
			morty+=1
		else:
			chef+=1
			morty+=1
	if(chef>morty):
		print(0,chef)
	elif(morty>chef):
		print(1,morty)
	else:
		print(2,chef)