# CTR (crypto 100)
##### team : sblan
##### participant : 廖唯辰 (r04922161)
## Description
```
CTR mode has significant efficiency advantages over the standard encryption, but...
http://52.68.224.122:9010/
```
## Solution
題目是將 username 包成 json 丟到 AES-128 CTR mode, 再連 iv 一起丟出來。  
但是在 CTR mode 下，如果 iv 一樣，AES本身加密出來結果不變，這個結果再 xor 明文得到密文 。  
因此只要將得到的加密結果 xor 已知明文，再 xor 欲變成的明文，就會得到在同樣 iv 下對新的明文加密的結果。

最後要給一個 token，使得這個 token 解密出來要有 admin 這項，值是 true  

首先，先丟 user = adminaaaaaaaaaaaaa，得到 cipher 和使用的 iv
```
http://52.68.224.122:9010/login?user=adminaaaaaaaaaaaaa
```
得到
```
rls883WrtBufrBQan2wovHBALhqB/LTzDOjNx1jmKF3LnFMk7Ja7AV9XxJu1
```
這時候包出來的 json 會是
```
{"user":"adminaaaaaaaaaaaaa"}
```
欲改變成
```
{"user":"admin","admin":true}
```
這時候只要如此
```
from = '{"user":"adminaaaaaaaaaaaaa"}'
to   = '{"user":"admin","admin":true}'
new_cipher = strxor(strxor(cipher, from), to)
```
最後把 iv 和 new cipher 丟回去
```
http://52.68.224.122:9010/admin?token=rls883WrtBufrBQan2wovHBALhqB/LTzDOjNx1jmaxCInFYo5Jn4WkpE0Ny1
```
得到 flag
```
{"user":"admin","admin":true,"flag":"CTF{Flip Flop F1ip Fl0p}"}
```
