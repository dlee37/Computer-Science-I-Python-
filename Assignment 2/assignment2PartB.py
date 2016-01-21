##Daniel Lee
##CSCI 1101 section 1

def calculateDayOfYear(month, day, year):
    ##returns the value of the day of the week
    
    ##commented print statements were used while
    ##debugging
    
    adjustMonth = ((month + 9)%12) + 4
    ##print(adjustMonth)
    adjustYear = year - adjustMonth//14
    ##print(adjustYear)
    century = adjustYear//100
    ##print(century)
    centYear = adjustYear % 100
    ##print(centYear)
    monthCorrect = (adjustMonth * 26) // 10
    ##print(monthCorrect)
    addedValue = day + monthCorrect + centYear + (centYear // 4) + (century//4) + (5 * century)
    ##print(addedValue)
    dayOfWeek = (addedValue + 6) % 7
    return dayOfWeek

def convertNumberCodeToDay(dayOfWeek):

    ##converts the number to the day of the week it corresponds to
    if (dayOfWeek == 0):
        return "Sunday"
    elif (dayOfWeek == 1):
        return "Monday"
    elif (dayOfWeek == 2):
        return "Tuesday"
    elif (dayOfWeek == 3):
        return "Wednesday"
    elif (dayOfWeek == 4):
        return "Thursday"
    elif (dayOfWeek == 5):
        return "Friday"
    elif (dayOfWeek == 6):
        return "Saturday"
    
def main():
##asks the user for the specific date of their 
##birth and then prints out what day of the week 
##that they were born on

    month = int(input("What month were you born in? (1-12) "))
    day = int(input("What day were you born on (1-31)? "))
    year = int(input("What year were you born on? (full year) "))
    
    ##invoke your previous function
    result = calculateDayOfYear(month, day, year)
    dayResult = convertNumberCodeToDay(result)
    
    ##now print out the value of your previous
    ##function
    print("Day of the week is: %s" % (dayResult))
