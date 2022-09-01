alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',' ']
cipher =['K', 'C', 'P', 'S', 'V', 'M', 'H', 'F', 'D', 'B', 'U', 'W', 'Q',
         'N', 'R', 'Y', 'T', 'J', 'O', 'I', 'X', 'E', 'L', 'A', 'Z', 'G',' ']

operations = input("What do you want to do? encrypt or decrypt\n")
message = input(f"Enter your message to be {operations}ed: \n").upper()

# Converting the message to a list
convert = []
for i in message:
    convert += i.split(",")
    lenght = len(convert)
    pass



    


# function for encrpting message
def encryption():
    encrypt = []
    encrypted = ""
    for position in convert:
        key = alphabet.index(position)
        encrypt.append(cipher[key])
    return encrypted.join(encrypt)

# function for decryption

def decryption():
    decrypt = []
    decrypted = ""
    for position in convert:
        key = cipher.index(position)
        decrypt.append(alphabet[key])
    return decrypted.join(decrypt)
    
if operations == 'encrypt':
    print(f"Your encrypted message is: {encryption()}")
    
elif operations == 'decrypt':
    print(f"Your decrypted message is {decryption()}")
    
else:
    raise Exception("Operation not found: %s" % operations)