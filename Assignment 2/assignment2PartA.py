##Daniel Lee
##CSCI 1101 section 1

def isValid(sat_math, sat_reading, sat_writing, class_rank):
    ##determines if a score is valid or not.
    
    if (sat_math < 200) or (sat_reading < 200) or (sat_writing < 200) or (class_rank < 1):
        return False
    elif (sat_math > 800) or (sat_reading > 800) or (sat_writing > 800):
        return False
    else:
        return True

def admissionStatus(sat_math, sat_reading, sat_writing, class_rank):
    ##determines if someone got accepted or 
    ##rejected from the school
    
    #determine if the scores are valid first
    if not isValid(sat_math, sat_reading, sat_writing, class_rank):
        return "Reject"
    
    #now check to see if someone got accepted or rejected if it turns true
    elif isValid(sat_math, sat_reading, sat_writing, class_rank):
        if (sat_math == 800) or (sat_reading == 800) or (sat_writing == 800):
            return "Accept"
        elif (sat_math < 300) or (sat_reading < 300) or (sat_writing < 300):
            return "Reject"
        elif ((sat_math + sat_reading + sat_writing)/3) > 650 and (class_rank <= 25):
            return "Accept"
        elif (rejected(sat_math, sat_reading, sat_writing, class_rank)):
            return "Reject"
        else:
            return "Waitlist"
        
def rejected(sat_math, sat_reading, sat_writing, class_rank):

    ##returns True or False based on if the test scores are less than 400 or in bottom quarter
    ##of graduating class
    
    if (sat_math < 400) and (sat_reading < 400) or (class_rank >= 75):
        return True
    if (sat_math < 400) and (sat_writing < 400) or (class_rank >= 75):
        return True
    if (sat_reading < 400) and (sat_writing < 400) or (class_rank >= 75):
        return True
    else:
        return False
        
def main():
    ##lets the user input their scores to determine if they got in the college or not
    
    sat_math = int(input("Please enter your SAT math score here: "))
    sat_reading = int(input("Please enter your SAT reading score here: "))
    sat_writing = int(input("Please enter your SAT writing score here: "))
    class_rank = int(input("Please enter your class rank here: "))
    
    ##a variable to determine your status
    condition = admissionStatus(sat_math, sat_reading, sat_writing, class_rank)
    print(condition)
