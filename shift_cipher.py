def encrypt(plaintext, key): 
    ciphertext = ""
    for char in plaintext: 
        if char.isalpha(): 
            shifted = chr((ord(char)+key -97)%26 + 97)
            ciphertext += shifted
        else:
            ciphertext += char
    return ciphertext

plaintext = "security"
key = 10
ciphertext = encrypt(plaintext, key)
cipher_z26 = [(ord(c) - ord('a')) % 26 for c in ciphertext.lower() if c.isalpha()]
print(cipher_z26)
