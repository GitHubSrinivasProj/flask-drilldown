#jinja templating will let us directly insert variables from
#our python code to HTML files
# the syntax for inserting a variable is
#{{some_variables}}

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name='Python'
    letters = list(name)
    pup_dict = {'pup':'sammy'}
    return render_template('template_variable.html',name=name,letters=letters
                            ,pup_dict=pup_dict)

if __name__ == '__main__':
    app.run(debug=True)
