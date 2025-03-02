from flask import Flask , render_template

'''
It creates an instance of the Flask class ,
which will be your WSGI (Web Server Gateway Interface) application.
'''

app = Flask(__name__)

@app.route('/welcome') #decorator to create an URL route
def welcome(): #function to be executed when the route is accessed
    return 'Welcome to Flask Course!'




# entry file for any code
if __name__ == "__main__":
    app.run(debug=True) # When refresh , it will adopt the changes automatically 

