from flask import Flask,render_template


app = Flask(__name__)



@app.route('/') #1
def name():
    return "This is my first flask application"
@app.route("/home/<name>") #2
def name1(name):
    return "Hello! " + name+ " How are you?"
@app.route('/<number>') #3
def calculation(number):
    number=int(number)
    return ("{}".format(number*number))
@app.route("/hello/<int:age>") #4
def age_(age):
    age+=10
    return ("{}".format(age))
def define2():
    return "This is for the add_url_rule Testing"

app.add_url_rule("/define",'define',define2)

@app.route("/html")
def html():
    return '<html> <body> <h1> Hello How are you?</h1> </body> </html>'

@app.route('/render')
def render():
    return render_template('message.html')


if __name__=="__main__":
    app.run()