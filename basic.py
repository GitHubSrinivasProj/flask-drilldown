from flask import Flask

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return"Hello World!"

@app.route('/information') #127.0.01:5000/information
def info():
    return "<h1>Puppies are cute</h1>"


#dynamic routing
@app.route('/Dynamic/<name>')
def dynamic_create(name):
    return "{} has created a dynamic routing page".format(name[100])


if __name__ == '__main__':
    app.run(debug=False)
