import math

class primeNumberGenerator():

    def __init__(self, ceilingNumber):
        self.ceilingNumber = ceilingNumber
        self.currentNumber = 7
        self.counter = 0
        self.sieveOfEratosthenes = 0
        self.listPrime = []
        

    ##getters and setters
    def getCurrentNumber():
        return self.currentNumber

    def generateArray():
        return self.N

    def setNextNumber():
        if(counter == 3):
            currentNumber += 4
        else:
            currentNumber += 2

        if (currentNumber % 3 == 0):
            setNextCounter()
            setNextNumber()
        else:
            setNextCounter()

    def setNextCounter():
        if(this.counter == 3):
            counter = 0
        else:
            counter += 1

    def setInitialList():
        listPrime.append(2) 
        listPrime.append(3) 
        listPrime.append(5) 

    def isPrime(queryNumber):
        for element in listPrime :
            if not (element <= math.sqrt(queryNumber)) :
                break
            if (p%element == 0):
                return False
        return True

    def addCurrentToList(cur):
        listPrime.add(cur)

