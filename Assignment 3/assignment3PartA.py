#Daniel Lee
##CSCI 1101 Section 1

def match(text, matchText):

    ##searches for a string inside of a texts and checks to see if
    ##the string is within that larger text
    if matchText == text:
        return True
    for i in range(len(text) - len(matchText) + 1):
        if text[i:i+len(matchText)] == matchText:
            return True

    return False


def main():
    text = str(input("Please enter a string that you want to input here: "))
    matchText = str(input("Please enter a string that you want to find inside of text: "))
    function = match(text, matchText)

    ##check to see if the previous function was found true
    if function:
        print('"%s" was found in "%s".' % (matchText, text))
    else:
        print('"%s" was not found in "%s".' % (matchText, text))
