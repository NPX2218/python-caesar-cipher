##############################
# FUNCTION: ENCRYPY_DECRYPT
##############################

def encrypt_decrypt(plain_text, choice, key):
    cipher_text = ""
    alphabets = "abcdefghijklmnopqrstuvwxyz"

    for character in plain_text:
        if character in alphabets:
            original_position = alphabets.find(character)
            if choice == 'decrypt':
                new_pos = (original_position - key) % 26
            elif choice == 'encrypt':
                new_pos = (original_position + key) % 26

            new_char = alphabets[new_pos]
            cipher_text += new_char
        else:
            cipher_text = cipher_text + character
    return cipher_text

##############################
# FUNCTION: MAIN
##############################


def main():
    text = str(input('Please enter a text to encrypt or decrypt: '))
    choice = str(input('Would you like to encrypt or decrypt (e/d): ')).lower()
    key = int(input('Please enter a key (a number): '))
    if choice == 'd':
        print(f"""
        Text converted successfully.
        From: {text}
        To: {encrypt_decrypt(text, 'decrypt', key)}
        """)

    elif choice == 'e':
        print(f"""
        Text converted successfully.
        From: {text}
        To: {encrypt_decrypt(text, 'encrypt', key)}
        """)

##############################
# FUNCTION: CHECK
##############################


if __name__ == '__main__':
    main()
