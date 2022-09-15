from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)


"""
    Hops allows us to enter List as inputs and outputs
"""

@hops.component(
    "/listinput",
    name = "listinput",
    inputs=[
        hs.HopsInteger("List of Numbers", "V", "List of Values", hs.HopsParamAccess.LIST)
    ],
    outputs=[
       hs.HopsInteger("Mass Addition","MA","Mass Addition")
    ]
)
def listinput(numList):
    massAdd = 0
    for n in numList:
        massAdd += n

    return massAdd



@hops.component(
    "/listoutput",
    name = "listoutput",
    inputs=[
        hs.HopsString("Text to repead", "T", "A string"),
        hs.HopsInteger("Repeat", "R", "Number of times to repeat it")
    ],
    outputs=[
       hs.HopsString("Mass Addition","MA","Mass Addition", hs.HopsParamAccess.LIST)
    ]
)
def listoutput(text, repeat):
    
    repeat_list = []
    for n in range(repeat):
        repeat_list.append(text)

    return repeat_list





if __name__== "__main__":
    app.run(debug=True)