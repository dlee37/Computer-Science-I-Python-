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
    
def main():
##asks the user for the specific date of their 
##birth and then prints out what day of the week 
##that they were born on

    month = int(input("What month were you born in? (1-12) "))
    day = int(input("What day were you born on (1-31)? "))
    year = int(input("What year were you born on? (full year) "))
    
    ##invoke your previous function
    result = calculateDayOfYear(month, day, year)
    
    ##now print out the value of your previous
    ##function
    print("Code: 0-Sunday, 1-Monday, 2-Tuesday")
    print("3-Wednesday, 4-Thursday, 5-Friday")
    print("6-Saturday")
    print("") ##empty line to space better/look organized
    print("Day of the week is: %d" % (result))