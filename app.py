from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)