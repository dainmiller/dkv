#!/usr/bin/env python3

import collections
import random

class KeyValueStore:
    """ Distributed key value store

        TODO(@dain): <<TO BE REMOVED BEFORE ALPHA LAUNCH>>

        # General <Key,Value> Store Implementation
        #
        - [x] Ability to set a key and value
        - [x] Ability to retrieve a value via the key
        - [x] Ability to retrieve all keys
        - [x] Ability to get all values
        - [x] Ability to update a value by key

        # Distributed <Key,Value> Store Integration
        #
        - [x] Ability to add a key and value, and it automatically adds URL to
          system as key
            {
                URL_HERE_TO_SERVER: {
                }
            }
        - [ ] Ability to store the data on the server - the value should point
          to a route with d structure
        - [ ] Route should point to a controller method
        - [ ] Controller method should save it to the DB (in this case redis)
        - [ ] Consider abstracting the storage implementation to allow any store
        - [ ] Abstract the code into a library for a few languages (python
          first, ruby second)
            - [ ] Library should contain all of the code above, and provide
              clear instructions
            - [ ] Allow to inheret from controller/storage model/etc so you can
              easily override and provide custom functionality
    """

    SERVERS = [
        'http://localhost:3000',
        'http://localhost:5000',
        'http://localhost:6000'
    ]

    def __init__(self):
        self.kv = collections.OrderedDict()

    def set(self, key, value):
        if key and value:
            self.kv[key] = value

    def update(self, key, value):
        for k in self.kv:
            if k == key:
                self.kv[k] = value
                return "Updated"

    def getValueByKey(self, key):
        for k in self.kv:
            if k == key:
                return self.kv[k]

    def getAllKeys(self):
        keys = []
        for k in self.kv:
            keys.append(k)
        return keys

    def getAllValues(self):
        values = []
        for k in self.kv:
            values.append(self.kv[k])
        return values

    def distributedSet(self, key, value):
        serverQuantity  = len(self.SERVERS)
        randomNumber    = random.randrange(0, serverQuantity)
        self.set(self.SERVERS[randomNumber], {
            key: value
        })

# END OF FILE 

v = KeyValueStore()
v.set('a', 1)
v.set('b', 3)
print(v.kv)

print(v.getValueByKey('a'))
print(v.getValueByKey('b'))
print(v.getAllKeys())
print(v.getAllValues())
print(v.update('a', 2))
print(v.getValueByKey('a'))

v.distributedSet('a', 2)
print(v.kv)
