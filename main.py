from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template("index.html"), 404
@app.route('/calculator')
def calc():
    return render_template("calculator.html"), 404

if __name__ == '__main__':
    app.run(port=8080)