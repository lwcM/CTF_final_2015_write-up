import subprocess
from pwn import *

context.log_level = 'error'

r = []
o = []
process_num = 20

def go(i):
	r.append(remote('52.68.224.122', 9020))
	#r.append(process('./lucky'))
	s = r[i].recvuntil('000000.*')
	s = s[s.find('SHA')+11:][0:8]
	s = ' '.join(map(str, map(ord, [x for x in s.decode('hex')])))
	o.append(remote('127.0.0.1', 8888))
	o[i].send(s + '\n')


ret = ['' for _ in xrange(20)]
for i in range(process_num):
	go(i)

for i in range(process_num):
	ret[i] = o[i].recv(4).encode('hex')

for i in range(process_num):
	r[i].sendline(ret[i])



qq = ['rock', 'paper', 'scissors']
ans = ['' for _ in xrange(21)]

for i in range(0, process_num):
	j = 0
	WIN = True
	for j in range(1, 21):
		print r[i].recvuntil('== Round %02d ==' % j)
		if ans[j] != '':
			r[i].sendline(ans[j])
		else:
			r[i].sendline(qq[0])
			ss = r[i].recvuntil(')')
			print ss
			if 'win' in ss:
				ans[j] = qq[0]
			elif 'tie' in ss:
				ans[j] = qq[1]
				WIN = False
				break
			else:
				ans[j] = qq[2]
				WIN = False
				break
	if WIN:
		print r[i].recv()
		print r[i].recv()
		break



