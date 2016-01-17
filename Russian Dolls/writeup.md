# Russian Dolls (misc 100)
##### team : sblan
##### participant : 龔逸軒 (r04922019) / 廖唯辰 (r04922161)
## Description
```
Let's play a game!
nc 52.68.224.122 9020
https://www.dropbox.com/s/c5vnss4iqlfphjl/lucky?dl=0
```
## Solution
russian_dolls_v2
```
$ file russian_dolls_v2
russian_dolls_v2: Zip archive data, at least v1.0 to extract
```
```
$ mv russian_dolls_v2 russian_dolls_v2.zip
$ unzip russian_dolls_v2.zip
Archive:  russian_dolls_v2.zip
 extracting: level1
```
level 1
```
$ file level1
level1: 7-zip archive data, version 0.4
```
```
$ 7z e level1

7-Zip [64] 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18
p7zip Version 9.20 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,8 CPUs)

Processing archive: level1

Extracting  level2

Everything is Ok

Size:       885
Compressed: 859

```
level 2
```
$ file level2
level2: ASCII text, with very long lines
```
打開來看，看起來像是 base64
```
$ base64 -d level2 > level3
$ file level3
level3: gzip compressed data, was "level4", from Unix, last modified: Wed Jan  6 14:35:28 2016
```
發現沒錯  
level 3
```
$ mv level3 level4.gz
$ gunzip level4.gz
```
level 4
```
$ file level4
level4: bzip2 compressed data, block size = 900k
```
```
$ mv level4 level5.bz2
$ bunzip2 level5.bz2
```
level 5
```
$ file level5
level5: lzip compressed data, version: 1
```
```
$ mv level5 level6.lz
$ lzip -d level6.lz
```
level 6
```
$ file level6
level6: POSIX tar archive
$ mv level6 level6.tar
$ tar -xvf level6.tar
level7
```
level 7
```
$ mv level7 level8.xz
$ xz -d level8.xz
```
level 8
```
$ file level8
level8: ASCII text
```
```
$ cat level8
# This is a shell archive.  Save it in a file, remove anything before
# this line, and then unpack it by entering "sh file".  Note, it may
# create directories; files and directories will be owned by you and
# have default permissions.
#
# This archive contains:
#
#       level9
#
echo x - level9
sed 's/^X//' >level9 << 'END-of-level9'
XPGS{Cnpxrq!Cnpxrq!Cnpxrq}
END-of-level9
exit
```
```
$ mv level8 level9.sh
$ sh level9.sh
x - level9
```
level 9
```
$ cat level9
PGS{Cnpxrq!Cnpxrq!Cnpxrq}
$ python -c 'print "PGS{Cnpxrq!Cnpxrq!Cnpxrq}".decode("rot13")'
CTF{Packed!Packed!Packed}
```
得到 flag `CTF{Packed!Packed!Packed}`
