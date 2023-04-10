n = int(input("enter:"))
i =1
j=2
c =-1
prime = [ ]
noprime=[]
while i<n+1:
	if n%i ==0:
		c+=1
		prime.append(i)
	i+=1

for k in range(0, c):
	while j<prime[k]:
		if prime[k]%j==0:
			noprime.append(prime[k])
		
		j+=1
	
for g in range(0, c):
	prime.remove(noprime[g])
for f in range(0, c):
	print(prime[c])
		