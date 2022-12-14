# Python program to illustrate Caesar Cipher Technique
from curses.ascii import isupper


def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

#check the above function
#       S
text = "CEASER CIPHER DEMO"
s = -5
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text,s))
#         67     57 -7
#
# print(ord('C') - 10 - 65)

# decrypt function 

def decrypt(text , s):
    result =""
    
    # traverse the cipher 
    for i in range(len(text)):
        char = text[i]
        
        # decrypt uppercase 
        if (char.isupper()):
            result += chr((ord(char) - s - 65)% 26 -65)
            
        # decrypt lowercase 
        else:
            result += chr((ord(char)-s-97) % 26 -97)
            
    return result 

