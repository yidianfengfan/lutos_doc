#!/usr/bin/env python
from pymongo import Connection
import bson
import hashlib


connection = Connection("127.0.0.1", 27017)
db = connection.test_database

print('ObjectID')
for i in range(1, 1000000):
    db.objectids.insert({'i': i})

print('int')
for i in range(1, 1000000):
    db.ints.insert({'_id': i, 'i': i})

print('Base64 BSON')
for i in range(1, 1000000):
    db.base64s.insert({'_id': \
        bson.Binary(hashlib.md5(str(i)).digest(),
        bson.binary.MD5_SUBTYPE), 'i': i})

print('string')
for i in range(1, 1000000):
    db.strings.insert({'_id': hashlib.md5(str(i)).digest(), 'i': i})