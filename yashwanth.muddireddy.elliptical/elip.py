##########################################################
#Name: Yashwanth Reddy Muddireddy
#Class: CMPS 5363 Cryptography
#Date: 4th august 2015
#Program 3: Elliptical Curve 
##########################################################
import argparse
import sys
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

#function for calculating slope and third point 
def value(x1,x2,y1,y2,a,b):
   
  
  #checking whether points lie on same curve or not
    if(y1**2==x1**3+a*x1+b and y2**2==x2**3+a*x2+b):
      print('given points lies on the curve')
      if(x1==x2):
        m=(3*x1**2+a)/(2*y2)
        x3 =(m**2-x1-x2)
        y3 =(m*(x3-x1)+y1)
	    #different points, slope and third point

        print(Fraction(x3).limit_denominator(1000),Fraction(y3).limit_denominator(1000))
        plotCoordinates = max(abs(x1),abs(x2),abs(x3),abs(y1),abs(y2),abs(y3))
        w = plotCoordinates + 5
        h = plotCoordinates + 5
        plotCurve(w,h,x1,x2,x3,y1,y2,y3,a,b,m)

      else:
        m=float(y2-y1)/float(x2-x1)
        x3 =(m**2-x1-x2)
        y3 =(m*(x3-x1)+y1)

        print(Fraction(x3).limit_denominator(1000),Fraction(y3).limit_denominator(1000))

        plotCoordinates = max(abs(x1),abs(x2),abs(x3),abs(y1),abs(y2),abs(y3))
        w = plotCoordinates + 5
        h = plotCoordinates + 5
        plotCurve(w,h,x1,x2,x3,y1,y2,y3,a,b,m)
        
    else:
      print('given points does not lies on curve')

def plotCurve(w,h,x1,x2,x3,y1,y2,y3,a,b,m):
    
    # Annotate the plot with your name using width (w) and height (h) as your reference points.
    an1 = plt.annotate("Yashwanth Reddy", xy=(-w+2 , h-2), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))

    # This creates a mesh grid with values determined by width and height (w,h)
    # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
    y, x = np.ogrid[-h:h:1000j, -w:w:1000j]

    # Plot the curve (using matplotlib's countour function)
    # This drawing function applies a "function" described in the
    # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
    # values in x and y.
    # The .ravel method turns the x and y grids into single dimensional arrays
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])

    # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
    plt.plot(x1, y1,'ro')

    # Annotate point 1
    plt.annotate('x1,y1', xy=(x1, y1), xytext=(x1+1,y1+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    plt.plot(x2, y2,'ro')

    # Annotate point 2
    plt.annotate('x2,y2', xy=(x2, y2), xytext=(x2+1,y2+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    # Use a contour plot to draw the line (in pink) connecting our point.
    plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))

    # I hard coded the third point, YOU will use good ol mathematics to find
    # the third point
    plt.plot(x3, y3,'yo')

    # Annotate point 3
    plt.annotate('x3,y3', xy=(x3, y3), xytext=(x3+1,y3+1),
            arrowprops=dict(arrowstyle="->",
            connectionstyle="arc3"),
            )

    # Show a grid background on our plot
    plt.grid()

    # Show the plot
    plt.show()

 
