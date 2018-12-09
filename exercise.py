# -*- coding: utf-8 -*-
import feedparser
import getpass
import requests

print("**********\nLogin Panel\n**********\n")

sys_user = "root"

sys_pass  = "1"

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
	print("**********\nMenu\n1-News\n2-Weather\n3-Currency\nq-Exit\n**********\n")
	islem = input("Select : ")
	if (islem == '1'):
	  haber = feedparser.parse('https://www.cnnturk.com/feed/rss/all/news')
	  for post in haber.entries:
	  	print(post.title)
	elif (islem == 'q'):
		print("Exited...")
	elif (islem == '2'):
		 = input('Pls Enter City Name: ')
    weather = requests.get('https://wttr.in/{}'.format(city+'?lang=tr'), headers={'user agent' : 'curl'})
		print(weather.text)
		
	elif (islem == '3'):
		print("1 Turkish Liras.")
		doviz = requests.get('https://api.exchangeratesapi.io/latest?base=TRY', headers={'user agent' : 'curl'})
		print(doviz.text)# -*- coding: utf-8 -*-
import feedparser
import getpass
import requests

print("**********\nLogin Panel\n**********\n")

sys_user = "root"

sys_pass  = "1"

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
	print("**********\nMenu\n1-News\n2-Weather\n3-Currency\nq-Exit\n**********\n")
	islem = input("Select : ")
	if (islem == '1'):
	  haber = feedparser.parse('https://www.cnnturk.com/feed/rss/all/news')
	  for post in haber.entries:
	  	print(post.title)
	elif (islem == 'q'):
		print("Exited...")
	elif (islem == '2'):
		city = input('Pls Enter City Name: ')
		weather = requests.get('https://wttr.in/{}'.format(city+'?lang=tr'), headers={'user agent' : 'curl'})
		print(weather.text)
		
	elif (islem == '3'):
		print("1 Turkish Liras.")
		doviz = requests.get('https://api.exchangeratesapi.io/latest?base=TRY', headers={'user agent' : 'curl'})
		print(doviz.text)# -*- coding: utf-8 -*-
import feedparser
import getpass
import requests

print("**********\nLogin Panel\n**********\n")

sys_user = "root"

sys_pass  = "1"

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
	print("**********\nMenu\n1-News\n2-Weather\n3-Currency\nq-Exit\n**********\n")
	islem = input("Select : ")
	if (islem == '1'):
	  haber = feedparser.parse('https://www.cnnturk.com/feed/rss/all/news')
	  for post in haber.entries:
	  	print(post.title)
	elif (islem == 'q'):
		print("Exited...")
	elif (islem == '2'):
		city = input('Pls Enter City Name: ')
		weather = requests.get('https://wttr.in/{}'.format(city+'?lang=tr'), headers={'user agent' : 'curl'})
		print(weather.text)
		
	elif (islem == '3'):
		print("1 Turkish Liras.")
		currency = requests.get('https://api.exchangeratesapi.io/latest?base=TRY', headers={'user agent' : 'curl'})
		print(currency.text)
