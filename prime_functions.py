#######################################
#                                     #
#  https://github.com/pedroguima      #
#                                     #
#######################################

def error(msg):
	print "\nError: ",msg


def is_palindromic(value):
	val_str=str(value)
	val_str_rev=val_str[::-1]
	if (val_str==val_str_rev):
		return 1
	return 0


## naive way
## To do: https://en.wikipedia.org/wiki/Primality_test#Python_implementation
def is_prime(value):
	i=value-1
	
	if(value==2 or value==3):
		return 1

	while(i<value):
		if(i==1):
			return 1
		if (value%i == 0):
			return 0
		i-=1

