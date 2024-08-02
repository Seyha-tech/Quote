from flask import Flask,render_template,request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Pos%40123@localhost:5432/Flask_Project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class favquote(db.Model):
     id= db.Column(db.Integer,primary_key=True)
     author= db.Column(db.String(30))
     quote= db.Column(db.String(400))

@app.route('/')
def index():
    result=favquote.query.all()
    return render_template('index.html',result=result)

@app.route('/quote')
def quote():
     return render_template('quote.html')

@app.route('/process',methods=['POST'])
def process():
    author=request.form['author']
    quote=request.form['quote']
    quotedata=favquote(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/login')
def login():
     return render_template('login.html')
@app.route('/register')
def register():
     return render_template('register.html')
