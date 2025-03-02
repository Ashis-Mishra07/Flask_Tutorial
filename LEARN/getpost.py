from flask import Flask , render_template , request

'''
It creates an instance of the Flask class ,
which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route('/welcome') #decorator to create an URL route
def welcome(): #function to be executed when the route is accessed
    return '<html><H1> Welcome Back </H1></html>'


@app.route('/index' ,methods=['GET']) #decorator to create an URL route)
def index():
    return render_template('index.html')


@app.route('/form',methods=['GET','POST']) #decorator to create an URL route
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name} !' 
    else:
        return render_template('form.html')


@app.route('/submit',methods=['GET','POST']) #decorator to create an URL route
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name} !' 
    else:
        return render_template('form.html')

# entry file for any code
if __name__ == "__main__":
    app.run(debug=True) # When refresh , it will adopt the changes automatically 

