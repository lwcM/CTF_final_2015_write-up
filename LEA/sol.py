import requests
import struct
from pysha1 import mysha1
from pysha1 import padding
# my implementation of sha1 is in pysha1.py

target = 'http://52.68.224.122:9000/'

s = 'WTF'
ipad = '\x36'*64
opad = '\x5c'*64
ext = 'flagq'

payload = {'deprecated': '1', 'data': ipad+s}
r = requests.get(target + 'sign', params=payload)
#print r.content


print repr(padding(ext, msgbytes=64+64+5))
# use new state in r.content to calculate first hash
first_hash = mysha1(ext, msgbytes=64+64+5, state=r.content)


payload = {'deprecated': '1', 'data': opad+first_hash}
r = requests.get(target + 'sign', params=payload)

signature = r.content
data = padding(s, msgbytes=64+3) + ext

#print 'signature = ' + signature
print 'data = ' + repr(data)

payload = {'sig':signature , 'data': data}
r = requests.get(target + 'verify', params=payload)
print r.content


