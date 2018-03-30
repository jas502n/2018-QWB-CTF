#encoding:utf8

def read_key_origin():
    fin=open("key","rb")
    res = fin.read()
    fin.close()
    return res
    
key = read_key_origin()
    
def crack(flag):
    assert flag.startswith("flag{")
    assert flag.endswith("}")
    assert len(flag)==27

    global key
    def lfsr(R,mask):
        output = (R << 1) & 0xffffff
        i=(R&mask)&0xffffff
        lastbit=0
        while i!=0:
            lastbit^=(i&1)
            i=i>>1
        output^=lastbit
        return (output,lastbit)



    R=int(flag[5:-1],2)
    mask    =   0x100002

    s=""
    for i in range(12):
        tmp=0
        for j in range(8):
            (R,out)=lfsr(R,mask)
            tmp=(tmp << 1)^out
        s+=chr(tmp)
        
    if s==key:
        print(flag)
        exit()
        

def enum():
    def _enum(s,dep):
        if 21==dep:
            print(s)
            flag = "flag{"+s+"}"
            crack(flag)
            return
            
        for bit in "01":
            _enum(s+bit,dep+1)
            
    _enum("",0)
    
def main():
    #flag{1110101100001101011}
    enum()
    
    
if '__main__'==__name__:
    main()
    