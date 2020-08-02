from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ques1.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/ques", methods=["POST", "GET"])
def ques1():
    if request.method == "POST":
        u_ans = request.form["val"]
        return redirect(url_for("user", name=u_ans))
    else:
	return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
    # Defining the home page of our site
