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
    robot.setPose(40,750,0)

def pentagram(): #this is an example
    penDown()
    for i in range (0, 5):
        forward (1, 3)
        turnBy(180-108,"deg") #each angle of pentagon is 108 deg
    penUp()
    
def part1():
    setUpSimWorld1()
    setForwardness("fluke-forward")
    pentagram()  #this is an example, replace it with your code for a star

def part2():
    setUpSimWorld2()
    setForwardness("fluke-forward")
    """
    you can fill in the rest
    """
