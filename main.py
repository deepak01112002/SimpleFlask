from flask import Flask

data = {
   "1" : "hello"
}

app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello Started" 

@app.route("/post")
def post():
   return "Hello"

@app.route("/view")
def view():
   return data

@app.route("/delete/<id>")
def delete(id):
   return "Not Found Id"
if __name__ == "__main__":
   app.run(debug=True)