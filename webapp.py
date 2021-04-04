from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/foundme', methods=['GET'])
def foundme():
    return "You found me!"

if __name__ == '__main__':
    app.run(debug=True)
