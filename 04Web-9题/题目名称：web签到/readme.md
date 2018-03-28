# Web 签到

http://39.107.33.96:10000

![](./1.jpg)

### 0x01 The Fisrt Easy Md5 Challenge

```
<!--
if($_POST['param1']!=$_POST['param2'] && md5($_POST['param1'])==md5($_POST['param2']))
{
die("success!");
}
-->
______________________________________
QNKCDZO
MD5: 0e830400451993494058024219903391

s878926199a
md5: 0e545993274517709034328855841020

_____________________________________

payload= param1=QNKCDZO&param2=s878926199a

> curl -v http://39.107.33.96:10000/ --data "param1=QNKCDZO&param2=s878926199a"
* timeout on name lookup is not supported
*   Trying 39.107.33.96...
* Connected to 39.107.33.96 (39.107.33.96) port 10000 (#0)
> POST / HTTP/1.1
> Host: 39.107.33.96:10000
> User-Agent: curl/7.46.0
> Accept: */*
> Content-Length: 33
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 33 out of 33 bytes
< HTTP/1.1 200 OK
< Date: Wed, 28 Mar 2018 06:08:37 GMT
< Server: Apache/2.4.7 (Ubuntu)
< X-Powered-By: PHP/5.5.9-1ubuntu4.20
< Set-Cookie: PHPSESSID=11aekrvs8plj1ro59o3es2mrk3; path=/
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Pragma: no-cache
< Content-Length: 61
< Content-Type: text/html
<
success!<script>alert('success!');location.href='/';</script>* Connection #0 to host 39.107.33.96 left intact


```


### 0x02 The Second Easy Md5 Challenge

```
<!--
if($_POST['param1']!==$_POST['param2'] && md5($_POST['param1'])===md5($_POST['param2']))
{
die("success!");
}
-->	

md5()函数要求接收一个字符串，若传递进去一个数组，则会返回null，即var_dump(md5(array(2))===null);值为bool(true)

payload= param1[]=0&param2[]=1

> curl -v http://39.107.33.96:10000/ --data "param1[]=0&param2[]=1"
* timeout on name lookup is not supported
*   Trying 39.107.33.96...
* Connected to 39.107.33.96 (39.107.33.96) port 10000 (#0)
> POST / HTTP/1.1
> Host: 39.107.33.96:10000
> User-Agent: curl/7.46.0
> Accept: */*
> Content-Length: 21
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 21 out of 21 bytes
< HTTP/1.1 200 OK
< Date: Wed, 28 Mar 2018 06:11:19 GMT
< Server: Apache/2.4.7 (Ubuntu)
< X-Powered-By: PHP/5.5.9-1ubuntu4.20
< Set-Cookie: PHPSESSID=9mrvbbbptvdv5lehgo8ic2q575; path=/
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Pragma: no-cache
< Content-Length: 61
< Content-Type: text/html
<
success!<script>alert('success!');location.href='/';</script>* Connection #0 to host 39.107.33.96 left intact

```

### 0x03 Md5 Revenge Now!

```
<!--
if((string)$_POST['param1']!==(string)$_POST['param2'] && md5($_POST['param1'])===md5($_POST['param2']))
{
die("success!);
}
-->	

Payload: 
param1=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2&param2=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2

> curl -v http://39.107.33.96:10000/ --data "param1=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2&param2=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2"  -H "Cookie: PHPSESSID=6596ep28sev99m6f2anj61a940"
* timeout on name lookup is not supported
*   Trying 39.107.33.96...
* Connected to 39.107.33.96 (39.107.33.96) port 10000 (#0)
> POST / HTTP/1.1
> Host: 39.107.33.96:10000
> User-Agent: curl/7.46.0
> Accept: */*
> Cookie: PHPSESSID=6596ep28sev99m6f2anj61a940
> Content-Length: 317
> Content-Type: application/x-www-form-urlencoded
>
* upload completely sent off: 317 out of 317 bytes
< HTTP/1.1 200 OK
< Date: Wed, 28 Mar 2018 06:17:49 GMT
< Server: Apache/2.4.7 (Ubuntu)
< X-Powered-By: PHP/5.5.9-1ubuntu4.20
< Expires: Thu, 19 Nov 1981 08:52:00 GMT
< Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
< Pragma: no-cache
< Content-Length: 42
< Content-Type: text/html
<
success! flag is QWB{s1gns1gns1gnaftermd5}* Connection #0 to host 39.107.33.96 left intact


```
### 0x04 Flag

#####  QWB{s1gns1gns1gnaftermd5}

#
#
### 0x05 内容转换成url编码

```
#encoding=utf-8
import urllib


file1 = open("message1.bin", "rb")
file2 = open("message2.bin", "rb")
res1 = file1.read()
res2 = file2.read()
s1 = urllib.quote(res1)
s2 = urllib.quote(res2)
file1.close()
file2.close()
print 'param1=%s'% s1 +'&'+'param2=%s'% s2

>>>param1=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2&param2=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2

```
### 0x06 md5碰撞hash值

```

> md5sum *

008ee33a9d58b51cfeb425b0959121c9 *message1.bin

008ee33a9d58b51cfeb425b0959121c9 *message2.bin

```

### 0x07 参考网站

https://www.mscs.dal.ca/~selinger/md5collision/
