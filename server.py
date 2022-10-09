from flask import Flask, render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/results", methods=['post'])
def results():
    return render_template("results.html")

app.run(debug=True)