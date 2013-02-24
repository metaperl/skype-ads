#!/usr/bin/python

from __future__ import print_function

import datetime
import itertools
import logging
import os
import random
import time



import Skype4Py

ad_path = "ads"
ad_delay = 30 # minutes


# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

#     letsjoin =  '#lkcglobal/$2d2b21b71349065e',

rooms = dict(
    unlimited_ad = '#debbiematics/$b3691abf8f26222',
    hy_22 = '#lorrie.trotter/$bbb7d486ea6b8d69',
    perfect_trade = '#lordking989/$ac4d25d36c595eea',
    new_programs = '#jimfurr/$2863804c49a01247',
    best_of_best = '#carol.shannon5/$7c08cb513334cc60',
    dollar_monster = '#toptenearner/$4b519b42a7091315',
    networking_in_motion = '#ezyebiz/$d6e8a7a402943eff',
    business_experts = '#kingmakerganesh/$554d6f21e608af70'
)

room_cycle = itertools.cycle(rooms.keys())


random.seed()
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

def general_advertising(filename):
    desired = 'asn:tax eternal ipdn london potis rays silver-saver solavei traderush traffic uinvest'.split()
    return any (s in filename for s in desired)

def general_advertising2(filename):
    desired = 'asn:tax eternal ipdn karatbars potis rays silver-saver solavei traffic uinvest'.split()
    return any (s in filename for s in desired)

def karatbars_advertising(filename):
    desired = 'rays karatbars'.split()
    return any (s in filename for s in desired)

def hot_programs(filename):
    desired = 'goldindex jubi like traderush'.split()
    return any (s in filename for s in desired)

#current_campaign = hot_programs
#current_campaign = general_advertising
#current_campaign = karatbars_advertising
current_campaign = general_advertising2

def wanted_ad(filename):
    return current_campaign(filename)

def random_file():
    files = [os.path.join(path, filename)
             for path, dirs, files in os.walk(ad_path)
             for filename in files
             if not filename.endswith("~")]
    return random.choice(files)

def get_wanted_file():
    file = random_file()
    if not wanted_ad(file):
        print("\t\tskipping {0}".format(file))
        return get_wanted_file()
    else:
        print("[ {0} ] posting {1}".format(current_time(), file), end="")
        return file



def post_ads():
    while True:
        file = get_wanted_file()
        post_ad(file)
        time.sleep( minutes_to_seconds(ad_delay) )

def main():
    while True:
        post_ads()


if __name__ == '__main__':
    main()
