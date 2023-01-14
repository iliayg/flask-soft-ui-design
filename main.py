from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hebrew")
def hebrew():
    return render_template("hebrew.html")

@app.route("/russian")
def russian():
    return render_template("russian.html")

@app.route("/english")
def english():
    return render_template("english.html")

if __name__ == '__main__':
    app.run(debug=True)
