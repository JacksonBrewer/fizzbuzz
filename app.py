#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz

def fizzbuzz():
	global n 
	n = 1
	while n < 101: 
	
		if((n%3==0) and (n%5==0)):
			print("FizzBuzz")

		elif(n%3==0):
			print("Fizz")

		else:
			print(n)
		n += 1 

fizzbuzz()