# Exercise 3 Template

# Do not modify the file name or function header

# Retuns a list with the prime numbers in the [a, b] interval
def prime(a, b):
	# Your code here
	primes = []
	primo = 1
	for i in range (a, b):
		primo = 1
		for j in range (2, i-1):
			if i%j==0:
				primo = 0
				break
		if primo == 1:
			primes.append(i)
	# ...

	return primes
