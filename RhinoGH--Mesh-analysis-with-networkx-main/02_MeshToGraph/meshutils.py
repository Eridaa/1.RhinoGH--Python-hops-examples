import rhino3dm as rg
import networkx as nx


def getAdjancentFaceList(mesh):
    sets = []

    for i in range(mesh.Faces.Count):
        sets.append( set(mesh.Faces[i]) )
        
    allAdj = []

    for i in range(len(sets)):
        adj = []
        for j in range(len(sets)):
            if sets[i] is not sets[j]:
                inter = sets[i].intersection( sets[j])
                if len(inter) ==2:
                    adj.append(j) 
        allAdj.append(adj)
    return allAdj      


def getAdjancentFaces(mesh, MeshFaceIndex):
    sets = []

    for i in range(mesh.Faces.Count):
        sets.append( set(mesh.Faces[i]) )
        
    adj  = []

    for i in range(len(sets)):
        if sets[MeshFaceIndex] is not sets[i]:
            inter = sets[i].intersection(sets[MeshFaceIndex])
            if len(inter) ==2:
                adj.append(i) 

    return adj    

