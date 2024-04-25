from flask import Flask, render_template,request

import os
from feature import *
from modelll import mode
PEOPLE_FOLDER = os.path.join('static', 'img')


app = Flask(__name__,static_url_path='/static')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

# def index():
#  return '<h1>Hello World!</h1>'
@app.route('/',methods=['GET'])
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    company_logo = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    return render_template("home.html", user_image = full_filename,company_logo=company_logo,csshai= "static/style.css")
    #return render_template('home.html')

@app.route('/about')
def hhome():
    return render_template('about.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

# @app.route('/user/<name>')
# def user(name):
#  return '<h1>Hello, %s!</h1>' % name

@app.route('/', methods=['POST'])
def predict():
    # l= [1,1,0,1,1,1,-1,-1,-1,-1,1,1,-1,1,0,-1,-1,-1,-1,0,1,1,1,1,1,-1,1,-1,1,0,-1]
    value = []
    # for x in request.form['urlname'].split(','):
    #     value.append(int(x)) 
    xx = featureExtraction(request.form['urlname'])
    print(xx)
    print(request.form['urlname'])
    
    objectofmodel = mode()
    print()
    o = objectofmodel.just(xx)
    # print(o[0])
    res = ''
    if(o == 1):
       res = 'This url is safe to view' 
    elif(o == -1):
        res = 'this URL  can be phishing url'
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    company_logo = os.path.join(app.config['UPLOAD_FOLDER'], '33.png')
    return render_template("home.html", user_image = full_filename,company_logo=company_logo,csshai= "static/style.css",result = res)
    # return render_template('home.html',result = res )
  
 
if __name__ == '__main__':
 app.run(debug=True)