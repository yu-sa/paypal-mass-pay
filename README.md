# Paypal Mass Pay & Ipn

paypalで提供しているMass PayとIpnのサービスをさっと利用するためのソースコード。
pythonのCGIHTTPServerを利用してサーバを立ててさっと使えるようになっています。

*フォルダ構成
```
paypal-mass-pay
├─README.md         # Read Me
├─cgiserver.py      # サーバ起動pyファイル
└─cgi-bin
  ├─mass_pay.py     # mass pay apiを叩いてくれる
  └─ipn.py          # ipnのrequestを受け付けてくれる
```

*サーバ起動
```
python cgi_server.py
```
