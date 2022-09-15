from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

import kmeans


#KMEANS COMPONENT ---------------------
@hops.component(
    "/kmeans",
    name = "kmeans",
    inputs=[
        hs.HopsString("Vectors","V","Vectors List", hs.HopsParamAccess.LIST),
        hs.HopsInteger("number of clusters", "n", "number of clusters")

    ],
    outputs=[
        hs.HopsString("Clusters","C","List of clusters", hs.HopsParamAccess.LIST),
    ]
)
def kmeans_clustering(string_vectors, n):

    #calling means method
    clusters = kmeans.kmeansAlgorithm(string_vectors, n)

    return clusters



if __name__== "__main__":
    app.run()
