#Mohammad Moiz Adil 
#This program performs the encryption and decryption of the plaintext adi lmo or 000308 111214 through the RSA encryption system, for the public keys {n = 269959 & e = 107}
#I am having issues exporting as html
#encrypt
print("plaintext = 000308\t111214\n")
plaintext_1 = 308 #numerical equivalent of 
plaintext_2 = 111214


e = 107
n = 269959

#break in 6
ciphertext_1 = (plaintext_1**e)%n
ciphertext_2 = (plaintext_2**e)%n
#print as blocks of 6
print("===============\nfollowing are the ciphertexts in blocks of 6:\n",ciphertext_1,ciphertext_2,"\n===============\n")




#decrypt
#compute inverse of 107 modulo eulers totient for n 
def euler_totient(n): 
    result =n 
    for i in range(2,n): 
        if n %i == 0: 
            result -= result/i
    return result


print("euler's totient function of",n, "is",euler_totient(n))
n = euler_totient(n)
print("EEA\n\n")
def EEA_fast(a,b): #taken from Joshua Schneider Trafalgar E207C |1C-EEA Methods Intro to Cryptology
    s=[1,0]
    t=[0,1]
    n=1
    while(a%b)!=0: 
        n+=1
        q=a//b
        r=a%b
        s_n=s[n-2]-q*s[n-1]
        t_n=t[n-2]-q*t[n-1]
        s.append(s_n)
        t.append(t_n)
        #print(s_n,t_n)
        a=b
        b=r
    return(s[n],t[n])

EEA_fast(268920,107)
print("congruence: ", 48*(268920) -120637*(107))
inverse = -120637 + 268920
#-120637 congruent to 148283 mod 268920 
print("can see inverse as",inverse) 

#decrypt using M1 = 23557^148283 mod 269959
#decrypt using M2 = 155317^148283 mod 269959
c1= 235537 #numerical equivalent of 
c2 = 62317


e = 148283
n = 269959

#break in 6
m1 = (c1**e)%n
m2 = (c2**e)%n
#print as blocks of 6
print("===============\nfollowing are the decrypted in blocks of 6:\n",m1,m2,"\n===============")                                #i believe the error for the first block is 

