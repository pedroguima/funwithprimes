def error(msg):
	print "\nError: ",msg


def is_palindromic(value):
	val_str=str(value)
	val_str_rev=val_str[::-1]
	if (val_str==val_str_rev):
		return 1
	return 0

def is_prime(value):
	i=value-1
	
	if(value==2):
		return 1

	while(i<value):
		if(i==1):
			return 1
		if (value%i == 0):
			return 0
		i-=1


while 1:
	try:
		max_prime=int(input("Please enter the upper limit value: "))
	except (NameError, ValueError):
		error("Please enter a valid natural number.")
		continue
	else:
		if (max_prime<2):
			error("Number must be greater or equal to 2")
			continue
	break


counter=2
while(counter<=max_prime):
	if((is_prime(counter)==1) and (is_palindromic(counter)==1)):
		print counter, 
	counter+=1

