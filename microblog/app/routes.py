from app import webapp
from flask import render_template, url_for, request, session
import datetime

@webapp.route('/')
@webapp.route('/index')
def index():
    return "Hello, World!"

@webapp.route('/time_and_logo')
def example1():
    time = datetime.datetime.now()

    response = '''
    <html>
        <img width = "100px" src = "{}" />
        Current Date and Time: {}
    </html>'''

    return response.format(url_for('static', filename='flask_logo.png'),time)

@webapp.route('/collatz_steps/<int:n>')
def count_collatz_steps(n):
    original = n
    steps = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        steps.append(n)

    return render_template("example3.html", n=original, steps=steps)

@webapp.route('/add')
def add_two_numbers():
    if request.args.get('n1').isdigit() == False or request.args.get('n2').isdigit() == False:
        return "Error! All inputs should be of type int."
    n1 = int(request.args.get('n1'))
    n2 = int(request.args.get('n2'))

    result = n1 + n2

    return render_template("example4.html", n1=n1, n2=n2, result=result)

@webapp.route('/add_v2',methods=['GET'])
def add_two_numbers_v2_form():
    return render_template("example4_form.html")


@webapp.route('/add_v2_submit',methods=['POST'])
def add_two_numbers_v2():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')

    if n1.isdigit() == False or \
       n2.isdigit() == False:
        error = "Error! All inputs most be of type int"
        return render_template("example4_form.html", error=error)
    
    
    
    n1 = int(request.form.get('n1'))
    n2 = int(request.form.get('n2'))
    return render_template("example4.html",n1=n1, n2=n2, result=n1+n2)

@webapp.route('/add_v3',methods=['GET'])
def add_two_numbers_v3_form():
    return render_template("example4_form_v2.html")
 
webapp.secret_key = '\x80\xa9s*\x12\xc7x(\x03\xbeHJ:\x9f\xf0!\xb1a\xaa\x0f\xee'

@webapp.route('/count',methods=['GET','POST'])
def count():
    numtimes = 0
    if 'numtimes' in session:
        numtimes = session['numtimes']
    session['numtimes'] = numtimes + 1

    return render_template("example5.html",numtimes=numtimes)

if __name__ == "__main__":
    webapp.run()

