#Design and Develop an aggregator in python which aggregates news / articles on “diabetes" and converts the content to be published on the kitchry platform. 
#This data model will be used as a subscription service to the clients who are diabetic. 
#The deliverable should be a working prototype. Feel free to define constraints and #assumptions as you see fit. Coding required.


#----------------------------------------------------------------------------------------

# The code below will go to any news related website, cnn is a pre-added one you can always add more.
# It will than display the categories that are for the selected website. You can select one and it will 
# continue to give you all the articles referring to the category. you can filter it more with a desired 
# keyword as well which is commented out below. Please check that section of the code. It will 
# take the text and throw it on to a GUI for easy read. The GUI was referenced from the website that is 
# listed above that section of the code.


#----------------------------------------------------------------------------------------

import newspaper
from newspaper import Article
from bs4 import BeautifulSoup
import urllib.request 
import re
from tkinter import *

UrlList = ["http://www.cnn.com/"]
Cateogry = []
Stories = [] 
Desired_Stories = [] 

def languages():
 	newspaper.languages()


def userinterface():
	
	while 1:
		Userinput = input("CNN is a pre-added news source would you like to add more?, Enter Yes or No: ")
		if(Userinput == "Yes"):
			Userinput = input("Enter input as, 'www.cnn.com'")
			UrlList.append(Userinput)
		if(Userinput == "No"):
			return 


def Cat():
	print(UrlList)
	Userinput = int(input("select from the links to obtain the Category Enter 0-N : " ))
	
	if(Userinput  > len(UrlList)):
		print("try again Number does not exist")
		Cat()
	else:		
		Art = newspaper.build(UrlList[Userinput])
		print("Category are being appended to a list for future usage")
		for x in Art.category_urls():
			Cateogry.append(x)

def Article_():
	y = 0 
	print("Please select from the list below")
	for x in Cateogry:
		print(y,".",x)
		print('\n')
		y = y + 1 
	Userinput = int(input("Select Category to display articles 0 - N "))

	ScrapingURL = Cateogry[Userinput]

	
	try:
	#requesting website
		page = page = urllib.request.urlopen(ScrapingURL)
		soup = BeautifulSoup(page,"html.parser")
	except:
		print("URL ERROR")

	#Below finding all the hyper links assuming that we want to check out different articles 
	
	for link in soup.find_all('a', href = True):
		Stories.append(link["href"])

	# making sure that we only get the health related information 
	substring = "/health"
	#we want the articles hence the index not the sub category 
	substring2 = "/index.html"
	# temp holding all the cleaned links 
	Temp = []
	for x in Stories:
		if substring and substring2 in x :
			Temp.append(x)
	
	#clearing out the list for future usage
	Stories.clear()
	
	#Asuming that this is for generic news so we want to go back and add the new link to access the articles 
	Link = ScrapingURL
	Link = Link.split('/')
	Final_String = Link[0]+"//"+ Link[2]
	
	for x in Temp :
		Final = Final_String + x
		Stories.append(Final) 

	#clearing out the temp list 
	Temp.clear()

	# This should give us the list of articles about health related topics   
	y = 0 
	for z in Stories:
			print(y,".",z)
			print('\n')
			y = y + 1 

 #----------------------------------------------------------------------------------------------------------------------
	# check = "diabetes"
	# for x in Stories:
	# 	if check in x :
	# 		Temp.append(x)
	# y = 0 
	# for z in Temp:
	# 		print(y,".",z)
	# 		print('\n')
	# 		y = y + 1 
	# above is to find anything article for a given topic ex check = diabetes 
	# make this as a user input check = input("ENTER Topic")
#-----------------------------------------------------------------------------------------------------------------------	

def Article_Text():
	
	Userinput = int(input("Select article to read 0 - N "))
	Url = Stories[Userinput]
	
	Art = Article(Url)
	try:
		Art.download()
		Art.parse() 
	except:
		print("ERROR") 
	
	print("------------------GUI Opening ----------------------------")
	
	Text_Art = Art.text
	# referenced https://www.python-course.eu/tkinter_text_widget.php
	#--------------------------------------------------------------------
	root = Tk()
	S = Scrollbar(root)
	T = Text(root, height=100, width=300)
	S.pack(side=RIGHT, fill=Y)
	T.pack(side=LEFT, fill=Y)
	S.config(command=T.yview)
	T.config(yscrollcommand=S.set)
	T.insert(END, Text_Art)
	mainloop(  )
  #----------------------------------------------------------------------


def main():
	userinterface()
	Cat()
	Article_()
	Article_Text()
   	


	#print(Stories)


#using this like the main function in C 
main()

