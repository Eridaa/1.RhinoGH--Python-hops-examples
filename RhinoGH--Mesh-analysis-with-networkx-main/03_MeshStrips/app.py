from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

import meshpath as mp
import meshutils as mu

#MESH WALKER COMPONENT ---------------------

#global variables for meshwalker component
walkerGraph = None
@hops.component(
    "/meshwalker",
    name = "meshwalker",
    inputs=[
        hs.HopsBoolean("reset","R","reset button"),
        hs.HopsMesh("Input Mesh", "M", "Mesh"),
        hs.HopsInteger("face Index 1","f1","Face index one"),
        hs.HopsInteger("face Index 2","f2","Face index two")

    ],
    outputs=[
        hs.HopsPoint("list of points","P","shortest path points", hs.HopsParamAccess.LIST),
        hs.HopsInteger("list of faces indexes","F","shortest path face indexes", hs.HopsParamAccess.LIST)
    ]
)
def meshwalker(reset, mesh, f1, f2):
    global walkerGraph

    #do something with this mesh
    if reset:
        walkerGraph = mp.graphFromMesh(mesh) #convert the mesh to a nx graph

    else:
        #use the graph to find the shortest path between two faces
        SP = mp.dijkstraPath(walkerGraph, f1, f2)
        pts = SP[0]
        faceInd = SP[1]

    return pts, faceInd




#MESH STRIPPER COMPONENT ---------------------
@hops.component(
    "/meshstripper",
    name="meshstripper",
    description=" Make a networkx graph with mesh vertices as nodes and mesh edges as edges ",
    inputs=[
        hs.HopsMesh("Mesh","M","Mesh to make networkx graph for"),
        hs.HopsString ("WeightMode ","W","Weight Mode"),
    ],
    outputs=[
        hs.HopsPoint("ShortestPath", "SP" ,"Shortest Path",hs.HopsParamAccess.LIST),
        hs.HopsString("FacesIndex", "I" ,"Faces indexes",hs.HopsParamAccess.LIST),
        hs.HopsInteger("Lengths","L","tree lengths",hs.HopsParamAccess.LIST),
    ])

def meshstripper(mesh,weightMode):

    strips=[]
    allindexes=[]
    slen=[]

    g = mp.graphFromMesh(mesh, weightMode)

    while len(g.nodes) > 0 :
        
        startpoint = mu.getStartPoint(g)
        sw = mp.AllShortestPaths(g, startpoint)   

        pathPoints = sw[0]
        pathIndexes = sw[1]
        pathLen = sw[2]
        pathNodes = sw[3]

        strips.extend(pathPoints)
        allindexes.extend(pathIndexes)
        slen.append(pathLen)
        
        g.remove_nodes_from(pathNodes)

    return strips, allindexes, slen



#MST COMPONENT ---------------------
@hops.component(
    "/mst",
    name = "mst",
    inputs=[
        hs.HopsMesh("Input Mesh", "M", "Mesh"),
        hs.HopsNumber("Weigth", "W", "Weight per face", hs.HopsParamAccess.LIST)

    ],
    outputs=[
        #hs.HopsPoint("list of points","P","shortest path points", hs.HopsParamAccess.LIST),
        #hs.HopsInteger("list of faces indexes","F","shortest path face indexes", hs.HopsParamAccess.LIST),
        hs.HopsString("list of faces indexes","F","shortest path face indexes", hs.HopsParamAccess.LIST),
        hs.HopsCurve("lines", "L", "MST Lines", hs.HopsParamAccess.LIST)
    ]
)
def mst( mesh, weights):


    mstGraph = mp.graphFromMesh(mesh) #convert the mesh to a nx graph
    
    #plot = mu.plotGraphSave(mstGraph)
    
    #if no weights define, assign random weights
    if weights == None:
        mu.addRandomWeights(mstGraph,3,10)
    else:
        mu.addWeights(mstGraph, weights)

    
    #plot graph with matplotlib
    #mu.plotGraphSave(mstGraph, 'MST_PLOT')

    #use the graph to find the shortest path between two faces
    MST = mp.minimun_spanning_tree(mstGraph)
    MST_= mu.serializeNestedList(MST)
    
    MSE = mp.minimun_spanning_edges(mstGraph)

    return MST_, MSE



if __name__== "__main__":
    app.run()
