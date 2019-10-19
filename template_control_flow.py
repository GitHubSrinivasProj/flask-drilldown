# how to use forloops and if statements and send it to the HTML files using jinja templating
# by using a specific syntax shown below
# {%%} write the for loop in between the % symbols
# <ul>
#    {%for item in mylist%}
#    <li>{{item}}</li>
#    {%endfor%}
#</ul>

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_logged_in = False
    return render_template('template_control_flow.html',user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)
