#Problem 1 
#-----------------------------------------------------------------------------------------------------------
# The formula to find P is as follows assuming your goal is to make sure there are no losses so Profit can be = 0 .
# 	P = (C/1-F) If the number is a whole value example (18)
# 	if number has leading decimal values we would want to round up as a safety net to ensure no loss occurs.
# 	P = (C/1-F) --> Rounded up
# 	If you want to figure out what P would be to gain some Profit(Z) it will be as follows
# 	P = ((C+Z)/(1-F))
#----------------------------------------------------------------------------------------------------------

# Take User input for C and F 
import math

#---------- Proof of concpet  and ERROR CHECKING-------------------------------------------------------------
# print("Welcome to Problem one please enter C as '10' and F as '.10 ")

# C = int(input("Enter C: "))
# F = float(input("Enter F: "))

# print("C is : " , C)
# print("F is : " , F)


# P = math.ceil((C/(1-F)))

# print( "P is : ",P)
#---------------------------------------------------------------------------------------------------------

# To make this run place the input textfile 

def Product_Sale_Price():
	temp = []
	file =[]
	C = []
	F = []
	P = []
	counter = 0
	userinput = input("ENTER the file as follows product_costs.txt:  ")
	#userinput = "'"+ userinput +"'"
	try:
		print("Reading file sucessful")
		input_file =  open(userinput,"r") 
		for x in input_file:
			file.append(x.split(" "))

		for x in file:
			C.append(int(x[0]))
			F.append(float(x[1]))

		while(counter < len(file)):
			
			#print(counter,"C is : ",C[counter]," ", "F is :", F[counter])
			P.append(math.ceil((C[counter]/(1-F[counter]))))
			counter = counter + 1 

		#---------------------------checking to see if list populated properly------------------------------
		y = 0 
		for x in P :
			print("P", y,":",x)
			print('\n')
			y = y +1 
		#--------------------------------------------------------------------------------------------------
		#checking the list 
		#print(P)
		#print(len(file))
	except:
		print(userinput)
		print("ERROR Reading file please TRY AGAIN: ")
		#Recurssively calling the function again
		Product_Sale_Price()


if __name__ =="__main__":
	Product_Sale_Price()