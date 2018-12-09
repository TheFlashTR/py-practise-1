# -*- coding: utf-8 -*-
import feedparser
import getpass
import requests

accounts = []

def register():
	print("Register")
	username = input("Username: ")
	if username in accounts:
		print(username,"already registered")
		accounts.append(username)
	else:
		passwd =  getpass.getpass("Pass: ")
		accounts.append(passwd)
		return accounts
		
def login():
	username = input("Username: ")
	passwd =  getpass.getpass("Pass: ")
	#getpass hides pass.
	if (username and passwd in accounts):
	    menu()
	else:
		print("Wrong Credentials")

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
		weather = requests.get('https://wttr.in/{}'.format(city+'?lang=en'), headers={'user agent' : 'curl'})
		print(weather.text)
		
	elif (operation == '3'):
		print("1 Turkish Liras.")
		currency = requests.get('https://api.exchangeratesapi.io/latest?base=TRY', headers={'user agent' : 'curl'})
		print(currency.text)
	else:
	    print("Wrong")

while True:
	print("""**********\nFl1sh's Panel\n1-Login\n2-Register\n**********\n""")
	stat = input("Select:")
	if (stat == '1'):
		login()
	if (stat == '2'):
		register()
	else:
		print("Wrong Credentials")
