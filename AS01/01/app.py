
from flask import Flask
import ghhops_server as hs

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/createGeometry",
    name = "Create Geometry",
    inputs=[

        
        hs.HopsNumber("X coordinate", "X", "X Coordinate of circle center", hs.HopsParamAccess.ITEM, default=5),
        hs.HopsNumber("Y coordinate", "Y", "Y Coordinate of circle center", hs.HopsParamAccess.ITEM, default= 8),
        hs.HopsNumber("Radius", "R", "Radius of Circle", hs.HopsParamAccess.ITEM, default= 4),
        hs.HopsPoint("Center Point", "P", "Center point of Geo", hs.HopsParamAccess.ITEM )

    ],
    outputs=[
       
       hs.HopsCurve("WEB","WEB","Web geometry ", hs.HopsParamAccess.LIST)
       
    ]
)
def createGeometry(rX, rY, radi, center):

    point = rg.Point3d(rX,rY,0)
    

    circle = rg.Circle(point,radi)
    circle1= circle.ToNurbsCurve()
    
    circle1.Domain= rg.Interval(0,1)
    diag = []
    pts=[]
    for d in range(0,10):
        pt = circle1.PointAt(d/10)
        l = rg.LineCurve(center, pt)
        l.ToNurbsCurve()
        l.Domain= rg.Interval(0,1)

        p= l.PointAt(0.5)
        pts.append(p)

        diag.append(l)
       
    conn = rg.Curve.CreateControlPointCurve(pts,1)
    conn.SetEndPoint(pts[0])
    diag.append(conn)
   
    return  diag,

if __name__== "__main__":
    app.run(debug=True)