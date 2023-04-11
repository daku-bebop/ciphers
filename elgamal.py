#Elgamal cs 
import random
plaintext = 7915

def generate_keys(p, g, x):
    y = pow(g, x, p)
    return y

p = 7919
g = 11                                      
x = 345                                       #secret
y = generate_keys(p, g, x)

def encrypt(plaintext, p, g, y):
    k = random.randint(1, p - 1)                        #constant plaintext results in different ciphertext on each encryption
    print("encrypting with k = ", k ) 
    c1 = pow(g, k, p)
    c2 = (pow(y, k, p) * plaintext) % p              #c2 = product of public y raised to k mod p %p to make sure within range. w.out mod p plaintext.can still decrpt. 
    return (c1, c2)

def decrypt(ciphertext, p, x):
    c1, c2 = ciphertext
    plaintext = (c2 * pow(c1, p-1-x, p)) % p        #FLT depending on c1 causes valueerr
    return plaintext


print("Public key (p, g, y):", p, g, y,"and secret key (x): ",x)

print("Plaintext:", plaintext)
ciphertext = encrypt(plaintext, p, g, y)
print("Ciphertext:", ciphertext)
decrypted_plaintext = decrypt(ciphertext, p, x)
print("Decrypted plaintext:", decrypted_plaintext)
