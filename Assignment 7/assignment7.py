##Daniel Lee
##CSCI 1101 Section 1

def find(aString,item):

    if item not in aString:
        return len(aString)
    elif aString[0] == item:
        return 0
    else:
        return 1+find(aString[1:],item)

def replace(text,oldsubstr,newsubstr):

    if text == '':
        return ''
    else:
        if text[:len(oldsubstr)] == oldsubstr:
            return newsubstr + replace(text[len(oldsubstr):],oldsubstr,newsubstr)
        else:
            return text[0] + replace(text[1:],oldsubstr,newsubstr)

def partialSums(numList):

    if numList == []:
        return []
    else:
        sums = [numList[0]]
        for number in partialSums(numList[1:]):
##            print(numList)
##            print(number)
            sums.append(number + numList[0])
##            print(sums)
    return sums

def countVowels(aString):

    if aString == '':
        return 0
    elif aString[0].lower() == 'a' or aString[0].lower() == 'e' or aString[0].lower() == 'i' or aString[0].lower() == 'o' or aString[0].lower() == 'u':
        return 1 + countVowels(aString[1:])
    else:
        return countVowels(aString[1:])
