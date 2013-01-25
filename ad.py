#!/usr/bin/python

import logging
import os
import random
import time

import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

rooms = dict(
    unlimited_ad = '#debbiematics/$b3691abf8f26222',
    letsjoin =  '#lkcglobal/$2d2b21b71349065e'
)

def post_ad(text):
    logging.debug("Posting {0}".format(text))
    c = skype.Chat(rooms['unlimited_ad'])
    c.SendMessage(text)

import os

ad_path = "ads"
ad_delay = 60 # minutes

def minutes_to_seconds(m):
    return m * 60

def wanted_ad(filename):
    desired = 'uinvest potis elias general silver-saver ipdn'.split()
    return any (
        filename.startswith(s) and not filename.endswith('~')
        for s in desired
    )

def post_ads():
    for (path, dirs, files) in os.walk(ad_path):
        for file in files:
            print file
            if not wanted_ad(file):
                print "\tskipping"
                continue
            else:
                print "\tposting"
            fullpath = os.path.join(path, file)
            with open(fullpath, 'r') as f:
                ad_copy = f.read()
                post_ad(ad_copy)
                time.sleep( minutes_to_seconds(60) )

def main():
    while True:
        post_ads()


if __name__ == '__main__':
    main()
