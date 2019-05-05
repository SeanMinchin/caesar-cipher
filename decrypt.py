def is_uppercase(char):
    return 65 <= ord(char) <= 90


def is_lowercase(char):
    return 97 <= ord(char) <= 122


def to_uppercase(char):
    return chr(ord(char) - 32)


encrypted_msg = input("Enter encrypted message: ")
key = input("Enter key cipher: ")

updated_key = ''
key_index = 0
for letter in encrypted_msg:
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

alpha_pos_diff = []
for enc_letter, key_letter in zip(encrypted_msg, updated_key):
    offset = (ord(enc_letter) - ord(key_letter)) % 26
    alpha_pos_diff.append(offset)

decrypted_msg = ''
for enc_letter, offset in zip(encrypted_msg, alpha_pos_diff):
    if is_uppercase(enc_letter):
        decrypted_msg += chr(65 + offset)
    elif is_lowercase(enc_letter):
        decrypted_msg += chr(97 + offset)
    else:
        decrypted_msg += enc_letter

print('Decrypted message:', decrypted_msg)
