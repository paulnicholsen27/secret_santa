import csv
import random
import smtplib
from string import strip
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import PASSWORD

TESTING = True

santa_path = "$HOME/Downloads/santa_test.csv"


class Player(object):

    def __init__(self, name, email, wants, address, forbidden):
        self.name = name
        self.email = email
        self.wants = wants
        self.forbidden = forbidden
        self.address = address


def get_player_info(csv_file):
    player_info = []
    with open(csv_file, 'r') as f:
        santareader = csv.DictReader(f)
        for row in santareader:
            data = map(strip, (row["Name"], row["Email"], row["Wants"], row["Address"], row["Forbidden"]))
            player_info.append(Player(data))
    print player_info
    return player_info


players = get_player_info(santa_path)
print players


# def assign_elves(players):
#     elves = []
#     for player in players:
#         elves += [player]
#     random.shuffle(elves)
#     for player in players:
#         if player.name != elves[0].name:
#             player.elf = elves.pop(0)
#         else:
#             player.elf = elves.pop(-1)


# assign_elves(players)

# SERVER = 'localhost'

# for player in players:
#     html_wants = " "
#     plain_text_wants = " "

#     if player.elf.wants:
#         plain_text_wants = "We know your elf is a big fan of %s." % player.wants
#         html_wants = "We know your elf is a big fan of <strong>%s</strong></br>." % player.wants

#     HMTL = """
#     <html>
#     <head></head>
#     <body>
#     <p>
#     Hello <strong>%s</strong>!  Happy Holidays!<br><br>

#     This year we've decided to play Secret Santa.<br>
#     For Secret Santa, please buy a gift for your secret elf, <strong>%s</strong>!

#     There is a price limit of $20 for Secret Santa gifts.<br><br>

#     %s

#     %s

#     Note:  This was sent anonymously so we don't know who has who.<br>
#     PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin my Christmas.<br><br>

#     Love,<br>
#     Paul
#     </p>
#     </body>
#     </html>
#     """ % (player.name, player.elf.name, html_wants, html_allergies)

#     TEXT = """
#     Hello %s!  Happy Holidays!

#     This year we've decided to play Secret Santa.
#     For Secret Santa, please buy a gift for your secret elf, %s!

#     There is a price limit of $15 for Secret Santa gifts.  Homemade gifts and treats encouraged!

#     %s

#     %s

#     Note:  This was sent anonymously so we don't know who has who.
#     PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin Christmas.

#     Love,
#     Paul
#     """ % (player.name, player.elf.name, plain_text_wants, plain_text_allergies)

#     FROM = 'pnichols104@gmail.com'
#     TO = 'pnichols104@gmail.com' if TESTING else [player.email]
#     SUBJECT = 'TEST SECRET SANTA' if TESTING else 'GMCW Secret Santa'

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
