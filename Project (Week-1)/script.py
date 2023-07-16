ablist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def chisquare(word):
    expected={"e":11,"a":7.8,"r":7.3,"i":8.6,"o":6.1,"t":6.7,"n":7.2,"s":8.7,"l":5.3,"c":4,"u":3.3,"d":3.8,"p":2.8,"m":2.7,"h":2.3,"g":3,"b":2,"f":1.4,"y":2,"w":0.91,"k":0.97,"v":1,"x":0.27,"z":0.44,"j":0.21,"q":0.19}
    for i in expected.keys():
        expected[i]=expected[i]*len(word)/100
    occ={}
    chi=0
    for i in expected.keys():
        for j in range(len(word)):
            if word[j]==i and i not in occ.keys():
                occ[i]=1
            elif word[j]==i :
                occ[i]+=1 
    for i in occ.keys():
        chi=chi+(occ[i]-expected[i])**2/expected[i]
    
    return chi

def shift_word(word, shift):
    shifted_word = ""
    
    for char in word:
            
            ascii_val = ord(char)
            if char.islower():
                shifted_ascii = (ascii_val - ord('a') + shift) % 26 + ord('a')
            else:
                shifted_ascii = (ascii_val - ord('A') + shift) % 26 + ord('A')
            shifted_word += chr(shifted_ascii)
        
    return shifted_word


cipher=input("Enter your cipher : ")
charlist={}
charindex={}
dist=[]
newcipher=""
for i in range(len(cipher)):
    if(ord(cipher[i])>96 and ord(cipher[i])<123):
        newcipher=newcipher+cipher[i]
    if(ord(cipher[i])>64 and ord(cipher[i])<91):
        newcipher=newcipher+cipher[i].lower()
    

for i in range(len(newcipher)):
    if(i+1)%3==1:
        if newcipher[i:i+3] in charlist:
            dist.append(i-charindex[newcipher[i:i+3]])
            charlist[newcipher[i:i+3]]+=1
            charindex[newcipher[i:i+3]]=i
        else:
            charindex[newcipher[i:i+3]]=i
            charlist[newcipher[i:i+3]]=1
    

maxv=0
maxit=0
for i in range(5,16):
    curv=0
    for j in range(len(dist)):
        if dist[j]%i==0 :
            curv+=1
    if i<14:
        if(curv>=maxv):
            maxv=curv
            maxit=i
    else:
        if(curv>maxv):
            maxv=curv
            maxit=i

shiftval=[]
j=0
c=1
for i in range(maxit):
    if j<maxit:
        shiftval.append(0)
        lchar=[]
        while j<(len(newcipher)):
            lchar.append(newcipher[j])
            j+=maxit
        # Example usage
        j=0
        chimin=200
        for k in range(26): 
            shift_value = k
            shifted_word = shift_word(lchar, shift_value)
            if(chisquare(shifted_word)<chimin):
                chimin=chisquare(shifted_word)
                if k==0:
                    k=26
                shiftval[i]=k
        j+=c
        c=c+1
str=""
for i in shiftval:
     str=str+ablist[26-int(i)]
print("The code word is : ",str)

keyword = str
string = cipher
string = string.lower()
newstr = ''
i = 0
for letter in string:
     if letter.isalpha()==False:
         newstr = newstr + letter
         continue
     newstr = newstr + ablist[(ablist.index(letter) - ablist.index(keyword[i%len(keyword)]))%26]
     i += 1
print("The decrypted text is -->")
print(newstr)