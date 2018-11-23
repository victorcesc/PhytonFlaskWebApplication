from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = 'aula de BCD - string aleatoria'

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)





@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
