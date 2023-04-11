#affine using asccii lowercase (repurposed) 
def encrypt_affine(plaintext, a, b):                              #((a*m)+bmod26)
    ciphertext_list = []
    for letter in plaintext:
        num = ord(letter)                       #ascii val for each
        num = (a * (num - ord('a')) + b) % 26   #apply encryption
        ciphertext_list.append(num)             #add ciphertext
    return ciphertext_list
def decrypt_affine(ciphertext, a, b):
    plaintext = ""
    a_inverse = pow(a, -1, 26) # a inverse modulo 26
    print("inverse: ",a_inverse)
    for num in ciphertext:
        num = (a_inverse * (num - b)) % 26      #apply inverse
        letter = chr(num + ord('a'))            #convert to char 
        # append the result to the plaintext
        plaintext += letter
    return plaintext
a = 21                        #coprime with mod                                           
b = 3                       
plaintext = 'skedaddle'
print("plaintext: ",plaintext)
ciphertext_z26 = encrypt_affine(plaintext, a, b)
ciphertext = ''.join([chr(block+ord('a')) for block in ciphertext_z26])
print("ciphertext: ",ciphertext)
print("ciphertext Z26: ",ciphertext_z26)

text = decrypt_affine(ciphertext_z26,a,b)
print("decrypted: " ,text)