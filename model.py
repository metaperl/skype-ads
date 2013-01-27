from elixir import *

metadata.bind = "sqlite:///model.sqlite"
metadata.bind.echo = True

class ChatRoom(Entity):
    skype_id = Field(Unicode(64)) # the skype id for the room, not rdbms id
    name = Field(Unicode(64))

class Ad(Entity):
    filename = Field(Unicode(64))
    program = OneToMany('Program')

class Program(Entity):
    name = Field(Unicode(64))
    short_name = Field(Unicode(64))
    ad = ManyToOne('Ad')

class Campaign(Entity):
