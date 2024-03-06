from flask import Flask, request, render_template
import re

app = Flask(__name__)

con = []

@app.route('/')
def index():
    return render_template('home.html')
## form tags helps the data to go from 
##  front end to back end

@app.route('/result')
def thankyou_fun():
    regex = request.args.get('regex_exp')
    content = request.args.get('string')
    match = re.findall(regex,content)
    con.append(match)  
    
    return render_template("home.html", con=con,match=match)

if __name__ == '__main__':
    app.run(debug =True, host='0.0.0.0',port=5000)