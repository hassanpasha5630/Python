
#--------------------------------------------------------------------------------------------------------
# I have used a recursive function for efficiency, it takes any input x and return the sum of its multiple
#-------------------------------------------------------------------------------------------------------
import sys


def multiple(x,value,counter):
	sys.setrecursionlimit(10000)
	if(counter >= 999):
		return value
		
	else:
		if( counter % x == 0 ):
			value = value + counter 
		counter = counter + 1 
		return multiple(x,value,counter)


def main():
	five = multiple(5,0,0)
	print("sum of multiple of 5 : ",five)
	seven = multiple(7,0,0)
	print("sum of multiple of 7 : ",seven)
	eleven = multiple(7,0,0)
	print("sum of multiple of 11 : ",eleven)

main()