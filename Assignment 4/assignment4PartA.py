##Daniel Lee
##CSCI 1101 section 1

def if2x2Matrix(aList):

    if len(aList[0]) != 2 or len(aList[1]) != 2:
        return False
    else:
        return True

def findDeterminant(aList):

    ##returns the determinant of a 2x2 matrix in hand
##    print(if2x2Matrix(aList))
##    print(len(aList[0]))
##    print(len(aList[1]))
##    print(((aList[0][0])*(aList[1][1]) - (aList[0][1])*(aList[1][0])))
    return ((aList[0][0])*(aList[1][1]) - (aList[0][1])*(aList[1][0]))

def main():
    firstRow = input("Enter the first row, separate with commas (do not add spaces): ")
    secondRow = input("Enter the second row, separate with commas(do not add spaces): ")
    row1 = firstRow.split(',')
##    print(row1)
    row2 = secondRow.split(',')
##    print(row2)
    row1 = [int(i) for i in row1]
##    print(row1)
    row2 = [int(i) for i in row2]
##    print(row2)
    aList = [row1,row2]
##    print(len(aList))
##    print(aList)
    
    ##use the above function to calculate the determinant
    determinant = findDeterminant(aList)
    matrix = if2x2Matrix(aList)
    if not matrix:
        print("The determinant cannot be found!")
    else:
        print("The determinant of the matrix is %s." % determinant)

