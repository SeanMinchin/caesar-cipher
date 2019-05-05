def is_uppercase(char):
    return 65 <= ord(char) <= 90


def is_lowercase(char):
    return 97 <= ord(char) <= 122


def to_uppercase(char):
    return chr(ord(char) - 32)


decrypted_msg = input("Enter a message to encrypt: ")
key = input("Enter key cipher: ")

updated_key = ''
key_index = 0
for letter in decrypted_msg:
    if is_uppercase(letter):
        updated_key += to_uppercase(key[key_index])
        key_index += 1
    elif is_lowercase(letter):
        updated_key += key[key_index]
        key_index += 1
    else:
        updated_key += letter
    if key_index == len(key):
        key_index = 0

alpha_pos = []
for letter in decrypted_msg:
    if is_uppercase(letter):
        alpha_pos.append(ord(letter) - 65)
    elif is_lowercase(letter):
        alpha_pos.append(ord(letter) - 97)
    else:
        alpha_pos.append(-1)

encrypted_msg = ''
for key_letter, pos in zip(updated_key, alpha_pos):
    if is_uppercase(key_letter):
        encrypted_msg += chr(((ord(key_letter) - 64 + pos) % 26) + 64)
    elif is_lowercase(key_letter):
        encrypted_msg += chr(((ord(key_letter) - 96 + pos) % 26) + 96)
    else:
        encrypted_msg += key_letter

print("Encrypted message:", encrypted_msg)
