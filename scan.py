#!/usr/bin/python

import codecs
import sys

import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

# Obtain some information from the client and print it out.
# print 'Your full name:', skype.CurrentUser.FullName
# print 'Your contacts:'
# for user in skype.Friends:
#     print '...', user.FullName.encode('utf-8').strip()

# print 'Your groups:'
# for group in skype.Groups:
#     print ',,,', group.DisplayName.encode('utf-8').strip()

print 'Your chats:'
for chat in skype.Chats:
    m = len(chat.Members)
    (n, fn) = [
        s.encode('ascii', 'ignore')
        for s in (chat.Name, chat.FriendlyName)
    ]
    print '{0}\t{1}\t{2}'.format(m, n, fn)
