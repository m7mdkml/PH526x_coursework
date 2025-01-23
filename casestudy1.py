# casesrudy1.py by mohammed, to create a secret code cipher

import string

alphabet = " " + string.ascii_lowercase


position = {}
index = 0
for char in alphabet:
    position[char] = index
    index += 1
    
print(position['n'])

def encoding(message, key):
    encoded_message = ""
    for char in message:
        # find current position
        current = position[char]
        # shift position forward by 1, wraps around 27
        new_position = (current + key) % 27
        # adds corresponding shifted character to encoded message
        encoded_message += alphabet[new_position]
    return encoded_message

message = "hi my name is caesar"
key = 3
encoded_message = encoding(message, key)

print(encoded_message)

decoding_key = -3
decoded_message = encoding(encoded_message, decoding_key)

print(decoded_message)
