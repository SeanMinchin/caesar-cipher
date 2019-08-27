# caesar-cipher
Python program to decrypt or encrypt a message based on a Caesar cipher key

For each letter in the decrypted string, the position of the decrypted letter in the alphabet is the difference between the encrypted letter's alphabet position and the key letter's alphabet position.

When encrypted a string, get the position of each letter in the string and add it to the position of the corresponding key letter to produce each encrypted letter.

When decrypting a string, find the difference between each decrypted letter and its corresponding key letter to get the position of each decrypted letter in the alphabet.

Uppercase and lowercase letters are treated as seperate alphabets, while special characters are ignored (not encrypted).

I got my explanation for this process from Wikipedia: https://en.wikipedia.org/wiki/Caesar_cipher
