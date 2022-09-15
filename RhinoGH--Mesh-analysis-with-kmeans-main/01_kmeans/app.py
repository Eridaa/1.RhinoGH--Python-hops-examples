from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

import kmeans


#KMEANS COMPONENT ---------------------
@hops.component(
    "/kmeans_simple",
    name = "kmeans",
    inputs=[
        hs.HopsInteger("number of clusters", "n", "number of clusters")

    ],
    outputs=[
        hs.HopsPoint("Points","P","List of points", hs.HopsParamAccess.LIST),
        hs.HopsString("Clusters","C","List of clusters", hs.HopsParamAccess.LIST)
    ]
)
def kmeans_clustering(n):

    #calling means method
    points, clusters = kmeans.kmeans(n)
    
    return points, clusters



if __name__== "__main__":
    app.run(debug=True)
