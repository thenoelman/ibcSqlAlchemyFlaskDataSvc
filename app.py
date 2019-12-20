from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#init
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/ibc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



@app.route('/', methods=['GET'])
def getStuff():
    return jsonify({'msg' : 'waddup!!!!'})

#run server
if __name__ == '__main__':
    app.run(debug=True)