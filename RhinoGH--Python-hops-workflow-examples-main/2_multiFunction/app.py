from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/addition",
    name = "addition",
    inputs=[
        hs.HopsInteger("First Number", "N1", "First Value", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Second Number", "N2", "Second Value", hs.HopsParamAccess.ITEM, default= 10)

    ],
    outputs=[
       hs.HopsInteger("Sum Result","S","Result of the sum")
    ]
)
def addition(num1, num2):
    sum = num1 + num2
    return sum



@hops.component(
    "/substraction",
    name = "substraction",
    inputs=[
        hs.HopsInteger("First Number", "N1", "First Value", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Second Number", "N2", "Second Value", hs.HopsParamAccess.ITEM, default= 10)

    ],
    outputs=[
       hs.HopsInteger("Sub Result","S","Result of the substraction")
    ]
)
def substraction(num1, num2):
    sub = num1 - num2
    return sub



@hops.component(
    "/multiplication",
    name = "multiplication",
    inputs=[
        hs.HopsInteger("First Number", "N1", "First Value", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Second Number", "N2", "Second Value", hs.HopsParamAccess.ITEM, default= 10)

    ],
    outputs=[
       hs.HopsInteger("Mult Result","M","Result of the multiplication")
    ]
)
def multiplication(num1, num2):
    mult = num1 * num2
    return mult





if __name__== "__main__":
    app.run(debug=True)