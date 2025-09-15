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

def message_encoder(s = str(input("Enter a message: "))):

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
    
print(message_encoder())
