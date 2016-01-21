##Daniel Lee
##CSCI 1101 section 1

##use a global variable to hold data
database = []
time = []

def fred(task):
    database.append(task)
    prettyPrint(database)
    askToDelete()
    askToPrintTask()
    while True:
        answer = input("Do you want to add another task? ")
        if answer == 'Yes' or answer == 'yes':
            main()
            break
        elif answer == 'No' or answer == 'no':
            prettyPrint(database)
            break

def isValidTime(hour,minute):
    if hour < 0 or hour > 24:
        return False
    elif minute < 0 or minute > 60:
        return False
    if hour == 24 and minute > 0:
        return False
    return True

def checkValidDate(month,day):
    if day > 31 or day < 1:
        return False
    elif month > 12 or month < 1:
        return False
    elif month == 2 and day > 28: ##does not include leap year
        return False
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        if day > 30:
            return False
    return True
    
def checkSameDate(specificDate):
    if len(time) > 0:
        for i in range(len(time)-1):
            if time[i][0] == specificDate:
                return True
    return False

def addToTime(specificDay,minutesConvert,length):
    time.append([specificDay,minutesConvert,length])
    ##print(time) ##used for debug
        
def ifAvailable():
    x = 0
    y = len(time) - 1
    while x < len(time) - 1:
##        print(time[x][1] + time[x][2])
##        print(time[y][1] + time[y][2])
        if time[x][1] == time[y][1]:
            return False
        elif time[x][1] + time[x][2] >= time[y][1] + time[y][2] and time[y][1] + time[y][2] > time[x][1]:
            time.pop(y)
            ##print('why')
            return False
        elif time[x][1] + time[x][2] > time[y][1] and time[x][1] < time[y][1]:
##            print(time[x][1] + time[x][2] > time[y][1])
##            print(time[x][1] < time[y][1])
            ##print('how')
            time.pop(y)
            return False
        else:
            x += 1
    return True
        

def askToPrintTask():
    while True:
        answer = input("Do you want to print a list of tasks for a date? ")
        if answer == 'Yes' or answer == 'yes':
            ask = input("What date do you want to print out? ")
            printTask(ask)
        elif answer == 'no' or answer == 'No':
            break
        
def printTask(date):
    for i in range(len(database)):
        if date == database[i][1]:
            print(database[i])

def askToDelete():
    while True:
        a = input("Do you want to delete a task? ")
        if a == 'yes' or a == 'Yes':
            b = input("What task do you want to delete? ")
            delTask(b)
        elif a == 'No' or a == 'no':
            break

def delTask(task):
    i = 0
    while i < len(database) - 1:
        if task == database[i][0]:
            database.pop(i)
            i += 1
        else:
            i += 1
    prettyPrint(database)

def prettyPrint(database):
    for r in database:
        row = r
        for c in row:
            print(c,"\t",end="")
        print()
    
def main():
    taskName = input("Enter the name of the task here: ")
    month = int(input("Enter the month that the task will be done (1-12): "))
    day = int(input("Enter the day the task will be done here (1-31): "))
    if not checkValidDate(month,day):
        print('This is not a valid day!')
        main()
        return
    hour = int(input("Enter the hour that the task will be done (0-24): "))
    minute = int(input("Enter the minute that the task will be done (0-59): "))
    if not isValidTime(hour,minute):
        print("This is not a valid time!")
        main()
        return
    
    length = float(input("Enter how long you think the task will take (in minutes): "))
    
    specificDay = '%d/%d' % (month,day)
    if minute < 10 and minute > 0:
        startTime = '%d:0%d' % (hour,minute)
    elif minute >= 10 and minute < 60:
        startTime = '%d:%d' % (hour,minute)

    minutesConvert = (60 * hour) + minute
    timeOfTask = minutesConvert + length
    addToTime(specificDay,minutesConvert,length)
    checkSameDate(specificDay)
    if checkSameDate(specificDay):
        if not ifAvailable():
            print('This does not fit in your schedule!')
            main()
            return
    description = input("Enter a general description of the task: ")
    task = [taskName, specificDay, startTime, length, description]
       
    ##call fred so the database works, fred does everything else
    schedule = fred(task)
