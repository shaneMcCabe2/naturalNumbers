"""
This script will convert the decimal system integer to the desired number
system. For example, to convert to the septimal system, pass in 7. For binary pass
in 2. Note: current version only supports 2-10 base number systems.
"""

import numpy as np #linear algebra and matrices
import math # basic math operations

def __main__():

    # prompt for integer to convert and desired number system
    inputDecimal = int(input('Input an integer (decimal-based) to convert: '))
    inputNumSys = int(input('Input an integer (2-10) for the desired number system: '))

    # pass the inputs into the conversion function
    print(str(inputDecimal) + ' (10-based) is equivalent to ' + str(convertInteger(inputDecimal, inputNumSys)) + ' (' + str(inputNumSys) + '-based)')

# takes in the decimal based integer and converts it to the desired number system integer
def convertInteger(decimal, numSystem):

    # declare an array of remainders, this will contain our converted digits
    remainderArray = []

    # add the remainder to the end of the array
    remainderArray.append(decimal % numSystem)
    # divide the decimal integer by the desired number system integer value
    divisionNum = decimal // numSystem

    # continue until divisionNum = 0, remainderArray will contain the converted digits in reverse
    while divisionNum != 0:
        remainderArray.append(divisionNum % numSystem)
        divisionNum = divisionNum // numSystem

    # initialize our string to contain integers from remainderArray
    string = ''

    # for each integer in our array, convert to a string and combine to one string
    for i in range(len(remainderArray)):
        string += str(remainderArray[i])

    # reverse the order of our string, then convert back to an integer
    convertedInt = int(string[::-1])

    return convertedInt

if __name__ == '__main__':
    __main__()
