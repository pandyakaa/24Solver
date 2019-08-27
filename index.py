from solver import solve
from flask import Flask, request
import json

app = Flask(__name__)
application = app

@app.route('/', methods=['POST'])

def index() :
    temp = request.form
    res = solve(temp['num1'],temp['num2'],temp['num3'],temp['num4'])
    res2 = []
    for i in res :
        res2.append(i)
    return(json.dumps({"result":res2}))

if __name__ == "__main__":
    app.run()