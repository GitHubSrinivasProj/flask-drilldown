from flask import Flask

app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index():
    return"Hello World!"

@app.route('/puppy_latin/<name>') #127.0.0.1:5000/puppy_latin/<name>
def latin_name(name):
    name = list(name)
    if(name[len(name)-1]!='y'):
        name = ''.join(name)
        return("<h1>This is the new latin name:{}</h1>".format(name+'y'))
    else:
        name[len(name)-1:] = ['i','f','u','l']
        name = ''.join(name)
        return("<h1>This is the new latin name:{}</h1>".format(name))


if __name__ == '__main__':
    app.run(debug=False)
