import backend
from flask import Flask, render_template, request
import main

view = backend.view()

def convertTuple(tup):
    str =  ''.join(tup)
    return str
def searching(view):
    for email in view:
     converted = convertTuple(email)
     main.send(converted)
     # print(converted)

searching(view)
app = Flask(__name__)





@app.route("/")
def index():
    return render_template("index.html")





@app.route('/sucess', methods=["POST"])
def sucess():
    email = request.form["email"]
    print(email)

    emailvalid = backend.search(email)

    if backend.searchings(emailvalid) == email:
        return render_template("index.html", text="seems like I aldready got your email")
    else:
        backend.insert(email)
        view = backend.view()
        print(f"new user {view}")
        main.send(email)

        return render_template("sucess.html")





if __name__ == "__main__":
    app.run(debug=True)
