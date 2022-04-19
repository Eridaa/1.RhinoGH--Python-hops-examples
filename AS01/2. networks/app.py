from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo
import networkx as nx

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createGraph",
    name = "Create Graph",
    inputs=[
        hs.HopsInteger("Count X", "X", "Number of node in X", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Count Y", "Y", "Number of node in Y", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0),


    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createGraph(X, Y, layout):

    G = geo.createGridGraph(X, Y)
    GW = geo.addRandomWeights(G)

    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout) 

    return nodes, edges

@hops.component(
    "/convertToNetworkX",
    name = " Convert Graph to NetworkX",
    inputs=[
        hs.HopsPoint("Nodes", "N", "List of Nodes",hs.HopsParamAccess.LIST),
        hs.HopsCurve("Edges", "E", "List of Edges", hs.HopsParamAccess.LIST),
        hs.HopsInteger("Layout", "L", "Layout to order Nodes", hs.HopsParamAccess.ITEM, default= 0)
    ],
    outputs=[
        hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
        hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)

def convertToNetworkX(nodes, edges, layout):

    G = nx.Graph()

    nd =[]

    #adding nodes
    for node in nodes:
        G.add_node(node)
        nd.append((node.X, node.Y, node.Z))

    #adding edges
    for edge in edges:
       pstart= nd.index((edge.PointAtStart.X, edge.PointAtStart.Y, edge.PointAtStart.Z))
       pend = nd.index((edge.PointAtEnd.X, edge.PointAtEnd.Y, edge.PointAtEnd.Z)) 
       G.add_edge(pstart, pend)
    
    #applying random weights and getting nodes and edges as outputs
    GW = geo.addRandomWeights(G)
    
    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout)

    return nodes, edges

if __name__== "__main__":
    app.run(debug=True)
