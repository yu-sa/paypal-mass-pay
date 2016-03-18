#!/usr/local/Cellar/python/2.7.11/bin/python
# -*- coding: utf-8 -*-
import ssl
import urllib
import httplib

def mass_pay_api():
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    conn = httplib.HTTPSConnection('api-3t.sandbox.paypal.com', context=context)
    params = urllib.urlencode(
        {"USER": "xxxxxxxxxxxxxxxxx",
         "PWD": "XXXXXXXXXXXXXXXX",
         "SIGNATURE": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
         "METHOD": "MassPay",
         "VERSION": 90,
         "RECEIVERTYPE": "EmailAddress",
         "CURRENCYCODE": "USD",
         "L_EMAIL0": "XXXXXXXXXXXXXXXXXXXXXXXXXX",
         "L_AMT0": "0.01",
         "L_UNIQUEID0": "test1"})
    conn.request('POST', '/nvp', params)
    res = conn.getresponse()
    data = res.read()
    return data

data = mass_pay_api()

f = open("test.log", "a")
f.write(data)
f.close()