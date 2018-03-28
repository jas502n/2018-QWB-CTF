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