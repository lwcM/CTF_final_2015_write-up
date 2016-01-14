import requests
def strxor(a, b):
	s = ''
	for x, y in zip(a, b):
		s += chr(ord(x)^ord(y))
	return s

target = 'http://52.68.224.122:9010/'

cipher = 'rls883WrtBufrBQan2wovHBALhqB/LTzDOjNx1jmKF3LnFMk7Ja7AV9XxJu1'
ini = '{"user":"adminaaaaaaaaaaaaa"}'
res = '{"user":"admin","admin":true}'
'''
r = requests.get(target + 'login?user=adminaaaaaaaaaaaaa')
print r.content
s = r.content.decode('base64')
'''
s = cipher.decode('base64')
qq = s[0:16] + strxor(strxor(s[16:], ini), res)
print qq.encode('base64')

'''
r = requests.get(target + 'admin?token=' + qq.encode('base64'))

print r.content
'''

  
