import re
from bs4 import BeautifulSoup
import requests
import urllib.request 
import time 
import sqlite3
from datetime import datetime
from collections import OrderedDict
from urllib.request import urlopen
import ssl # this is to bypass the certi issue 
import ast
import os
from tkinter import *
import sys 
import PyQt5 
#packages needed above 



#Urls that are being used 
Url = "ENTER URL"


#------- Data structures -------------------#

Links = [Url] # Keeping this just in case in the futre that we might need more links to scrape 
Data = []   # Where all the Data will be stored 
TypeCasting = [] #just in case we need to TypeCast 


#----------END DSTRA -------------------------#


DB = sqlite3.connect('DB_NAME.db')
cursor = DB.cursor()
#----------- Creating Database --------------#

def CreateDB():
	global DB
	global cursor
	#try statment is added becuase we do not want the table to be recreated if already made 
	try:
		#creating table 
		cursor.execute('''CREATE TABLE Products( Name TEXT , BidNum REAL, ListingNum REAL ,END_Date REAL, Current_Bid REAL , Time REAL, Date REAL, Day TEXT) ''')
		#commit the query 
		DB.commit()
	except:

		print("Table has already been made")
		

#--------------- DB done --------------------#

def Scraper():
	#global varibales 
	global Links
	global Data
    
	
	#creating temp table to hold and manipulate data
	temp = []
	
	
	#requesting website
	page = urllib.request.urlopen(Links[0])
	soup = BeautifulSoup(page,"html.parser")

	#finding all the desired data boxes
	Table = soup.find_all("div",attrs = {"class":"box col-md-4 col-sm-6 col-ms-6 col-xs-12"})
	
	#assigning Table to temp table < not needed just for my ease >
	temp = Table

	# removing all the unwanted tags and info 
	for y in temp:
		x = y.text.strip()
		Data.append(x)
		
	
	#checing the len of data set to see if the correct number of info is coming in
	#print(len(Data))

	#cleaning data to make it more readable 
	Data = [D.replace('Bid Now', '-----END OF BOX---- \n') for D in Data]
	#returning the data list to be called when needed
	return Data


#------------Scraper done --------------#




#-----------Readable-------------------#

def Readable(Data):
	#printing the list out in a neat fashion

	print(*Data,sep=('\n'))

#--------------Readable End-----------#

#--------------GUI--------------------#
	


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel_1 (root)
    
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel_1 (w)
   
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None




#-------------GUI END- -----------------
class New_Toplevel_1:
    

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("900x360+-1102+229")
        top.title("Tyshopper")
        top.configure(background="#FF8C00")



        self.button1 = Button(top,command =self.buttonClick)
        self.button1.place(relx=0.41, rely=0.89, height=24, width=108)
        self.button1.configure(activebackground="#d9d9d9")
        self.button1.configure(activeforeground="#000000")
        self.button1.configure(background="#FFFFFF")
        self.button1.configure(disabledforeground="#a3a3a3")
        self.button1.configure(foreground="#000000")
        self.button1.configure(highlightbackground="#d9d9d9")
        self.button1.configure(highlightcolor="black")
        self.button1.configure(pady="0")
        self.button1.configure(text='''Enter''')
        self.button1.configure(width=108)
        

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.33, rely=0.78, relheight=0.06, relwidth=0.32)
        self.Entry1.configure(background="#FFD700")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=194)
        self.Entry1.configure(text= '''ENTERT DESIRED VALUE''')

        self.Listbox1 = Listbox(top)
        self.Listbox1.place(relx=0.1, rely=0.08, relheight=0.67, relwidth=0.81)
        self.Listbox1.configure(background="#FFA500")
        self.Listbox1.configure(disabledforeground="#a3a3a3")
        self.Listbox1.configure(font="TkFixedFont")
        self.Listbox1.configure(foreground="#000000")
        self.Listbox1.configure(width=494)
      #  list_ = ['one','two','three','four','five','six','seven'] 
      
      # # print(self.Entry1.get())
      #  for x in list_:
      #   self.Listbox1.insert(END,x)
#--------Organize The Data ----------#
    def buttonClick(self):
    	global DB
    	global cursor
    	Data = Scraper()
    	i = 0 	
    	WorthBuying = []
    	userinput = self.Entry1.get()
    	while(i < len(Data)):
    		temp = Data[i].split('\n')
    		print('\n')
    		#printing with the datastructure for testing
    		print(temp[0]) #name
    		print(int(temp[2].replace('Number Of Bids:',''))) #number of bids 
    		print(int(temp[3].replace('Listing #:',''))) #listing 
    		print(temp[5].replace('Auction Ends: ','')) #Auction Ending 		
    		print(float(temp[10].replace('Current Bid$','')))#current bid
			#Sucess so now assigning variables to manipulate data
    		name = temp[0]
    		Bids = int(temp[2].replace('Number Of Bids:',''))
    		ListingNum = int(temp[3].replace('Listing #:',''))
    		AuctionEnding = temp[5].replace('Auction Ends: ','')
    		CurrentB = float(temp[10].replace('Current Bid$',''))


    			#------Data_Logic ----# 

			
			 #The logic that we want to take is that if the bid number is less than or eqal to 700 show us the list of products that are worth buying
			 #700 > Listing 


    		if (CurrentB <= int(userinput)):
    			WorthBuying.append(name)
    			WorthBuying.append(str(ListingNum))
    			WorthBuying.append(AuctionEnding)

    			#------Logic ---------#



			#trying to insert into the database 

    			try:
    				cursor.execute('''INSERT INTO Products (Name,BidNum,ListingNum,END_Date,Current_Bid,Time,Date,Day)VALUES(?,?,?,?,?,?,?,?)''',
		                               (temp[0],int(temp[2].replace('Number Of Bids:','')),int(temp[3].replace('Listing #:','')),temp[5].replace('Auction Ends: ',''),float(temp[10].replace('Current Bid$','')),datetime.now().strftime("%H:%M:%S"),time.strftime("%x"),
		                                datetime.now().strftime("%A")))
    				DB.commit()
    				print("SUCESS")
    			except:
    				print("Error INSERTing into DB")
    			i = i + 1



    	def Clean_Up(List_Cleanup):
    		temp = [] 
    		y = 0 
    		while(1):
    			if(y > len(List_Cleanup)):
    				break
    			else:
    				try: 
    					Final = List_Cleanup[y]+" " + List_Cleanup[y+1]+ " " +" " +List_Cleanup[y+2]
    				except:
    					break
    				temp.append(Final)
    				y = y + 3
    		return temp
    	WorthBuying = Clean_Up(WorthBuying)

    	for x in WorthBuying:
    		self.Listbox1.insert(END,x)



	


#--------END------------------------#



if __name__ == '__main__':
    vp_start_gui()
