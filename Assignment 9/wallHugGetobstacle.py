from Myro import *
from Graphics import *
#init("/dev/tty.IPRE6-296314-DevB")


def goAhead(): #check for wall on left and clear ahead
    left = 100
    center = 400
    right = 100
    turnBy(90,"deg") #turn left to face a wall
    ll = 0
    cc = 0
    rr = 0
    l,c,r = getObstacle()
    cc = c + cc
    l,c,r = getObstacle()
    cc = c + cc
    l,c,r = getObstacle()
    cc = c + cc
    cc = cc//3
    print(l,cc,r)
    #if (l < left and c < center and r < right): #nothing on left
    if (cc < 2400 ): #nothing on left    
        print("nothing on left, go a distance and turn left")
        turnBy(-90,"deg") #turn right face front again
        forward(1,1)
        turnBy(90,"deg") #turn left to face open space
        forward(1,1)
        return  #return nothing on left
    else :  #something on left
        print("something on left")
        turnBy(-90,"deg") #face front again
        l,c,r = getObstacle()
        l,c,r = getObstacle()
        l,c,r = getObstacle()
        print(l,c,r)
        #if (l < 5000 and c < 5000 and r < 5000): #nothing in front
        if (c < 5000): #nothing in front
           print("something on left, clear ahead")
           return  #return something on left, nothing in front, just cruise
        else:
           print("something on left, front blocked")
           turnBy(-90,"deg")
           return #somehthing ahead, turn right


def setUpSimWorld2():
    width, height = 500, 400,
    sim = Simulation("My Simulated Robot world", width, height, Color("lightgrey"))
    # Add boundaries
    sim.addWall((0, 0), (width, 10), Color("blue"))
    sim.addWall((0, 0), (10, height), Color("lightblue"))
    sim.addWall((width - 10, 0), (width, height), Color("black"))
    #sim.addWall((0, height - 10), (width, height), Color("green"))
    sim.addWall((0, height - 10), (width, height), Color("green"))
    #sim.addWall((width/2, height - 50), (width, height), Color("orange"))
    sim.addWall((width/2 + 50, height - 100), (width/2 + 120, height), Color("red"))
    # Start simulation loop:
    sim.setup()
    # Make a robot 
    robot = makeRobot("SimScribbler", sim)
    x,y = robot.getLocation()
    print (robot.getLocation())
    robot.setPose(x,y-30,0)
    print (robot.getLocation())
    #forward(-1,.5)



def setUpSimWorld3():
    width, height = 500, 400,
    sim = Simulation("My Simulated Robot world", width, height, Color("lightgrey"))
    # Add boundaries
    sim.addWall((0, 0), (width, 10), Color("blue"))
    sim.addWall((0, 0), (10, height), Color("lightblue"))
    sim.addWall((width - 10, 0), (width, height), Color("red"))
    #sim.addWall((0, height - 10), (width, height), Color("green"))
    sim.addWall((140, height - 10), (width, height), Color("green"))
     # Start simulation loop:
    sim.setup()
    # Make a robot (save return, or use Myro.robot)
    robot = makeRobot("SimScribbler", sim)
    x,y = robot.getLocation()
    print (robot.getLocation())
    robot.setPose(100,200,0)
    print (robot.getLocation())
    #forward(-1,.5)




def setUpSimWorld():
    width, height = 500, 400,
    sim = Simulation("My Simulated Robot world", width, height, Color("lightgrey"))
    # Add boundaries
    sim.addWall((0, 0), (width, 10), Color("blue"))
    sim.addWall((0, 0), (10, height), Color("lightblue"))
    sim.addWall((width - 10, 0), (width, height), Color("red"))
    #sim.addWall((0, height - 10), (width, height), Color("green"))
    sim.addWall((140, height - 10), (width, height), Color("green"))
    sim.addWall((0, height - 350), (width, height/4), Color("orange")) #250,height/2
    #sim.addWall((width/2, height - 50), (width, height), Color("orange"))
    sim.addWall((width/2 + 50, height - 100), (width/2 + 120, height), Color("black"))
    # Start simulation loop:
    sim.setup()
    # Make a robot (save return, or use Myro.robot)
    robot = makeRobot("SimScribbler", sim)
    x,y = robot.getLocation()
    print (robot.getLocation())
    robot.setPose(x,y-30,0)
    print (robot.getLocation())
    #forward(-1,.5)


def findRed():
    for i in range(20):
        p = takePicture("blob")
        show(p)
        
        turnBy(10,"deg")



def goToWall():
    turnBy(90,"deg") #turn left to face a wall
    l,c,r = getObstacle()
    while (c < 2000):
        cruise()
        l,c,r = getObstacle()
    turnBy(-90,"deg") #turn right face front again
    return    
    
def cruise():
    forward(1,.5)
    return

def main():
    setUpSimWorld3()
    setForwardness("fluke-forward")
    goToWall()
    while (True):
        goAhead()
        cruise()

#main()