# Y (reverse 100 150)
##### team: sblan
##### participant: 廖唯辰 (r04922161)
## Description
```
Python is a clean and clear language, which is easy to understand.
Warning: You may need a supercomputer, or to optimize this program.
https://www.dropbox.com/s/35b92t3ohrsocnu/y.pyc?dl=0
https://www.dropbox.com/s/7jxvdvzmode2mce/y2.pyc?dl=0
```
## Solution
給了`.pyc`檔案，裝個 `uncompyle2`, decompile 之後觀察程式碼, 大概在做如下的事情  
y.pyc
```
def f(n):
    if n == 1:
        return 1
    elif n & 1:
        return f(3 * n + 1) + 1
    else:
        return f(n / 2)

y = int(raw_input())
sum = 0
for i in range(1, y+1):
    sum += f(i)

print ['QQ{Fail}', 'CTF{' + hex(y)[2:] + '}'][sum == 3242]
```
y2.pyc 就是把 `3242` 改為 `37765512783`  
這其實就是 Collatz conjecture  
f 用來計算某數字經過多少操作才會變為 1  
1~y 代入 f 的 sum 要等於他給定的數字  
用 Dynamic Programming 加上多一點的 RAM 就可以很快求出來了  
有些比較難求的數字，可以直接 request `http://www.nitrxgen.net/collatz/` 得到結果  
y.pyc 求出來是 100, flag 為 `CTF{64}`  
y2.pyc 求出來是 201398976, flag 為 `CTF{c011ac0}`  
