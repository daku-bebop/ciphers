#shift using ascii 
def encrypt(plaintext, key): #shift each char with key val
    ciphertext = ""
    for char in plaintext:  #loop through each c and shift by adding key value to ascii code
            shifted = chr((ord(char)+key -ord('a'))%26 + ord('a'))    #encrypt ( add key(k) and mod by 26 for lowercase chars)
            ciphertext += shifted
    return ciphertext
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
            shifted = chr((ord(char) - key - ord('a')) % 26 + ord('a'))
            plaintext += shifted
    return plaintext

plaintext = "discombobulate"        #lowercase 
key = 19
print("encrypting plaintext: ",plaintext," with key: ",key,"\n")
ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext,key) 
print("ciphertext:           ", ciphertext)
#cipher_z26 = [(ord(c) - ord('a')) % 26 for c in ciphertext.lower() if c.isalpha()]
#print("ciphetext z26:",cipher_z26)

print("\ndecrypted plaintext:  ",decrypted_plaintext) 