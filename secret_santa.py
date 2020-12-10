import csv
import random
import smtplib
from string import strip
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import PASSWORD

TESTING = True

santa_path = "/Users/paulnichols/Downloads/santa_test - Sheet1.csv"


class Player(object):

    def __init__(self, name, email, wants, address, forbidden):
        self.name = name
        self.email = email
        self.wants = wants
        self.forbidden = forbidden
        self.address = address
        self.elf = None


def get_player_info(csv_file):
    player_info = []
    with open(csv_file, 'r') as f:
        santareader = csv.DictReader(f)
        for row in santareader:
            data = map(strip, (row["Name"], row["Email"], row["Wants"], row["Address"], row["Forbidden"]))
            player_info.append(Player(*data))
    return player_info


players = get_player_info(santa_path)


def assign_elves(players):
    elves = []
    for player in players:
        elves += [player]
    random.shuffle(elves)
    for player in players:
        found_elf = False
        index = 0
        while not found_elf:
            try:
                if player.name != elves[index].name and player.forbidden != elves[index].name:
                    player.elf = elves.pop(index)
                    found_elf = True
                else:
                    index += 1
            except IndexError:
                for player in players:
                    player.elf = None 
                    return assign_elves(players)

assign_elves(players)

                

SERVER = 'localhost'

for player in players:


    HMTL = """
    <html>
    <head></head>
    <body>
    <p>
    Hello <strong>%s</strong>!  Happy Holidays!<br><br>

    This year we've decided to play Secret Santa.<br>
    For Secret Santa, please buy a gift for your secret elf, <strong>%s</strong>!<br>

    There is a price limit of $15 for Secret Santa gifts.  Homemade gifts and treats encouraged!<br><br>

    You can mail your elf their gift to:<br><br>

    <strong>%s</strong><br><br>

    When asked for some ideas for gifts, your elf said:<br><br>

    <strong>%s</strong><br><br>

    Note:  This was sent anonymously so we don't know who has who.<br>
    PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin my Christmas.<br><br>

    I hope you're all doing well in these very difficult times and I can't wait to make music with you all again. Stay safe <3 <br><br>

    Love,<br>
    Paul
    </p>
    </body>
    </html>
    """ % (player.name, player.elf.name, player.elf.address, player.elf.wants )

    TEXT = """
    Hello %s!  Happy Holidays!

    This year we've decided to play Secret Santa.
    For Secret Santa, please buy a gift for your secret elf, %s!

    There is a price limit of $15 for Secret Santa gifts.  Homemade gifts and treats encouraged!

    You can mail your elf their gift to:

    %s

    When asked for some ideas for gifts, your elf said:

    %s


    Note:  This was sent anonymously so we don't know who has who.
    PLEASE DO NOT REPLY DIRECTLY TO THIS MESSAGE or you will ruin my Christmas. <3

    Love,
    Paul
    """ % (player.name, player.elf.name, player.elf.address, player.elf.wants)

    FROM = 'paulnicholsen27@gmail.com'
    TO = 'paulnicholsen27@gmail.com' if TESTING else [player.email]
    SUBJECT = 'TEST SECRET SANTA' if TESTING else 'GMCW Secret Santa'

    msg = MIMEMultipart('alternative')
    part1 = MIMEText(TEXT, 'plain')
    part2 = MIMEText(HMTL, 'html')
    msg.attach(part1)
    msg.attach(part2)
    msg['Subject'] = SUBJECT
    server = smtplib.SMTP('smtp.gmail.com', 587)  # port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('paulnicholsen27@gmail.com', PASSWORD)
    server.sendmail(FROM, TO, msg.as_string())
    server.close()
