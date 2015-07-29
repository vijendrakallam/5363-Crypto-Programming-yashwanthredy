###############################################
# Name: Yashwanth Reddy Muddireddy
# Class: CMPS 5363 Cryptography
# Program2 - Vigenere Implementation
###############################################

import argparse
import sys
import random
import string

# Variable symbols (Global)
symbols = """!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

#############################################################################
# keywordFromSeed -
#    Works by peeling off two digits at a time, and using modulo to map it into
#    the proper range of A-Z for use as a keyword.
# Example:
#    This example spells math, and I chose values 0-25 on purpose, but
#    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
#    or any value % 26 for that matter.
#
#    seed = 12001907
#    l1   = 12001907 % 100 = 07 = H
#    seed = 12001907 // 100 = 120019
#    l2   = 120019 % 100 = 19 = T
#    seed = 120019 // 100 = 1200
#    l3   = 1200 % 100 = 0 = A
#    seed = 1200 // 100 = 12
#    l4   = 12 % 100 = 12 = M
#    seed = 12 // 100 = 0
#
# @param {int} seed - An integer value used to seed the random number generator
#                     that we will use as our keyword for vigenere
# @return {string} keyword - a string representation of the integer seed
#############################################################################

#function to generate a keyword from seed value
def keywordFromSeed(seed):
    Letters = []
    seed = int(seed)

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)

#function for building a vigenere matrix randomly	
def buildVigenere(symbols,seed):

    n = len(symbols)

    vig = [[0 for i in range(n)] for i in range(n)]
    temp = symbols
	
    for char in temp:
        random.seed(seed)
        exists = []
        for j in range(n):
            r = random.randrange(len(temp))
    
            if r not in exists:
                exists.append(r)
            
            else:
                while(r in exists):
                    r = random.randrange(len(temp))
                exists.append(r)
            while(vig[j][r] != 0):
                r = (r + 1) % n

            vig[j][r] = char
    return vig


#function for encrypting the message using the seed value	
def encrypt(message,key,seed):

    vig = buildVigenere(symbols,seed)
    Cipher = ""
    # loops that retrieve the position of key alphabet in the row and message position in column
    for i in range(len(message)-1):
        for ci in range(len(symbols)):
            if (key[ i % len(key)] == vig[0][ci]):
                column = ci
        for ri in range(len(symbols)):
            if (message[i] == vig[ri][0]):
                row= ri
					
        # empty string cipher that adds up the encrypted alphabets
        Cipher = Cipher + vig[row][column]
    return Cipher

#function for decrypting the encoded message using  the same seed value	
def decrypt(message,key,seed):

    vig = buildVigenere(symbols,seed)
    plain = ""
     # loops that retrieve the position of key alphabet in the row and encrypted message position in corresponding column
    for i in range(len(message)): 
        for ri in range(len(symbols)):
            if (key[i % len(key) ] == vig[ri][0]):
                row = ri
        for ci in range(len(symbols)):
            if ( message[i] == vig[row][ci]):
                column = ci
         # empty string plain that adds up the decrypted alphabets
        plain = plain+ vig[0][column]     
    return plain
	
def main():
    cipherMessage = encrypt(message,key,seed)
    print(cipherMessage)

    plainMessage = decrypt(cipherMessage,key,seed)
    print(plainMessage)

        
if __name__ == '__main__':
    main()


