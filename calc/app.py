# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_nums():
    """ Add numbers """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(add(a,b))


@app.route("/sub")
def sub_nums():
    """ Subtract numbers """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(sub(a,b))



@app.route("/mult")
def mult_nums():
    """ Multiply numbers """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(mult(a,b))



@app.route("div")
def div_nums():
    """ Divide numbers """
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    
    return str(div(a,b))

  