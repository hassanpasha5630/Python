
_author__ = "Hassan Pasha"
__copyright__ = "Copyright 2007"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ ="Modern Wall Art"
__email__ = "(Enter Email)"
__status__ = "Non-Commercial Use"

# Using random and name lib to use the built in function 
import random 	
import names 

'''
 How to use : Take names and insert into a given list -> example ['Hassan', 'Pasha', etc]
 than call function with list in FunctionName(list)
 -----
 Run code using Python Interperter , CMD , or an IDE

'''


def LuckyWinnerSelector(Holder = []):


	# this loop will just come up with 50,000 random names with and put into the list
	# If you already have a list with given names please comment this out below, which will increase run time
	# this is just testing the space that it can hold 

	for x in range (0,50000):
		
		name = names.get_first_name()

		Holder.append(name)


	# This will shuffle the list 
	random.shuffle(Holder)

	# This random function below will only select one winner 

	# LuckyWinner = random.choice(Holder)
	# print(LuckyWinner)

	#This Function below lets you select more than one winner 

	LuckyWinner2 = random.sample(Holder,1)
	print(LuckyWinner2)
		

# main function
if __name__ == '__main__':

	print("Welcome")

	#generating list 
	list1 = []
	#passing the the list to the given function
	LuckyWinnerSelector(list1)

