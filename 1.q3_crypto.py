import string

def decrypt_shift_cipher(ciphertext):
    # TRy all possible keys 
    for key in range(26):
        # Decrypt the ciphertext using  key
        plaintext = ""
        for c in ciphertext:
            plaintext_c = chr((ord(c) + key - 97) % 26 + 97)
            plaintext += plaintext_c
        
        #Print decrypted message for each key
        print("Key: ", key, "Decrypted message: ", plaintext)#when you see the word, you'll know


ciphertext = "afxg"
decrypt_shift_cipher(ciphertext)

def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    for i, c in enumerate(ciphertext):
        shift = ord(key[i % len(key)]) - ord('A')
        plain_char = chr((ord(c) - shift - ord('A')) % 26 + ord('A'))
        plaintext += plain_char
    return plaintext

ciphertext = "satktriumvxdwjjf"
key = "info"
print("\ndecrypt using keyword (info) & ciphertext (satktriumvxdwjjf)")
print(decrypt_vigenere(ciphertext, key))


