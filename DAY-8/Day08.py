import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text,shift_amount):
    n = 0
    text1 = ""
    final_text = ""
    for n in range(0,(len(text))):
        ind = text[n]
        text1 += text[n]
        ind2 = alphabet.index(ind)
        ind3 = ind2 + shift
        n += 1
        final_text += alphabet[ind3]
    print(final_text)

def decrypt(original_text,shift_amount):
    n = 0
    text1 = ""
    final_text = ""
    for n in range(0,(len(text))):
        ind = text[n]
        text1 += text[n]
        ind2 = alphabet.index(ind)
        ind3 = ind2 - shift
        n += 1
        final_text += alphabet[ind3]
    print(final_text)

if direction == "encode":
    encrypt(original_text = text,shift_amount = shift)
else:
    decrypt(original_text = text,shift_amount = shift)