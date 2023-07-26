from sage.all import *
def bitand(a,b):
    c= bin(int(a,2) & int(b,2))
    return str(c[2:])
def bitnot(a):
    c=""
    for i in a:
        if(i=="1"):
            c=c+"0"
        else:
            c=c+"1"
    return c
def binsum(a,b,c,d):
    sum = bin(int(a, 2) + int(b, 2) + int(c, 2) +int(d, 2))
    sum=str(sum[2:])
    return sum
def xorstring(a,b,c):
    y=int(a,2) ^ int(b,2) ^ int(c,2)
    y='{0:b}'.format(y)
    return y
def right_rotate_string(s, k):
    if not s or k == 0:
        return s

    k %= len(s)
    rotated = s[-k:] + s[:-k]
    return rotated
def right_shift_string(s, k):
    if not s or k == 0:
        return s

    k %= len(s)
    rotated=""
    for i in range(k):
        rotated=rotated+"0"
    rotated = rotated + s[:-k]
    return rotated
def str_to_bits(string):
    # Initialize empty list to store binary values
    binary_list = []
     
    # Iterate through each character in the string
    for char in string:
        # Convert character to binary, pad with leading zeroes and append to list
        binary_list.append(bin(ord(char))[2:].zfill(8))
         
    # Join the binary values in the list and return as a single string
    return ''.join(binary_list)
H_0="01101010000010011110011001100111"
H_1="10111011011001111010111010000101"
H_2="00111100011011101111001101110010"
H_3="10100101010011111111010100111010"
H_4="01010001000011100101001001111111"
H_5="10011011000001010110100010001100"
H_6="00011111100000111101100110101011"
H_7="01011011111000001100110100011001"
a=H_0
b=H_1
c=H_2
d=H_3
e=H_4
f=H_5
g=H_6
h=H_7
k=["0x428a2f98","0x71374491","0xb5c0fbcf","0xe9b5dba5","0x3956c25b","0x59f111f1","0x923f82a4","0xab1c5ed5",
"0xd807aa98","0x12835b01","0x243185be","0x550c7dc3","0x72be5d74","0x80deb1fe","0x9bdc06a7","0xc19bf174",
"0xe49b69c1","0xefbe4786","0x0fc19dc6","0x240ca1cc","0x2de92c6f","0x4a7484aa","0x5cb0a9dc","0x76f988da",
"0x983e5152","0xa831c66d","0xb00327c8","0xbf597fc7","0xc6e00bf3","0xd5a79147","0x06ca6351","0x14292967",
"0x27b70a85","0x2e1b2138","0x4d2c6dfc","0x53380d13","0x650a7354","0x766a0abb","0x81c2c92e","0x92722c85",
"0xa2bfe8a1","0xa81a664b","0xc24b8b70","0xc76c51a3","0xd192e819","0xd6990624","0xf40e3585","0x106aa070",
"0x19a4c116","0x1e376c08","0x2748774c","0x34b0bcb5","0x391c0cb3","0x4ed8aa4a","0x5b9cca4f","0x682e6ff3",
"0x748f82ee","0x78a5636f","0x84c87814","0x8cc70208","0x90befffa","0xa4506ceb","0xbef9a3f7","0xc67178f2"]
filen=input("Enter your filename(without .txt) : ")
text_file=open("{0}.txt".format(filen),"r")
sign=text_file.read()
sign_bits=str_to_bits(sign)

len_bits=len(sign_bits)

append_size=len_bits%512
if(append_size>448):
    append_size=960-append_size
elif(append_size<=448):
    append_size=448-append_size
if(append_size>=1):
    sign_bits=sign_bits+"1"
    append_size-=1
    for i in range(append_size):
        sign_bits=sign_bits+"0"

# print(len(sign_bits))

for i in range(64-len((bin(len_bits))[2:])):
    sign_bits=sign_bits+"0"
# print(bin_len)    
# print(type(bin_len))
sign_bits=sign_bits+str(bin(len_bits))[2:]
# print(sign_bits)    
# print(len(sign_bits))
findig=""
for i in range(len(sign_bits)//512):

    M=[]
    ccd=0
    for i in range(16):
        M.append(sign_bits[ccd:ccd+32])
        ccd+=32
    dump=""
    for i in range(32):
        dump=dump+"0"
    # print("hi")
    # print(len(dump))
    for i in range(48):
        M.append(dump)
    
    # w=[]
    # for i in range(64):
    #     w.append(M[i])
    for i in range(16,64):
        
        v1=right_rotate_string(M[i-15],7)
        v2=right_rotate_string(M[i-15],18)
        v3=right_shift_string(M[i-15],3)
        s0=xorstring(v1,v2,v3)
        
        v4=right_rotate_string(M[i-2],17)
        v5=right_rotate_string(M[i-2],19)
        v6=right_shift_string(M[i-2],10)
        s1=xorstring(v4,v5,v6)
        M[i]=binsum(M[i-16],s0,M[i-7],s1)[-32:]
    

    for i in range(64):
        s1=xorstring(right_rotate_string(e,6),right_rotate_string(e,11),right_rotate_string(e,25))
        ch= int(bitand(e,f),2) ^ int(bitand(bitnot(e),g),2)
        ch='{0:b}'.format(ch)
        temp1=binsum(h,s1,ch,M[i])
        kdump=str( "{0:08b}".format(int(k[i], 16)))
        temp1=str(bin(int(temp1,2) + int(kdump,2))[2:])[-32:]
        s0=xorstring(right_rotate_string(a,2),right_rotate_string(a,13),right_rotate_string(a,22))
        maj=xorstring(bitand(a,b),bitand(a,c),bitand(b,c))
        temp2=bin(int(s0,2) + int(maj,2))
        temp2=str(temp2[2:])[-32:]
        h=g
        g=f
        f=e
        e=bin(int(d,2) + int(temp1,2)) 
        e=str(e[2:])[-32:]
        d=c
        c=b
        b=a
        a=bin(int(temp1,2) + int(temp2,2))
        a=str(a[2:])[-32:]
    H_0=bin(int(H_0,2) + int(a,2)) 
    H_0=str(H_0[2:])[-32:]
    H_1=bin(int(H_1,2) + int(b,2)) 
    H_1=str(H_1[2:])[-32:]
    H_2=bin(int(H_2,2) + int(c,2)) 
    H_2=str(H_2[2:])[-32:]
    H_3=bin(int(H_3,2) + int(d,2)) 
    H_3=str(H_3[2:])[-32:]
    H_4=bin(int(H_4,2) + int(e,2)) 
    H_4=str(H_4[2:])[-32:]
    H_5=bin(int(H_5,2) + int(f,2)) 
    H_5=str(H_5[2:])[-32:]
    H_6=bin(int(H_6,2) + int(g,2)) 
    H_6=str(H_6[2:])[-32:]
    H_7=bin(int(H_7,2) + int(h,2)) 
    H_7=str(H_7[2:])[-32:]
digest= H_0 +H_1 +H_2+H_3+H_4+H_5+H_6+H_7
    # digest=int(digest,2)
    # digest=hex(digest)[2:]
findig=findig+digest
# if(len(sign_bits)==1024):

findig=int(findig,2)


N=int(input("N :"))
e=int(input("e :"))
S=input("signature :")

S=int(S,16)
S=pow(S,e,int(N))
if(S==findig):
    print("accept")
else:
    print("reject")