import random
import pprint
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import PASSWORD

TESTING = True

players = [{'name': 'Paul', 'email': 'pnichols104@gmail.com', 'elf': '', 'exclude':['Jason']},
		  {'name': 'Jason', 'email': 'jason.b.olsen@gmail.com', 'elf': '', 'exclude':['Paul']},
		  {'name': 'Matt', 'email': 'matthew.angrisani@gmail.com', 'elf': '', 'exclude':['Emily']},
		  {'name': 'Emily', 'email': 'emily.angrisani@gmail.com', 'elf': '', 'exclude':['Matt']},
		  {'name': 'Barbara', 'email': 'bknispel@mindspring.com', 'elf': '', 'exclude':['David']},
		  {'name': 'David', 'email': ' dkennedy18@nyc.rr.com', 'elf': '', 'exclude':[' Barbara']},
		  {'name': 'Sandy', 'email': 'sangrisani@hotmail.com', 'elf': '', 'exclude':['']},
		]

def assign_elves():
	santas = [player['name'] for player in players]
	assigned = False
	while not assigned:
		random.shuffle(santas)
		potential = True
		while potential:
			for i in range(len(santas)):
				if players[i]['name'] != santas[i] and santas[i] not in players[i]['exclude']:
					players[i]['elf'] = santas[i]
				else:
					potential = False
					break
			if potential:
				assigned = True
			break

assign_elves()

SERVER = 'localhost'
for player in players:
	
	HMTL = """
	<html>
	<head></head>
	<body>
	<p>
	Hello <strong>%s</strong>!  Merry Christmas!<br><br>

	This year we've decided to play Secret Santa and Yankee Swap.  
	For Secret Santa, please buy a gift for your secret elf, <strong>%s</strong>!  
	There is a price limit of $50 for Secret Santa gifts.<br><br>

	For Yankee Swap, please purchase a gift for a grab-bag costing no more than $25.<br><br>

	Note:  This was sent anonymously so I won't know who has who.  
	PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin my Christmas.<br><br>

	Love,<br>
	Paul
	</p>
	</body>
	</html>
	""" %(player['name'], player['elf'])

	TEXT = """
	Hello %s!  Merry Christmas!

	This year we've decided to play Secret Santa and Yankee Swap.  
	For Secret Santa, please buy a gift for your secret elf, %s!  
	There is a price limit of $50 for Secret Santa gifts.

	For Yankee Swap, please purchase a gift for a grab-bag costing no more than $25.

	Note:  This was sent anonymously so I won't know who has who.  
	PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin my Christmas.

	Love,
	Paul
	""" %(player['name'], player['elf'])

	FROM = 'pnichols104@gmail.com'
	TO = 'pnichols104@gmail.com' if TESTING else [player['email']]
	SUBJECT = 'TEST SECRET SANTA' if TESTING else 'Secret Santa'

	msg = MIMEMultipart('alternative')
	part1 = MIMEText(TEXT, 'plain')
	part2 = MIMEText(HMTL, 'html')
	msg.attach(part1)
	msg.attach(part2)
	msg['Subject'] = SUBJECT
	server = smtplib.SMTP('smtp.gmail.com',587) #port 465 or 587
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login('pnichols104@gmail.com', PASSWORD)
	server.sendmail(FROM, TO, msg.as_string())
	server.close()