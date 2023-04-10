def encrypt(plaintext, key): #shift each char with key val
    ciphertext = ""
    for char in plaintext: 
        if char.isalpha(): 
            shifted = chr((ord(char)+key -97)%26 + 97)
            ciphertext += shifted
        else:
            ciphertext += char
    return ciphertext

plaintext = "unsecureity"
key = 10
print("encrypting plaintext: ",plaintext," with key: ",key)
ciphertext = encrypt(plaintext, key)
cipher_z26 = [(ord(c) - ord('a')) % 26 for c in ciphertext.lower() if c.isalpha()]
print(cipher_z26)
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shifted = chr((ord(char)-key-97)%26 + 97)
            plaintext += shifted
        else:
            plaintext += char
    return plaintext
dint= decrypt(ciphertext, key) 
print(dint) 