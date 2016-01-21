##Daniel Lee
##CSCI section 1

from Myro import *

def menu():

    answer = askQuestion("choose 1", ["Red and Green","Monochrome","Stich","Mirror","Emboss Effect","Nothing, I wish to quit"])
    if (answer == "Red and Green"):
        answer = 1
    elif (answer == "Monochrome"):
        answer = 2
    elif (answer == "Stich"):
        answer = 3
    elif (answer == "Mirror"):
        answer = 4
    elif (answer == "Emboss Effect"):
        answer = 5
    elif (answer == "Nothing, I wish to quit"):
        answer = 6
    return answer
    
def grayscaleImage(oldPic):

    W = getWidth(oldPic)
    H = getHeight(oldPic)

    print("the width of the picture is " + str(W))
    print("the height of the picture is " + str(H))

    # create the grayscale image
    newPic = makePicture(W, H)
    for x in range(0,W):
        for y in range(0,H):

            pixel = getPixel(oldPic, x, y)
            redValue = getRed(pixel)
            greenValue =  getGreen(pixel)
            blueValue = getBlue(pixel)
            #grayValue = MAX(redValue,greenValue,blueValue)
            grayValue = (redValue + greenValue + blueValue)/3
            setPixel(newPic, x, y, makeColor(grayValue, grayValue, grayValue))
    return newPic

def adjustRedAndGreen(oldPic):
    w = getWidth(oldPic)
    h = getHeight(oldPic)
    print("width of photo is %d" % w)
    print("height of photo is %d" % h)
    ##newPic = copyPicture(oldPic)
    newPic = makePicture(w,h)
    ##now instensify the red and green
    for x in range(w):
        for y in range(h):
            pixel = getPixel(oldPic, x, y)
            redValue = getRed(pixel)
            greenValue =  getGreen(pixel)
            blueValue = getBlue(pixel)
            if redValue > 200:
                newRed = redValue//2
                setPixel(newPic, x, y, makeColor(newRed, greenValue, blueValue))
                if greenValue < 75:
                    newGreen = greenValue * 2
                    setPixel(newPic, x, y, makeColor(newRed, newGreen, blueValue))
            elif greenValue < 75:
                newGreen = greenValue * 2
                setPixel(newPic, x, y, makeColor(redValue, newGreen, blueValue))
            else:
                setPixel(newPic, x, y, makeColor(redValue, greenValue, blueValue))
    return newPic
    
def monochrome(oldPic):
    w = getWidth(oldPic)
    h = getHeight(oldPic)
    newPic = makePicture(w, h)
    print("width of photo is %d" % w)
    print("height of photo is %d" % h)
    for x in range(w):
        for y in range(h):
            pixel = getPixel(oldPic, x, y)
            red = getRed(pixel)
            green =  getGreen(pixel)
            blue = getBlue(pixel)
            if red + blue + green > 150:
                setPixel(newPic, x, y, makeColor(255, 255, 255))
            else:
                setPixel(newPic, x, y, makeColor(0, 0, 0))
    return newPic
    
def stitch(pic1,pic2):
    #if photos are not the same size, just returns picture2
    show(pic1, "As We Adjust")
    show(pic2, "As We Adjust")
    w1 = getWidth(pic1)
    h1 = getHeight(pic1)
    w2 = getWidth(pic2)
    h2 = getHeight(pic2)
    if w1 != w2 and h1 != h2:
        return pic2
    for x in range(w1//2):
        for y in range(h1):
            
            pix = getPixel(pic1,x,y)
            pix2 = getPixel(pic2,x,y)
            setRed(pix2, getRed(pix) )
            setGreen(pix2, getGreen(pix))
            setBlue(pix2, getBlue(pix))
            
    
def mirror(oldPic):
    width = 0
    w = getWidth(oldPic)
    h = getHeight(oldPic)
    newPic = copyPicture(oldPic)
    print("width of photo is %d" % w)
    print("height of photo is %d" % h)
    for x in range(w//2):
        for y in range(h):
            print(w)
            print(width)
            pixel = getPixel(oldPic, width, y)
            pixel2 = getPixel(newPic, w, y)
            red = getRed(pixel)
            green =  getGreen(pixel)
            blue = getBlue(pixel)
            setPixel(newPic, w, y, makeColor(red, green, blue))
        width += 1
        w -= 1
    return newPic
            

def emboss(oldPic):
    pic = grayscaleImage(oldPic)
    w = getWidth(pic)
    h = getHeight(pic)
    newPic = makePicture(w, h)
    print("width of photo is %d" % w)
    print("height of photo is %d" % h)
    for x in range(w):
        for y in range(h):
            pixel = getPixel(pic, x, y)
            pixel2 = getPixel(pic, x-1, y-1)
            totalPixelValue2 = getRed(pixel2) + getGreen(pixel2) + getBlue(pixel2)
            red = getRed(pixel)
            green = getGreen(pixel)
            blue = getBlue(pixel)
            totalPixelValue = red + green + blue
            newColor = 128 + (totalPixelValue2 - totalPixelValue)/2
            setPixel(newPic,x,y,makeColor(newColor,newColor,newColor))
    return newPic

def main():
    choice = menu()
    while choice != 6:
        
        if choice == 1:
            beforePic = makePicture(pickAFile())
            show(beforePic, "Before i see changes")
            newPic = adjustRedAndGreen(beforePic)
            show(newPic, "After Red and Green intensified")
            
        elif choice == 2:
            beforePic = makePicture(pickAFile())
            show(beforePic, "Before i see changes")
            newPic = monochrome(beforePic)
            show(newPic, "After monochrome")
            
        elif choice == 3:
            beforePic1 = makePicture(pickAFile())
            beforePic2 = makePicture(pickAFile())
            #if photos are not the same size, just returns picture2
            stitch(beforePic1, beforePic2)
            
        elif choice == 4:
            beforePic = makePicture(pickAFile())
            show(beforePic, "Before i see changes")
            newPic = mirror(beforePic)
            show(newPic, "After mirror")
            
        elif choice == 5:
            beforePic = makePicture(pickAFile())
            show(beforePic, "Before i see changes")
            newPic = emboss(beforePic)
            show(newPic, "After emboss")
            
        choice = menu()