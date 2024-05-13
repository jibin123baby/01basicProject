alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
'''
    This function is used to Encrypt or Decrypt text based on
    a length specified by User
    If text is a, and shift is 2, then output will be c (a=1, 1+2 = 3, which is c)
'''
def encode_decode(text1, shift1, direction1):
    output_text = ""
    if direction1 == 'decode':
        shift1 = -1 * shift1
    for i in text1:
        '''
            Only Encrypt or Decrypt alphabets, Skips the other characters
            such as Special characters and numbers
        '''
        if i in alphabet:

            i = alphabet[alphabet.index(i) + shift1]
            output_text = output_text + i
        else:
            output_text += i
    print(f"{direction1}d Text is {output_text}")


isContinue = True
while isContinue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:  # Added for big shift number to properly work
        shift = shift % 26
    encode_decode(text, shift, direction)
    choice = (input("Do you want to Continue\n1. Yes\n2. No")).lower()
    if choice == '1' or choice == 'yes':
        isContinue = True
    else:
        isContinue = False
        print("Good Bye")
