from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def hello_msg():
    return "Hello Mam !!"

tasks = [
    {
        "id":1,
        "title":"Get up at 5 am",
        "description":"Teach the morning 6 am ",
        "done":False
    },
        {
        "id":2,
        "title":"Sleep at 7 am",
        "description":"sleep after teaching the 6 am for 1 Hour",
        "done":False
    },
        {
        "id":3,
        "title":"Get up at 8 am",
        "description":"Teach the coding clases agian ",
        "done":False
    },
    
]

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide JSON data"

        }, 400)
    task = {
        "id": tasks[-1]["id"]+1,
        "title": request.json["title"],
        "description": request.json.get("description",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully !!"
    })

if(__name__=="__main"):
    app.run(debug=True)