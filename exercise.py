# -*- coding: utf-8 -*-
import feedparser
import getpass
import requests


sys_user = "root"

sys_pass  = "fl1sh"

def login():
	username = input("Username: ")
	passwd =  getpass.getpass("Pass: ")
	#getpass hides pass.
	if (username != sys_user and passwd == sys_pass):
		print("Wrong Username...")
	elif (username == sys_user and passwd!= sys_pass):
		print("Wrong Password...")
	elif (username != sys_user and passwd != sys_pass):
		print("Wrong Username and Password...")
	else:
		menu()

def logout():
    print("Log outed...")
    return
		
def menu():
	print("**********\nMenu\n1-News\n2-Weather\n3-Currency\nq-Exit\n**********\n")
	operation = input("Select : ")
	if (operation == '1'):
	  haber = feedparser.parse('https://www.cnnturk.com/feed/rss/all/news')
	  for post in haber.entries:
	  	print(post.title)
	elif (operation == 'q'):
		logout()
	elif (operation == '2'):
		city = input('Pls Enter City Name: ')
		weather = requests.get('https://wttr.in/{}'.format(city+'?lang=tr'), headers={'user agent' : 'curl'})
		print(weather.text)
		
	elif (operation == '3'):
		print("1 Turkish Liras.")
		currency = requests.get('https://api.exchangeratesapi.io/latest?base=TRY', headers={'user agent' : 'curl'})
		print(currency.text)
	else:
	    print("Wrong")

print("**********\nLogin Panel\n**********\n")

while True:
	login()
