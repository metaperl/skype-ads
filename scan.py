#!/usr/bin/python

import Skype4Py

# Create an instance of the Skype class.
skype = Skype4Py.Skype()

# Connect the Skype object to the Skype client.
skype.Attach()

# Obtain some information from the client and print it out.
print 'Your full name:', skype.CurrentUser.FullName
print 'Your contacts:'
for user in skype.Friends:
    print '...', user.FullName.encode('utf-8').strip()

print 'Your groups:'
for group in skype.Groups:
    print ',,,', group.DisplayName.encode('utf-8').strip()

print 'Your chats:'
for chat in skype.Chats:
    (n, fn) = chat.Name.encode('utf-8'), chat.FriendlyName.encode('utf-8')
    print 'skypename: {0} topic: {1} friendly name: {2}'.format(n, chat.Topic, fn)
