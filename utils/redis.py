#!/usr/bin/python
# @Time  : 2020/5/9 15:28
# @Author: LOUIE
# @Desc  : 操作 redis
from redis import StrictRedis

class ConnRedis:
    def set_redis(self, key):
        conn = StrictRedis(host='120.79.216.107', port=6379, db=0, password=123456)
        conn.incr(key, amount=1)