from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/say_hello',methods=['POST'])
def submit():
	name = request.form.get('name')
if __name__ == '__main__':
 app.run(debug=True)