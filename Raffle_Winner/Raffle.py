
_author__ = "Hassan Pasha"
__copyright__ = "Copyright 2017"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ ="Modern Wall Art"
__email__ = "(Enter Email)"
__status__ = "Non-Commercial Use"

# Using random and name lib to use the built in function 
import random 	
import names 
import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
import re
from bs4 import BeautifulSoup
import urllib
import urllib.request
import csv
import time
import sqlite3
#import datetime
from datetime import datetime
from collections import OrderedDict
'''
 How to use : Take names and insert into a given list -> example ['Hassan', 'Pasha', etc]
 than call function with list in FunctionName(list)
 -----
 Run code using Python Interperter , CMD , or an IDE

'''

#<a class="_4zhc5 notranslate _iqaka" title="icymidarling" href="/icymidarling/">icymidarling</a>
#<li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="icymidarling" href="/icymidarling/">icymidarling</a><span><!-- react-text: 55 -->Damn sick pic lil pp<!-- /react-text --></span></li>
#<ul class="_mo9iw _123ym"><li class="_nk46a"><h1><a class="_4zhc5 notranslate _iqaka" title="pashabrb" href="/pashabrb/">pashabrb</a><span><!-- react-text: 38 -->"If the Earth is this beautiful how will Janna be " <!-- /react-text --><a href="/explore/tags/nature/">#nature</a><!-- react-text: 40 --> <!-- /react-text --><a href="/explore/tags/exploring/">#exploring</a><!-- react-text: 42 --> <!-- /react-text --><a href="/explore/tags/oftrack/">#ofTrack</a><!-- react-text: 44 --> <!-- /react-text --><a href="/explore/tags/paki2016/">#paki2016</a></span></h1></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="ikhan_photography" href="/ikhan_photography/">ikhan_photography</a><span><!-- react-text: 50 -->you tryna be SRK or something<!-- /react-text --></span></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="icymidarling" href="/icymidarling/">icymidarling</a><span><!-- react-text: 55 -->Damn sick pic lil pp<!-- /react-text --></span></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="mohammedude" href="/mohammedude/">mohammedude</a><span><!-- react-text: 60 -->Lil pp lmaoo 😂 😂.<!-- /react-text --></span></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="ashah203" href="/ashah203/">ashah203</a><span><!-- react-text: 65 -->Daaang Pasha<!-- /react-text --></span></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="duduuuuuuuuuuuuuuuuu" href="/duduuuuuuuuuuuuuuuuu/">duduuuuuuuuuuuuuuuuu</a><span><!-- react-text: 70 -->😊😄<!-- /react-text --></span></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="pashabrb" href="/pashabrb/">pashabrb</a><span><a class="notranslate" href="/ikhan_photography/">@ikhan_photography</a><!-- react-text: 76 --> SRK trying to be me fam<!-- /react-text --></span></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="pashabrb" href="/pashabrb/">pashabrb</a><span><a class="notranslate" href="/icymidarling/">@icymidarling</a><!-- react-text: 82 --> 😐😐😐😐😐😐 <!-- /react-text --><a class="notranslate" href="/mohammedude/">@mohammedude</a></span></li><li class="_nk46a"><button class="_4vltl" title="Delete Comment">Delete Comment</button><a class="_4zhc5 notranslate _iqaka" title="pashabrb" href="/pashabrb/">pashabrb</a><span><a class="notranslate" href="/ashah203/">@ashah203</a><!-- react-text: 89 --> dang Ali<!-- /react-text --></span></li></ul>


def scrapping(Holder=[]):
	

		#url = "https://www.instagram.com/p/BJgktASjGya/?taken-by=pashabrb&hl=en"
		#url = "https://www.instagram.com/p/BQoHh2nl4wq/?taken-by=modernwallart&hl=en"
		url = "https://www.instagram.com/p/BQVkFI7jJc9/?hl=en"


		HTML = urllib.request.urlopen(url)
		soup = BeautifulSoup(HTML,"html.parser")

		try:
			for x in soup.findAll('a', attrs= {"class": "_4zhc5 notranslate _iqaka"}):
				for y in x :
					soup.findAll("href")
					
					Holder.append(y)


			#print(Holder)
			return Holder	
		except:
			print("ERROR SCAPPING NAMES")




def LuckyWinnerSelector(Holder = []):


	# this loop will just come up with 50,000 random names with and put into the list
	# If you already have a list with given names please comment this out below, which will increase run time
	# this is just testing the space that it can hold 

	# for x in range (0,50000):
		
	# 	name = names.get_first_name()

	# 	Holder.append(name)


	# This will shuffle the list 
	random.shuffle(Holder)

	# This random function below will only select one winner 

	# LuckyWinner = random.choice(Holder)
	# print(LuckyWinner)

	#This Function below lets you select more than one winner 

	LuckyWinner2 = random.sample(Holder,1)

	print("The lucky Winner is :" , LuckyWinner2) 
	return Holder   
#	print(LuckyWinner2)
		

# main function
if __name__ == '__main__':

	print("Welcome")

	#generating list 
	list1 = []
	#passing the the list to the given function
	#LuckyWinnerSelector(list1)
	scrapping(list1)
	print(list1)
	print(len(list1))
	LuckyWinnerSelector(list1)
	#print(len(list1))
	list1 = list(set(list1))
	#print(list1)

	exit = input("Press Enter to exit")


