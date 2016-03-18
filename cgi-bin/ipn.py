#!/usr/local/Cellar/python/2.7.11/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import cgi
import ssl
import urllib
import httplib

form=cgi.FieldStorage()
post = {key: form[key].value for key in form.keys()}
print "application/json\n"

def ipn(post):
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    conn = httplib.HTTPSConnection('www.sandbox.paypal.com', context=context)
    payload = 'cmd=_notify-validate&' + \
        '&'.join(['{}={}'.format(key, urllib.quote_plus(val))
                  for key, val in post.items()])

    conn.request('POST', '/cgi-bin/webscr', payload)
    res = conn.getresponse()
    result = res.read()
    if not result == 'VERIFIED':
        print json.dumps({'error': 'ipn authentication check error'})
        sys.exit()
    return result


ipn(post)
data = dict(post)

print json.dumps(data)