"""
This function takes a string as input and encodes it by moving the last n characters 
of each word to the front, where n is the position of the word in the string 
(starting from 1).

 - Input: A string containing multiple words.
 - Output: The encoded string.

Example:
 - Input: "Hello world this is a test"
 - Output: "oHell rldwo htis si a test"
"""

def message_encoder(s = str(input("\nEnter a message: "))):

    encoded_message = ""

    try:
        for pos,word in enumerate(s.split(),start=1):
            if len(word) < pos:
                encoded_message += word + " "
            else:
                encoded_message += word[-pos:] + word[:-pos] + " "
        return encoded_message.strip()
    except Exception as e:
        return str(e)

print(f"Encoded message: {message_encoder()}")

def decoder(encoded_message):
    decoded_message = ""

    try:
        for pos, word in enumerate(encoded_message.split(), start=1):
            if len(word) < pos:
                decoded_message += word + " "
            else:
                decoded_word = word[pos:] + word[:pos]
                decoded_message += decoded_word + " "
        return decoded_message.strip()
    except Exception as e:
        return str(e)

print(f"Decoded message: {decoder(message_encoder())}")