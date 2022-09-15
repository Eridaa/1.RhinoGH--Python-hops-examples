from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

import meshpath as mp
import meshutils as mu
import drawutils as du

#MESH WALKER COMPONENT ---------------------

#global variables for meshwalker component
walkerGraph = None
@hops.component(
    "/meshwalker",
    name = "meshwalker",
    inputs=[
        hs.HopsMesh("Input Mesh", "M", "Mesh"),
        hs.HopsBoolean("Plot", "P", "Plot", optional=True)


    ],
    outputs=[
        hs.HopsString("text","T","shortest path points"),

    ]
)
def meshToGraph(mesh, plot=False):

    G = mp.SimpleGraphFromMesh(mesh)
    print(G)
    if plot:  
        du.plotGraph(G)
        #du.plotGraphSave(G)
    
    return str(G)



if __name__== "__main__":
    app.run(debug=True)
