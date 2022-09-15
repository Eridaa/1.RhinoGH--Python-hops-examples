#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg

def createRandomPoints(count,rX, rY):

    randomPts = []
    for i in range(count):

        #in each itereation generate some random points
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)

        #create a point with rhino3dm
        random_pt = rg.Point3d(random_x, random_y, 0)
        
        #add point to the list
        randomPts.append(random_pt)

    return randomPts