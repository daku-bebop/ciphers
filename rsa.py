import math 
def text_z26(text):
    letter_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
                  'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
                  'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,
                  's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
                  'y': 24, 'z': 25}
    Z26 = ''
    for letter in text:
        Z26 += format(letter_map[letter], '02d')
   
    #blocks=[int(Z26[i:i+4]) for i in range(0,len(Z26),4)]
    
    return Z26
def z26_text(Z26):
    letter_map = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f',
                  6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l',
                  12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
                  18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x',
                  24: 'y', 25: 'z'}
    text = ''
    for i in range(0, len(Z26), 2):
        block = int(Z26[i:i+2])
        text += letter_map[block]
    return text
#give p & q, should be large (miller-rabin)
p = 283
q= 313
def generate_keypair(p,q):
    n = p * q
    pn = (p-1) * (q-1)
    e = 65537
    d = pow(e,-1,pn)
    #print(d)
    return (n,e,d) 
def rsa_encrypt(plaintext_blocks,e,n):
    encrypted_block = pow(plaintext_blocks,e,n)
    ciphertext = format(encrypted_block, '02d')
    return ciphertext

def rsa_decrypt(ciphertext_blocks, d, n):
    decrypted_block = pow(ciphertext_blocks, d, n)
    decrypted = format(decrypted_block,'02d')
    return decrypted


plaintext ='crypto'
pint = text_z26(plaintext)
plaintext_blocks = [int(pint[i:i+4]) for i in range(0,len(pint),4)]
print('plaintext:',plaintext,'  Z26:',plaintext_blocks)
(n,e,d) = generate_keypair(p,q)
ciphertext_blocks = [rsa_encrypt(block,e,n) for block in plaintext_blocks]
print("ciphertext: \t\t", ciphertext_blocks)
ciphertext=''.join(ciphertext_blocks)
cints=[int(block) for block in ciphertext_blocks]
decrypted_plaintext=[rsa_decrypt(block,d,n) for block in cints]
dint = ''.join(decrypted_plaintext)

print("decrypted Z26\t\t[",dint,"]")
#print(z26_text(21724151914))



#def rsa_encrypt(plaintext,e,n): 
 #   ciphertext = pow(int(pint),e,n)
  #  print("ciphertext: ",ciphertext)
  #  return ciphertext
#def rsa_decrypt(ciphertext,e,n): 
   #   pn=(p-1)*(q-1)
    #d=pow(e,-1, pn) 
    #print("decryption exponent:" , d) 
    #plaintext= pow(int(ciphertext), d, n)
    #print("plaintext: ",plaintext)
    #z26=str(plaintext)
    #text = ''
    #for i in range(0,len(z26),2):
    #    index = int(z26[i:i+2])
    #    text+=chr(index+ ord('a'))
    #print("text", text)
    #return text

#ciphertext = rsa_encrypt(pint,e,n)
#rsa_decrypt(ciphertext,e,n)


#rsa_decrypt(ciphertext,e,n)