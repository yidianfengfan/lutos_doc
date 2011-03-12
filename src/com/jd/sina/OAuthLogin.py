#coding=gbk
'''
Created on 2011-3-2

@author: leishg
'''
from weibopy.api import API
from weibopy.auth import OAuthHandler

App_Key = "1301184712"
App_Secret = "72023ad9cf7e87b163921cc1490c2cef"

auth = OAuthHandler(App_Key, App_Secret)
auth_url = auth.get_authorization_url()
print 'Please authorize: ' + auth_url
verifier = raw_input('PIN: ').strip()

#http://api.t.sina.com.cn/oauth/authorize?oauth_token=4a72f6e4813750610c47f4c86120d0a2
#496558
access_token = "7e4261f41e53aab3e2f7da5c8ffb3f1b"
access_key = "285414"
#auth.get_access_token(verifier)
auth.setToken("0ae7e293bfabc120c74fc25ab234f028", "77083ac464f82da67f5a7764b9d0088d")
api = API(auth)

status = api.get_user(id=1650951660)
print status
#status = api.update_status('城市黄昏--洪启'.encode("utf-8"))
#print status.id

#print status.text



