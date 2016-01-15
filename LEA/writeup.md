# LEA (crypto 200)
##### team : sblan
##### participant：lwc (r04922161)
## Description
```
Yes, "leave as final exam".
http://52.68.224.122:9000/
```
## Solution
sign 部分
```
server.mount_proc('/sign') do |req, res|
  data = req.query['data']

  res.body = if data.nil? || data.include?('flag')
               'huh...?'
             elsif req.query['deprecated']
               OpenSSL::Digest::SHA1.hexdigest(strxor(KEY, data))
             else
               OpenSSL::HMAC.hexdigest('SHA1', KEY, data)
             end
end
```  
sign 的時候  
1. data 中不能有 flag  
2. request 中有 deprecated 輸出 sha1(strxor(KEY, data))  
3. request 中無 deprecated 輸出 HMAC(sha1, KEY, data)   

---

verify 部分
```
server.mount_proc('/verify') do |req, res|
  sig = req.query['sig']
  data = req.query['data']

  res.body = if sig.nil? || data.nil?
               'huh...?'
             elsif sig == OpenSSL::HMAC.hexdigest('SHA1', KEY, data)
               if data.include?('flag')
                 $stderr.puts "\e[32;1m#{req.remote_ip} get flag!\e[0m"
                 FLAG
               else
                 'verified, but no flag :('
               end
             else
               'OAQ...?'
             end
end
```
verify 的時候  
1. 給 data 和 sig。  
2. HMAC(sha1, KEY, data) == sig 且 data 中有 flag 字眼，就可以拿到 flag。  

---

可以做 Length Extension Attack，以下是初步想法  
1. 丟一段 data (+deprecated) 得到 sha1(data)  
2. 根據 sha1 演算法知道剛才得到的值其實是 sha1(data + padding(data))  
3. 根據 sha1 演算法直接構造 sha1(data + padding(data) + str)，其中 str 包含 flag 字眼  
4. HMAC(sha1, KEY, data) = sha1(KEY^opad | sha1(KEY^ipad | data))  
     ipad = '\x36' * 64  
     opad = '\x5c' * 64  
5. 湊巧以前有 implement 過修改版的 sha1   
https://github.com/lwcM/lwctools/blob/master/pysha1.py  
可以指定 sha1 的 interal state 以及 padding 後面要填的 bytes 數量  

---  

依照以上思路開始攻擊，  
由於 `fail if KEY.size < 30 || KEY.size > 50 `,  
只要傳送 data = ipad + s 去 sign (+deprecated)，就可以得到 sha1(KEY^ipad | s)
```
s = 'WTF'
payload = {'deprecated': '1', 'data': ipad+s}
r = requests.get(target + 'sign', params=payload)
```
將剛剛的結果作為 internal state，造出新的 sha1
```
first_hash = mysha1('flagq', msgbytes=64+64+5, state=r.content)
```
前面有 ipad + 'WTF' + padding('WTF') + 'flagq', 所以有 64+64+5 bytes,  
得到 first_hash = sha1(KEY^ipad | 'WTF' | padding(ipad + 'WTF') | 'flagq'),   
再來就拿 opad + first_hash 去 sign (+deprecated)，就可以得到 signature = sha1(KEY^opad | first_hash),   
這個值也就等同於 HMAC(sha1, KEY, 'WTF' + padding(ipad + 'WTF') + 'flagq')

`data = 'WTF\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x18flagq'`
```
payload = {'sig':signature , 'data': data}
r = requests.get(target + 'verify', params=payload)
```
最後得到 flag `CTF{did you use hashpump~?}`
