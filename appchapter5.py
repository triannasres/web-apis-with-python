from flask import Flask, jsonify, request,render_template

app = Flask(__name__)
# curl -i -X GET "http://127.0.0.1:5000/tstchapter5?fname=Jason&lname=Statham"

@app.get("/")
def template():
    return  render_template( "index.html" )

@app.get("/tstchapter5")
def index():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    if not fname and not lname:
        return jsonify({ "status" : "error" })
    elif fname and not lname:
        response = { "data" : f"Hello, {fname}!" }
    elif not fname and lname:
        response = { "data" : f"Hello, Mr. {lname}!" }
    else :
        response = { "data" : f"Is your name {fname} {lname}?" }
    return jsonify(response)

if __name__ == "__main__" :
    app.run()