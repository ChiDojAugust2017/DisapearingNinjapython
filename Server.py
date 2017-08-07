from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', name = "No Ninjas Here")

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route("/ninjas/<color>")
def specific_ninja(color):
    specific_color = color
    return render_template("specific_ninja.html", display_ninja=specific_color)



app.run(debug=True)