
def getParity( n ):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return abs(parity)
# Driver program to test getParity()


def isError(userInput, userParity):
    realParity = getParity(userInput)
    if(realParity == userParity):
        return True
    else:
        return False
def part1():
    userInput = input("input your number")
    userParity = input("input your parity bit")
    error = isError(int(userInput), int(userParity))
    if(error == False):
        print ('error')
    else:
        print ('no error')

def part1B():
    userInput = input("input a number that will be converted to binary")
    userInput = str(bin(int(userInput))[2:].zfill(8))
    #userInput = userInput + str(getParity(int(userInput)))
    numErrors = int(input('how many errors do you want'))
    errorBinary = addError(userInput, numErrors)
    parity = getParity(int(userInput))
    eParity = getParity(int(errorBinary))

    print('normal parity =' + str(parity))
    print('error parity =' + str(eParity))


def addError(binary, n):
    newList = list(binary)
    for i in range(0,n):
        bit = int(binary[i])
        newBit = abs(~bit)
        newList[i] = str(newBit)
    return ''.join(newList)

part1B()
