from flask import Flask;
app=Flask("appplication")
print(__name__)
@app.route("/")
def hello():
  return "Hello World"
print(hello())
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)