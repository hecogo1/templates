from flask import Flask
import xgboost
app = Flask(__name__)

@app.route('/classify', methods = ['GET', 'POST'])
def classify(pl, pw, sl, sw):
    pl = request.args.get('pl')
    pw = request.args.get('pw')
    sl = request.args.get('sl')
    sw = request.args.get('sw')
    retultados = xgboost_classify_iris(pl, pw, sl, sw)
    return resultados

# To run in terminal
# $ FLASK_APP=api_code/hello.py flask run  

# Execute the program
# $ export FLASK_APP = api_code/clasificador.py
# $ python –m flask –un –host=0.0.0.0 –port=8080

# call to a flask service python with flask

# $ curl –data “sl=5.1&sw=3.5&pl=1.4&pw=0.3” \ ”http://modeloescalado:8080/clasifica”