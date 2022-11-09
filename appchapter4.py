from flask import Flask, jsonify, request

app = Flask(__name__)
#curl -X GET "http://127.0.0.1:5000/tstchapter4?name=David"

@app.get("/tstchapter4")
def index ():
    name = request.args.get( "name" )
    if not name:
        return jsonify({ "status" : "error" })
    response = { "data" : f"Hello, {name} !" }
    return jsonify(response)