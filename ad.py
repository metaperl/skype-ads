#!/usr/bin/python

import itertools
import logging
import os
import random
import time

import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

#     letsjoin =  '#lkcglobal/$2d2b21b71349065e',

rooms = dict(
    unlimited_ad = '#debbiematics/$b3691abf8f26222',
    perfect_trade = '#lordking989/$ac4d25d36c595eea',
    new_programs = '#jimfurr/$2863804c49a01247',
    best_of_best = '#carol.shannon5/$7c08cb513334cc60'
)

room_cycle = itertools.cycle(sorted(rooms.keys()))

ad_path = "ads"
ad_delay = 15 # minutes

random.seed()
def select_room_random():
    return random.choice(rooms.keys())

def select_room_cyclic():
    return room_cycle.next()

room_selector = select_room_random

def post_ad(file):
    with open(file, 'r') as f:
        ad_copy = f.read()
        room = room_selector()
        print room
        c = skype.Chat(room)
        c.SendMessage(ad_copy)

def minutes_to_seconds(m):
    return m * 60

def wanted_ad(filename):
    desired = 'asn:tax elias eternal eurex gold ipdn jubi potis silver-saver solavei traffic uinvest xchanger'.split()
    return any (s in filename for s in desired)

def random_file():
    files = [os.path.join(path, filename)
             for path, dirs, files in os.walk(ad_path)
             for filename in files
             if not filename.endswith("~")]
    return random.choice(files)

def get_wanted_file():
    file = random_file()
    if not wanted_ad(file):
        print "\tskipping {0}".format(file)
        return get_wanted_file()
    else:
        print "\tposting {0}".format(file)
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
