from Myro import *
from Graphics import *


def setUpSimWorld1():
    width, height = 800, 800,
    sim = Simulation("My Simulated Robot world", width, height, Color("lightgrey"))
    # Add boundaries
    sim.addWall((0, 0), (width, 10), Color("blue"))
    sim.addWall((0, 0), (10, height), Color("lightblue"))
    sim.addWall((width - 10, 0), (width, height), Color("red"))
    #sim.addWall((0, height - 10), (width, height), Color("green"))
    sim.addWall((0, height - 10), (width, height), Color("green"))
     # Start simulation loop:
    sim.setup()
    # Make a robot (save return, or use Myro.robot)
    robot = makeRobot("SimScribbler", sim)
    robot.setPose(width//2,height//2,0)

def setUpSimWorld2():
    width, height = 300, 300,
    sim = Simulation("My Simulated Robot world", width, height, Color("lightgrey"))
    # Add boundaries
    sim.addWall((0, 0), (width, 10), Color("blue"))
    sim.addWall((0, 0), (10, height), Color("lightblue"))
    sim.addWall((width - 10, 0), (width, height), Color("red"))
    #sim.addWall((0, height - 10), (width, height), Color("green"))
    sim.addWall((0, height - 10), (width, height), Color("green"))
     # Start simulation loop:
    sim.setup()
    # Make a robot (save return, or use Myro.robot)
    robot = makeRobot("SimScribbler", sim)
    robot.setPose(40,250,0)

def drawStar():
    penDown()
    for i in range(5):
        forward(1,3)
        speak("i love henry")
        turnBy(180+36,"deg")
    penUp()

def lawnMower():
    penDown()
    right = False
    while True:
        l,c,r = getObstacle()
        print(l,c,r)
        if right == False:
            if l == 0 and r == 0 and c == 0:
                stop()
                break
            if l > 6000 and r > 6000 and c > 6000:
                stop()
                break
            if c > 4500 or l > 4500:
                turnBy(90,"deg")
                forward(1,1)
                turnBy(90,"deg")
                right = True
            else:
                cruise()
                
        elif right == True:
            if l == 0 and r == 0 and c == 0:
                stop()
                break
            if l > 6000 and r > 6000 and c > 6000:
                stop()
                break
            if c > 4500 or r > 4500:
                turnBy(270,"deg")
                forward(1,1)
                turnBy(270,"deg")
                right = False
            else:
                cruise()
##         print(right)
                
def cruise():
    forward(1,1)
    return        
    
def part1():
    setUpSimWorld1()
    setForwardness("fluke-forward")
    drawStar()
    
def part2():
    setUpSimWorld2()
    setForwardness("fluke-forward")
    lawnMower()    