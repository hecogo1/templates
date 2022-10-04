from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

# To run in terminal
# $ FLASK_APP=api_code/hello.py flask run  