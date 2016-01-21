from Myro import *
from Graphics import *

def square():
    penDown()
    for i in range(4):
        forward(1,1)
        turnBy(90,"deg")
    penUp()
        
def setUpSimWorld1():
    width, height = 500, 500,
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

def main():
    setUpSimWorld1()
    setForwardness("fluke-forward")
    square()