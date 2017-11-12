import re


def palindrome(StringInput):
	correct = []
	wrong = []
	
	correctint = 0
	wrongint = 0
	for inputs in StringInput:
		

		# The code below will turn the sting to all lower for better accuracy 
		UserInput = inputs.lower().strip(" ")

		
	
		# list that will hold the backWord word to compare with
		backWord = [] 


		# usrinput into a list 
		normalWord = list(UserInput.strip(" "))

		# counter to iterate through the list
		counter = len(normalWord) 
		
		print(normalWord)
		while( counter  > 0) : 

			backWord.append(normalWord[counter-1])
			counter = counter - 1 


		if(normalWord == backWord):
			correct.append(UserInput)
			correctint = correctint + 1 
			print("True")
		else :
			wrong.append(UserInput)
			wrongint = wrongint + 1 
			print("False")


	print("The correct List ",correct)
	print(correctint)

	print("The Wrong List",wrong)
	print(wrongint)




#This is the userinterphase basic interpahse to give the user a more indivisual feel
def FrontEnd():
	
	Holder = []

	user = input("Welcome, Who do I have the oppurtuinty of speaking to\n")
	print("Nice to meet you",user)

	inputIntake = input("Pleae Enter list of words you would like to check,press q to stop Press enter to start")

	

	while(inputIntake != "q"):

		inputIntake = input(" ")
		if(inputIntake != "q"):
			Holder.append(inputIntake)

	
	return Holder


#calling the function which takes the second functions as an argument
palindrome(FrontEnd())
