from flask import Flask , render_template , request , redirect , url_for

'''

Building URL Dynamically
Variable Rules and URL Building
Jinja2 Template Engine

'''

app = Flask(__name__)

@app.route('/welcome') #decorator to create an URL route
def welcome(): #function to be executed when the route is accessed
    return '<html><H1> Welcome Back </H1></html>'


@app.route('/index' ,methods=['GET']) #decorator to create an URL route)
def index():
    return render_template('index.html')


@app.route('/submit',methods=['GET','POST']) #decorator to create an URL route
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name} !' 
    else:
        return render_template('form.html')
    

# Variable rule 
@app.route('/success/<score>')    # if we write <int:score> , it will only accept integer value but we do need to type cast it i.e. variable rule  
def success(score):
    return f'The score u got is  {score} !'



# to pass it to html page 
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

'''

{{  }}  -> exprssion to print output in html
{%  %}  -> expression to write control statements in html , loops 
{#  #}  -> expression to write comments in html

'''

@app.route('/success_story/<int:score>')
def success_story(score):
    res = ""
    if(score>50):
        res = "Pass"
    else:
        res = "Fail"

    exp = {'score':score , 'res': res}

    return render_template('success_story.html',results = exp)


# If condition
@app.route('/if/<int:score>')
def if_condition(score):
    return render_template('if.html',score = score)


# url_for() function ->  dynamically building a URL for a specific function

@app.route('/fail')
def fail():
    return 'You have failed !'

@app.route('/pass')
def pass_():
    return 'You have passed !'

@app.route('/result/<int:score>')
def result(score):
    if score<50:
        return redirect(url_for('fail'))
    else:
        return redirect(url_for('pass_'))
    






# entry file for any code
if __name__ == "__main__":
    app.run(debug=True) # When refresh , it will adopt the changes automatically 

