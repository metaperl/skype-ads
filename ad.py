import os
import time

import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

skypechat = '#debbiematics/$b3691abf8f26222'

def post_ad(text):
    c = skype.Chat(skypechat)
    c.SendMessage(text)

import os

ad_path = "ads"
ad_delay = 60 # minutes

def minutes_to_seconds(m):
    return m * 60

def post_ads():
    for (path, dirs, files) in os.walk(ad_path):
        print path
        print dirs
        print files
        print "----"
        for file in files:
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
