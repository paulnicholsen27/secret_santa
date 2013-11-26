import random
import pprint
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