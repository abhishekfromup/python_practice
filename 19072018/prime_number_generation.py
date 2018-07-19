# test.py
#import math
from math import sqrt

def primeNumberGenerator(limit):
	global total
	for i in range(2, limit):
		for j in range(2, int(sqrt(i))+1):
			if ((i % j) == 0):
			# print("%d is NOT prime number \n" %i)
				break
		else:
			print(i , "is prime number")
			total += 1


total = 0

def main():
	global total, limit
	total = 0
	limit = int(input("Please enter the limit till where you want to generate prime numbers: "))
	primeNumberGenerator(limit)
	print("Total prime numbers till ", limit, " are: " , total)

if (__name__ == "__main__"):
	main()
