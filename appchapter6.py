from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.get("/")
def index():
    return  render_template( "index.html" )

@app.get("/search")
def search():
    args = request.args.get( "q" )
    return redirect(f"https://google.com/search?q={args}")

if __name__ == "__main__" :
    app.run()

@app.get("/lucky")
def lucky():
    args = request.args.get( "q" )
    return redirect(f"https://www.google.com/search?q={args}&btnI=I%27m+Feeling+Lucky&source=hp&ei=TxBtY7v5GZHaz7sPuJGMqAo&iflsig=AJiK0e8AAAAAY20eX-h8AYcZd_dmzTFVVDRYGR42e5sy")

if __name__ == "__main__" :
    app.run()