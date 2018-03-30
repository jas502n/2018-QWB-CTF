from flag import flag
assert flag.startswith("flag{")
# 作用：判断字符串是否以指定字符或子字符串开头flag{
assert flag.endswith("}")
# 作用：判断字符串是否以指定字符或子字符串结尾}，flag{}，6个字节
assert len(flag)==25
# flag的长度为25字节，25-6=19个字节
#3<<2可以这么算，bin(3)=0b11向左移动2位变成1100，0b1100=12(十进制)
def lfsr(R,mask):
    output = (R << 1) & 0xffffff    #将R向左移动1位，bin(0xffffff)='0b111111111111111111111111'=0xffffff的二进制补码
    i=(R&mask)&0xffffff             #按位与运算符&：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
    lastbit=0
    while i!=0:
        lastbit^=(i&1)    #按位异或运算符：当两对应的二进位相异时，结果为1
        i=i>>1
    output^=lastbit
    return (output,lastbit)



R=int(flag[5:-1],2)
mask    =   0b1010011000100011100

f=open("key","ab")   #以二进制追加模式打开
for i in range(12):
    tmp=0
    for j in range(8):
        (R,out)=lfsr(R,mask)
        tmp=(tmp << 1)^out   #按位异或运算符：当两对应的二进位相异时，结果为1
    f.write(chr(tmp))  #chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
f.close()