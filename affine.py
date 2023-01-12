def encrypt_affine_cipher_integer(plaintext, a, b):
    ciphertext_list = []
    for letter in plaintext:
        # Get the ASCII value of the letter
        num = ord(letter)
        # Apply the affine transformation
        num = (a * (num - ord('A')) + b) % 26
        # append the result to the ciphertext
        ciphertext_list.append(num)
    return ciphertext_list

plaintext = "security"
a = 2
b = 3
ciphertext = encrypt_affine_cipher_integer(plaintext, a, b)
print(ciphertext)
