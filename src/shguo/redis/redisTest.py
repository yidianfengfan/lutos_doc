#!/usr/bin/python
# encoding: utf-8

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

#r = redis.Redis(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
print r.set('foo', 'bar')

print r.get('foo')
