import requests
MAXN = 3000000000
N = 3000000000
d = {}
d[1] = 1

def query(x):
	r = requests.post('http://www.nitrxgen.net/collatz/' + str(x) + '/')
	s = r.content
	return int(s[s.find('0:'):s.find('</pre')].split()[-2][:-1]) + 1

def f(x):
	try:
		return d[x]
	except KeyError:
		if len(d) + 1 > N:
			return query(x)
		if x & 7 == 5:
			d[x]=f(3*((x-5)>>3)+2)+4
		elif x & 1:
			d[x]=f(x*3+1)+1
		else:
			d[x]=f(x>>1)+1
		return d[x]


def dp(nn):
	x = 0
	sm = 0
	for i in range(1, nn+1):
		sm += f(i)
		if (i >> 19) != x:
			x = i >>19
			print i, sm
		if sm >= 37765512783:
			return sm
	return sm

def gogo(n):
	i = 0
	sm = 0
	while sm < n and i <= MAXN:
		i += 1
		sm += d[i]
	return hex(i)[2:]

'''
print dp(100000001, 150000000, 18023493583)
print gogo(3242)
'''
# 18023493583
#print query(100)
#print query(100000000)
print dp(200000000)

print gogo(37765512783)
