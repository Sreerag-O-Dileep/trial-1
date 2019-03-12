import flask
from flask import request

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('trial.html')

@app.route('/getfile', methods=['GET', 'POST'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
print(result)       
if __name__ == '__main__':
        app.run(host='127.0.0.1',debug=True,port=8080)