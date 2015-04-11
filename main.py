#######################################
#                                     #
#  https://github.com/pedroguima      #
#                                     #
#######################################

from prime_functions import *

def header():
	print "\n## Fun with primes v0.1 ##\n"

def print_list(option, max_prime):
	counter=3

	if(option==1):
		while(counter<=max_prime):
			if(is_prime(counter)==1):
				print counter,
			counter+=1
	elif(option==2):
		while(counter<=max_prime):
			if((is_prime(counter)==1) and (is_palindromic(counter)==1)):
				print counter,
			counter+=1

def main_menu():
	header()
	while 1:
		print "\nWhat would you like to do today?"
		print "1- Get a list of Primes"
		print "2- Get a list of Palindromic Primes" 
	        try:
			option=int(input("\nPlease select an option: "))
	        except (NameError, ValueError, SyntaxError):
        	        error("Please enter a valid option.")
			continue
		else:
			if (option<1 or option>2):
				error("Please enter a valid option.")
				continue
		break

	while 1:
		try:
			max_prime=int(input("\nPlease enter the upper limit value: "))
		except (NameError, ValueError, SyntaxError):
		        error("Please enter a valid natural number.")
			continue
		else:
			if (max_prime<2):
				error("Number must be equal or greater than 2")
				continue
		break
	print_list(option, max_prime)

main_menu()
