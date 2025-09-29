import random
import string


#encryption
def encryption(chars, key):
    plain_text = input("Message to encrypt: ")
    ciper_text = ""

    for letter in plain_text:
        index =chars.index(letter)
        ciper_text += key[index]
    print(f"Your encoded message is: {ciper_text}")


#decrytion
def decryption(chars,key):
    encoded_message = input("let's decode your message! Enter your encryption code: ")
    plan_text = ""

    for letter in encoded_message:
        index =key.index(letter)
        plan_text += chars[index]
    print(f"Your encoded message is: {plan_text}")


def main():
    chars = ' ' + string.digits + string.ascii_letters + string.punctuation
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    #print(f"Chars: {chars}")
    #print(f"Key:   {key}")
    encryption(chars, key)
    decryption(chars, key)



if __name__ == '__main__':
    main()