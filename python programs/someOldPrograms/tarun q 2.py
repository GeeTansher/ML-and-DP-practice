n = int(input("Enter a number :"))
print("The prime factors of your number:-")
i = 1
a =0
while i < n+1:
	if n%i == 0:
		for j in range(2, i):
			a =0
			if i%j ==0:
				a+=1
	if a ==0:
		'print("\t", i)
	i+=1