import math

def helper_truncate( number, decimal_places=0 ):
    '''Custom made function to truncate a floating point (decimal) number to a certain number \
    of places.'''
    multiplier = 10 **decimal_places
    return math.trunc(number*multiplier) / multiplier

def load_testImage( caseIndex ):
    testCaseFilename = "testCase" + str(caseIndex) + ".txt"
    testCaseFile = open(testCaseFilename,"r")
    nTestCaseRows = int(testCaseFile.readline())

    # create the test case image.
    testCaseImage = []
    for i in range(nTestCaseRows):
        myRow = testCaseFile.readline().split()
        testCaseImage.append([float(numbers) for numbers in myRow])
    testCaseFile.close()
    return testCaseImage

def check_convolution( caseIndex, convolvedImage ):    
    # once we have the convolved image, open the check file to see.
    checkFilename = "convolved"+str(caseIndex)+".txt"
    checkFile = open( checkFilename, "r" )
    numRows = int(checkFile.readline())

    if numRows < 1:
        return False
    rowIndex = 0
    for row in convolvedImage:
        inputRow = checkFile.readline().split()
        numberRow = [helper_truncate(float(item), 4) for item in inputRow]

        for index in range(len(row)):
            if numberRow[index] != helper_truncate(row[index], 4):
                print("Convolve Test Case {}, mismatch at [{},{}]: had {}, expected {}".format(caseIndex, rowIndex, 
                                                                                               index, row[index], numberRow[index]))
                checkFile.close()
                return

        rowIndex = rowIndex + 1
    print("CONVOLVE SUCCESS for test {}".format(caseIndex))
    checkFile.close()

def check_pooling(caseIndex, pooledImage ):
    checkFilename = "maxpool"+str(caseIndex)+".txt"
    checkFile = open( checkFilename, "r" )
    numRows = int(checkFile.readline())

    if numRows < 1:
        return False
    rowIndex = 0
    for row in pooledImage:
        inputRow = checkFile.readline().split()
        numberRow = [helper_truncate(float(item), 4) for item in inputRow]

        for index in range(len(row)):
            if numberRow[index] != helper_truncate(row[index], 4):
                print("Max Pool Test Case {}, mismatch at [{},{}]: had {}, expected {}".format(caseIndex, rowIndex, 
                                                                                               index, row[index], numberRow[index]))
                checkFile.close()
                return

        rowIndex = rowIndex + 1
    print("MAXPOOL SUCCESS for test {}".format(caseIndex))
    checkFile.close()
