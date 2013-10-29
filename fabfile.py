
from __future__ import print_function

# core
import datetime
import itertools
import logging
import os
import random
import time

# 3rd party
import Skype4Py

ad_path = "ads"
ad_delay = 120 # middle of the day when no one is working
current_campaign=None


# Create an instance of the Skype class.
skype = Skype4Py.Skype()

skype.Timeout = 900000

# Connect the Skype object to the Skype client.
skype.Attach()

#     letsjoin =  '#lkcglobal/$2d2b21b71349065e',


rooms = dict(
    bills = '#bill.8bucks/$a707d292b44d57a5',
    barbs = '#barbarella623/$e1c4d8a66a9d8209',
    feel_free = '#andrek333/$e38c0fe714eefd4e',
    anything_goes = '#lyndabourgeois/$e7391b9ffa653fe6',
    ad_with_gigi = '#gina.dujardin/$38e60fce428eadd1',
    work_smarter = '#dotone4/$3ae54c7bded9b832',
    hy_22 = '#lorrie.trotter/$bbb7d486ea6b8d69',
    perfect_trade = '#lordking989/$ac4d25d36c595eea',
    new_programs = '#jimfurr/$2863804c49a01247',
    best_of_best = '#carol.shannon5/$7c08cb513334cc60',
    dollar_monster = '#toptenearner/$4b519b42a7091315',
    networking_in_motion = '#ezyebiz/$d6e8a7a402943eff',
    business_experts = '#kingmakerganesh/$554d6f21e608af70',
    carols_room = '#carol.shannon5/$cj.nulifetime;c3a063745b4f9a0f',
    positive_thinking = '#carol.shannon4/$94cefc7f09c4c446',
    gfp_with_updates = '#lynette.artin/$1a07187ff6215046',
    unlimited_ad = '#debbiematics/$b3691abf8f26222'
)

#room_cycle = itertools.cycle(

#rk = reversed(rooms.keys())

rk = rooms.keys()
random.shuffle(rk)
rk = [ 'bills' ] + rk
print(rk)

room_cycle = itertools.cycle(rk)


random.seed()

# -----------------------------------------------------------------------

def programs(filename):
    desired = 'cbk karatbars potis uinvest'.split()
    return any (s in filename for s in desired)

def general(filename):
    desired = 'cbk healthy ipdn karatbars nacv potis rays silver-saver solavei uinvest'.split()
    return any (s in filename for s in desired)

def invest2(filename):
    desired = 'pure-income potis uinvest'.split()
    return any (s in filename for s in desired)

# 'belizers cbk karatbars matchrateplus solavei ufund uinvest wealthbuilders'.split()

def mlmi(filename):
    desired = 'belizers cbk karatbars matchrateplus solavei ufund'.split()
    return any (s in filename for s in desired)


def mlm(filename):
    desired = 'cbk flipping karatbars ufund'.split()
    return any (s in filename for s in desired)

def kb(filename):
    desired = 'karatbars'.split()
    return any (s in filename for s in desired)

def urgent(filename):
    desired = 'karatbars/urgent'.split()
    return any (s in filename for s in desired)

def golden(filename):
    desired = 'golden-ark'.split()
    return any (s in filename for s in desired)

def normal(filename):
    desired = 'lttw selina'.split()
    return any (s in filename for s in desired)


def warm(filename):
    desired = ''.split()
    return any (s in filename for s in desired)

def hot(filename):
    desired = 'karatbars/uk'.split()
    return any (s in filename for s in desired)

# -----------------------------------------------------------------------


def select_room_random():
    return random.choice(rooms.keys())

def select_room_cyclic():
    return room_cycle.next()

room_selector = select_room_cyclic

def current_time():
    now = datetime.datetime.now()
    return now.strftime("%I:%M%p")

def post_ad(file):
    with open(file, 'r') as f:
        ad_copy = f.read()
        room = room_selector()
        print(" to {0}".format(room))
        try:
            c = skype.Chat(rooms[room])
        except:
            logging.warn("ERROR in c.Chat({0})".format(room))
            return
        try:
            c.SendMessage(ad_copy)
        except:
            logging.warn("ERROR in c.SendMessage(ad_copy)")
            pass

def minutes_to_seconds(m):
    return m * 60


def wanted_ad(filename):
    return current_campaign(filename)

def random_file():
    files = [os.path.join(path, filename)
             for path, dirs, files in os.walk(ad_path)
             for filename in files
             if not filename.endswith("~")]
    return random.choice(files)

def get_wanted_file():
    while True:
        file = random_file()
        if not wanted_ad(file):
            #print("\t\tskipping {0}".format(file))
            pass
        else:
            print("[ {0} ] posting {1}".format(current_time(), file), end="")
            return file


def post_ads():
    while True:
        file = get_wanted_file()
        post_ad(file)
        time.sleep( minutes_to_seconds(ad_delay) )

def main(campaign='general'):
    global current_campaign
    current_campaign = globals()[campaign]
    while True:
        post_ads()


if __name__ == '__main__':
    main()
