##Daniel Lee
##CSCI 1101 Section 1

def match(text, matchText):

    ##searches for a string inside of a texts and checks to see if
    ##the string is within that larger text
    placeHolder = ""
    index = 0
    if matchText == text:
        return True
    for i in range(len(text) - len(matchText) + 1):
        for c in matchText:
            if c == '?':
                placeHolder += text[i]
                i += 1
            elif c != '?':
                placeHolder += c
                i += 1
        if placeHolder == text[index:index + len(matchText)]:
            return True
        else:
            placeHolder = ""
            index += 1
        
    return False

def main():
    text = str(input("Please enter a string that you want to input here: "))
    matchText = str(input("Please enter a string that you want to find inside of the text: "))

    function = match(text, matchText)
    
    if function:
        print("The pattern %s was found in %s." % (matchText, text))
    else:
        print("The pattern %s was not found in %s." % (matchText, text))
