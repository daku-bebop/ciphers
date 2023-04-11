#Diffie-Hellman Key Exchange Protocol       
import random

p = 991
g = 6

a = random.randint(1, p-1)                    #Alice chooses secret power a and sends pow(g,a,p) to Bob 
A = pow(g, a, p)
print("Alice sends to Bob:", A)              #sends 

b = random.randint(1, p-1)
B = pow(g, b, p)                              #sends 
print("Bob sends to Alice:", B)
s1 = pow(B, a, p)                         # Alice computes s = pow(B,a,p) 

s2 = pow(A, b, p)

                                          #verify
if s1 == s2:
    s = s1
    print("Alice and Bob share the same secret encryption key:", s)
else:
    print("Error: s1 and s2 do not match.")
