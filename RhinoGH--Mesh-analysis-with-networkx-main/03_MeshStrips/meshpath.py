import networkx as nx
import rhino3dm as rg
import meshutils as mu

def SimpleGraphFromMesh(mesh):

    # Create graph
    G=nx.Graph()

    #Get the full graph
    for i in range(mesh.Faces.Count):
        
        # Add node to graph and get its neighbours
        G.add_node(i)
        neighbours = mu.getAdjancentFaces(mesh ,i)
        
        # Add edges to graph
        for n in neighbours:
            if n > i:
                G.add_edge(i,n)

    return G



def graphFromMesh(mesh,weightMode = "edgeLength"):

    # Create graph
    g=nx.Graph()
    a=mesh
    meshtype = mu.getMeshType(mesh)

    #Get the full graph
    for i in range(a.Faces.Count):

        if meshtype == "tri":    
            face_center = mu.getFaceCenterTri(a, a.Faces[i])
        elif meshtype == "quad":
             face_center =mu.getFaceCenter(a, a.Faces[i])

        
        # Add node to graph and get its neighbours
        g.add_node(i,point = face_center, face = i, isNaked = a.Faces.HasNakedEdges(i))
        neighbours = mu.getAdjancentFaces(a ,i)
        
        
        # Add edges to graph
        for n in neighbours:
            if n > i:
                p1=face_center
                if meshtype == "tri":    
                    p2=mu.getFaceCenterTri(a, a.Faces[n])
                elif meshtype == "quad":
                    p2=mu.getFaceCenter(a, a.Faces[n])
                
                line = rg.Line(p1,p2)
                if weightMode == "edgeLength":
                    w = line.Length
                elif weightMode == "sameWeight":
                    w = 1
                g.add_edge(i,n,weight=w,line=line)

    return g



def shortestPath(g, f1, f2):

    sp = nx.shortest_path(g, f1, f2, weight = "weight")
    
    pts = [g.nodes[i]["point"] for i in sp]
    faceInd = [g.nodes[i]["face"] for i in sp]

    return pts, faceInd, sp


def dijkstraPath(g, f1, f2):

    sp = nx.dijkstra_path(g, f1, f2, weight = "weight")
    
    pts = [g.nodes[i]["point"] for i in sp]
    faceInd = [g.nodes[i]["face"] for i in sp]

    return pts, faceInd, sp

def longestPath(g, f1, f2):

    sp = nx.dag_longest_path(g, f1, f2, weight = "weight")
    
    pts = [g.nodes[i]["point"] for i in sp]
    faceInd = [g.nodes[i]["face"] for i in sp]

    return pts, faceInd, sp


def burnEdgesPath(g):
    
    sp = mu.getGraphNakedNodes(g)

    pts = [g.nodes[i]["point"] for i in sp]
    faceInd = [g.nodes[i]["face"] for i in sp]

    return pts, faceInd, sp


def AllShortestPaths(g, startpoint):
    end_point_index=startpoint #for single face islands
    """Get the end point by getting the index of the point that has the longest shortest path"""

    initial_length=0 
    for i in list(g.nodes):          
        if mu.hasPath(g,startpoint,i):
            Pathlength = nx.dijkstra_path_length(g,startpoint,i,weight = "weight")
            if Pathlength>initial_length :
                initial_length=Pathlength
                end_point_index=i
                s=i
            elif Pathlength < initial_length and i!=startpoint:
                end_point_index=s


    end=end_point_index
    
    # Check that start and end are not the same node
    if startpoint == end:
        pts = [g.nodes[startpoint]["point"]]
        indexes=[startpoint]
        sl=1
        to_be_removed=[startpoint]
        return [pts,indexes,sl,to_be_removed]
        
    else:
        # Check that a path exist between the two nodes
        if mu.hasPath(g,startpoint,end):
            # Calculate shortest path
            
            sp = nx.dijkstra_path(g,startpoint,end,weight = "weight")

            # Make polyline through path
            pts = [g.nodes[i]["point"] for i in sp]
            #get points indexes 
            indexes=sp
            sl=len(sp)
            to_be_removed=sp

        
                    
        return [pts,indexes,sl,to_be_removed]



def minimun_spanning_tree(g):

    MST=nx.minimum_spanning_tree(g, algorithm='kruskal')
    
    #MB =nx.maximum_branching(MST, preserve_attrs = True)
    #MB =nx.minimum_branching(MST, preserve_attrs = True)

    ED= nx.algorithms.tree.branchings.Edmonds(MST)
    MB= ED.find_optimum(style="branching", kind= "max",preserve_attrs = True)
    #print(MB.nodes(data=True))

    S = [MB.subgraph(c).copy() for c in nx.connected_components(MB)]
    
    allnodes= [list(g.nodes) for g in S]

    return allnodes


def minimun_spanning_edges(g):

    MST=nx.minimum_spanning_tree(g, algorithm='kruskal')
    T_edges=MST.edges
    tree_lines=[]
    
    for i in T_edges:
        p1index=i[0]
        p2index=i[1]
        p1=g.nodes[p1index]["point"]
        p2=g.nodes[p2index]["point"]
        l=rg.LineCurve(p1, p2)
        tree_lines.append(l)
    
    return tree_lines


        