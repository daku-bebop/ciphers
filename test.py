#converts integer string to text string
#using 2-digit blocks
def Z26_text(Z26):
    
    letters='abcdefghijklmnopqrstuvwxyz'
    
    text=''
    for i in range(0,len(Z26),2):
        text+=letters[int(Z26[i:i+2])]
        
    return(text)
print(Z26_text('021724151914'))