#Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
#For numbers that are multiples of both three and five print “FizzBuzz

def fizzbuzz():
	global n 
	n = 1
	while n < 101: 
	   #If n is divisible by 3 AND 5 with no remainders, print FizzBuzz
		if((n%3==0) and (n%5==0)):
			print("FizzBuzz")
		#If n is divisible by 3 with no remainders, print Fizz
		elif(n%3==0):
			print("Fizz")
		#If n is divisible by 5 with no remainders, print Buzz 
		elif(n%5==0):
			print("Buzz")
		#If none of the above requirements are met, print the integer value of variable n 
		else:
			print(n)
		n += 1 

fizzbuzz()