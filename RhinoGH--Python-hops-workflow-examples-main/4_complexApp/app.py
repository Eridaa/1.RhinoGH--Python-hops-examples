from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import work as wk

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/mycomponent",
    name = "MyComponent",
    inputs=[
        hs.HopsInteger("First Number", "N1", "First Value", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Second Number", "N2", "Second Value", hs.HopsParamAccess.ITEM, default= 10)

    ],
    outputs=[
       hs.HopsInteger("Sum Result","S","Result of the sum")
    ]
)
def MyComponent(num1, num2):
    op = wk.addition(num1, num2)
    return op


#be careful with cache!


if __name__== "__main__":
    app.run(debug=True)