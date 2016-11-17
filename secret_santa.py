import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import PASSWORD
import csv

TESTING = True

santa_path = "/Users/paulnicholsen/Desktop/santa_test.csv"


class Player(object):

    def __init__(self, name, email, allergies, wants):
        self.name = name
        self.email = email
        self.allergies = allergies
        self.wants = wants

def get_player_info(csv_file):
    with open(csv_file, 'r') as f:
        santareader = csv.DictReader(f)
        # import ipdb; ipdb.set_trace()
        # player_info = [{"name": row["Your name"], "email": row["Email"], "allergies": row["Allergies"], "wants": row["Wants"]} for row in santareader]
        player_info = [Player(row["Your name"], row["Email"], row["Allergies"], row["Wants"]) for row in santareader]
    return player_info

players = get_player_info(santa_path)
print players

def assign_elves():
    elves = random.shuffle([player.name for player in players])
    import ipdb; ipdb.set_trace()
    for player in players:
        print player
        if player.name != elves[0]:
            player.elf = elves[0]
            elves.pop(0)
        else:
            player.elf = elves[-1]
            elves.pop(-1)

assign_elves()
print players

# SERVER = 'localhost'

# for player in players:

#     if player["allergies"]:
#         allergies = "We know that your elf does not like <strong>%s</strong>.<br>" % player["allergies"]

#     if player["wants"]:
#         wants = "We know your elf is a big fan of <strong>%s</strong></br>" % player["wants"]

#     HMTL = """
#     <html>
#     <head></head>
#     <body>
#     <p>
#     Hello <strong>%s</strong>!  Merry Christmas!<br><br>

#     This year we've decided to play Secret Santa.  
#     For Secret Santa, please buy a gift for your secret elf, <strong>%s</strong>!

#     There is a price limit of $20 for Secret Santa gifts.<br><br>

#     %s

#     %s

#     Note:  This was sent anonymously so we don't know who has who.  
#     PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin my Christmas.<br><br>

#     Love,<br>
#     Paul
#     </p>
#     </body>
#     </html>
#     """ % (player['name'], players[player["elf"]]["allergies"], players[player["elf"]]["wants"], player['elf'])

#     TEXT = """
#     Hello %s!  Merry Christmas!

#     This year we've decided to play Secret Santa and Yankee Swap.  
#     For Secret Santa, please buy a gift for your secret elf, %s!  
#     There is a price limit of $50 for Secret Santa gifts.

#     For Yankee Swap, please purchase a gift for a grab-bag costing no more than $25.

#     Note:  This was sent anonymously so I won't know who has who.  
#     PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin my Christmas.

#     Love,
#     Paul
#     """ % (player['name'], player['elf'])

#     FROM = 'pnichols104@gmail.com'
#     TO = 'pnichols104@gmail.com' if TESTING else [player['email']]
#     SUBJECT = 'TEST SECRET SANTA' if TESTING else 'Secret Santa'

#     msg = MIMEMultipart('alternative')
#     part1 = MIMEText(TEXT, 'plain')
#     part2 = MIMEText(HMTL, 'html')
#     msg.attach(part1)
#     msg.attach(part2)
#     msg['Subject'] = SUBJECT
#     server = smtplib.SMTP('smtp.gmail.com', 587)  # port 465 or 587
#     server.ehlo()
#     server.starttls()
#     server.ehlo()
#     server.login('pnichols104@gmail.com', PASSWORD)
#     server.sendmail(FROM, TO, msg.as_string())
#     server.close()
