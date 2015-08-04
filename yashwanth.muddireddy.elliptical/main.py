##########################################################
#Name: Yashwanth Reddy Muddireddy
#Class: CMPS 5363 Cryptography
#Date: 4th august 2015
#Program 3: Elliptical Curve 
##########################################################

import argparse
import sys
import elip as el
from fractions import Fraction

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", dest="a", help="Part 'a' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-b", dest="b", help="Part 'b' of elliptical curve: y^2 = x^3 + ax + b")
    parser.add_argument("-x1",dest="x1", help="")
    parser.add_argument("-y1",dest="y1", help="")
    parser.add_argument("-x2",dest="x2", help="")
    parser.add_argument("-y2",dest="y2", help="")

    args = parser.parse_args()

    

    print("a=",args.a," b=",args.b,"x1=",args.x1," y1=",args.y1," x2=",args.x2," y2=",args.y2)
    print('curveEquation: y**2=x**3 + {0}x + {1}'.format(args.a,args.b)) 
	
	#initializing variables
    a =Fraction(args.a)
    b = Fraction(args.b)
    x1 = Fraction(args.x1)
    y1 = Fraction(args.y1)
    x2 = Fraction(args.x2)
    y2 = Fraction(args.y2)
    x3 = Fraction()
    y3 = Fraction()
    el.value(x1,x2,y1,y2,a,b)
    print(Fraction(x3).limit_denominator(1000),Fraction(y3).limit_denominator(1000))
    
   
if __name__ == '__main__':
    main()
