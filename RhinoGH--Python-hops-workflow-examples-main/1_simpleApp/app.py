from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

"""
    How to create inputs and outputs for hops.
    
    Hops Inputs should match the number of Hops inputs
    Hops Outputs should match the number of items that the functions returns 
"""


@hops.component(
    "/mycomponent",
    name = "MyComponent",
    inputs=[
        hs.HopsString("Name", "N", "Provide your name"),
        hs.HopsInteger("Age", "A", "Provide your age")
    ],
    outputs=[
       hs.HopsString("Text","T","Print name and age")
    ]
)
def printNameAndAge(name, age):
    text= "My name is {} and I am {} years old".format(name, age)
    return text



if __name__== "__main__":
    app.run(debug=True)