def CheckNumber(InputString):
	
	List = list(InputString)


	checkingList = ["1","2","3","4","5","6","7","8","9","0"]
	newList = [] 
	for x in List:
		for y in checkingList:
			if(x == y):
				newList.append(x)
				
	newList.sort()
	print(newList)

					
	 
			
	

def ChecknumberR(InputString,subtracter):
	x = list(InputString)

	if(subtracter == len(x)):
			return
	
	if(x[subtracter-len(x)].isdigit()):
		z = (x[subtracter-len(x)])
		print(z)
		
	
	ChecknumberR(InputString,(subtracter + 1))
		

ChecknumberR("123fahhikadjfka[2384hhn7",0)

