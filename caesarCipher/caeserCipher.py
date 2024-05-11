alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(text1, shift1, direction1):
    #textLst = list(text1)
    ciphertxt = ""
    if direction1 == 'encode':
        for i in text1:
            #print("shift is", shift1)
            #print(alphabet[alphabet.index(i)])

            i = alphabet[alphabet.index(i) + shift1]
            ciphertxt = ciphertxt + i
    return ciphertxt

def decode(ciphertxt, shift1, direction1):
    #textLst = list(text1)
    normaltxt = ""
    if direction1 == 'decode':
        for i in ciphertxt:
            i = alphabet[alphabet.index(i) - shift1]
            normaltxt = normaltxt + i
    return normaltxt

for i in range(0,2):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'decode':
        decryptText = decode(text, shift, direction)
        print(f"Decrypted Text is {decryptText}")
    else:
        encryptText = encode(text, shift, direction)
        print(f"Encrypted Text is {encryptText}")






