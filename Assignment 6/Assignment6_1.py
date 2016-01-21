##Daniel Lee
##CSCI 1101 section 1

import random
all_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.!?'

def make_encoder(alphabet):
    ##maps a random value to each key
    
    encoder = {}
    alphabetList = list(alphabet)
        
    for letter in alphabet:
        encoder[letter] = random.choice(alphabetList)
        alphabetList.remove(encoder[letter])
##        print(encoder)
##        print(alphabetList)

    return encoder

def encode_msg(msg,encoder):
    #make an empty msg and return it something encoded

    encoded_msg = ''
    for c in msg:
        if c == ' ':
            encoded_msg += ' '
            continue
        encoded_msg += encoder[c]

    return encoded_msg

def make_decoder(encoder):
    decoder = {v:k for k,v in encoder.items()}
    return decoder

def decode_message(encoded_msg,decoder):
    decoded_msg = ""
    for c in encoded_msg:
        if c == ' ':
            decoded_msg += ' '
            continue
        decoded_msg += decoder[c]

    return decoded_msg
