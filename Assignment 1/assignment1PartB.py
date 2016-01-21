##Daniel Lee
##CSCI 1101 section 1

def calculateKelvin(F):

##returns a value in Kelvin from Farenheit
    C = 5/9 * (F - 32)
    K = C + 273.15
    return K
    
def main():
    F = float(input("Enter the number of degrees in Farenheit: "))

##invoke your function into a variable
    result = calculateKelvin(F)
    print("The temperature in Farenheit of", F)
    print("converts to a temperature of %.2f degrees Kelvin." % (result))