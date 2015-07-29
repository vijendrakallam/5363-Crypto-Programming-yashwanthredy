###############################################
# Name: Yashwanth Reddy Muddireddy
# Class: CMPS 5363 Cryptography
# Program2 - Vigenere Implementation
###############################################

import argparse
import sys
import math
import randomized_vigenere as rv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
    parser.add_argument("-i", "--inputfile", dest="plainText", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-s", "--seed", dest = "seed",help="Integer seed")
    args = parser.parse_args()
    
    file = open(args.plainText,'r')
    message = file.read()
    seed = args.seed


    key = rv.keywordFromSeed(seed)
    print(key)

    if(args.mode == 'encrypt'):
        data = rv.encrypt(message,key,seed)
    else:
        data = rv.decrypt(message,key,seed)
        
    o = open(args.outputFile,'w')
    o.write(str(data))        

if __name__ == '__main__':
    main()
