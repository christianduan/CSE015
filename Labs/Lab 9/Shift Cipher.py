def encode(t, k):
    result = ""

    for i in range(len(t)):
        char = t[i]
        if (char.isupper()):
            result += chr((ord(char) + k - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + k - 97) % 26 + 97)
        else:
            result += chr((ord(char) + k - 32) % 26 + 32)
    return result

t = input("What would you like to encode? ")
k = int(input("How much would you like to shift? "))

print ("Plain Text : " + t)
print ("Shift pattern : " + str(k))
print ("Cipher: " + encode(t, k))
print (" ")

#=============================================

def decode(t, k):
    ciphertext = input('Please enter your Encrypted sentence here: ')
    shift = int(input('Please enter its shift value: '))
    space = []
    ciphertext = ciphertext.split()
    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    sentence = ' '.join(sentence)
    print ('Decryption Successful')
    print ('Your encrypted sentence is:', sentence)

decode(t, k)