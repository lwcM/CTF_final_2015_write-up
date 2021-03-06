# Lucky (crypto 300)
##### team : sblan
##### participant : 廖唯辰 (r04922161)
## Description
```
Let's play a game!
nc 52.68.224.122 9020
https://www.dropbox.com/s/c5vnss4iqlfphjl/lucky?dl=0
```
## Solution
1. 反組 binary之後，發現程式第一部分(這裡稱為第一關)給定一個 8 bytes 字串的前 4 個 bytes，問若將這個字串作 sha1 之後前三個bytes 都是 0x00，那一開始的字串後 4 個 bytes 為何？這部份暴力求解即可。  
2. 第二關是和程式猜拳，可以出 `'rock', 'paper', 'scissors'` 三種，需要連贏 20 場才能過關，拿到 flag。  
3. 電腦出拳的方法是用 `rand()`，而 seed 設定為 `srand(time(NULL))`，時間點在過上述 sha1 的第一部分之後。  
4. 注意到，可以知道沒過關的時候是平手還是輸了。  
5. 時限只有 30 秒  

----

因為是完全 random ，直接硬玩一般來說是不可能贏的了 (當然我不敢說完全不可能贏)。  
但是可以注意到 seed 為 `time(NULL)`，那同時解掉 sha1 的玩家，程式有極大的機率在同一秒 call `time()` ，使得 seed 一樣，後面電腦的出拳就會都是一樣的。  

因此，初步想法是直接開 21 個 socket，如果能讓這 21 個連線都壓在同一秒 call time()，那就可以透過試誤法逐漸知道電腦的出拳 pattern，最差情況就是每次都猜輸或平手，犧牲掉一個連線可以前進一關，在第 21 次就篤定可以贏了。  

初步嘗試之後發現，依序解 21 個第一關基本上會浪費過多時間，雖然第一關可以在 30 秒內跑完，但是後面猜拳部分通常會跑不完。  
所以這裡算第一關部分改為 21 組平行運算，就可以壓到極低的時間內算完。  
另外，就算前面都很快算完，也不見得可以剛好壓在同一秒 call `time()`，如果剛好有一部分壓到下一秒，那輪到那個連線時就會失敗了，不過這只是小問題，多試幾次就可以成功了。  

最後得到 flag 為 `CTF{rooooooooock, you are so lucky!}`
