from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import pymysql
pymysql.install_as_MySQLdb()
with open("config.json", 'r') as c:
    params = json.load(c)['params']

local_server = params['local_server']
app = Flask(__name__)
#mail = Mail(app)
#app.config.update(
#    MAIL_SERVER='smtp.gmail.com',
#    MAIL_PORT='465',
#    MAIL_USE_SSL='True',
#    MAIL_USERNAME=params['gmail_username'],
#    MAIL_PASSWORD=params['gmail_password']
#)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_url']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_url']



db = SQLAlchemy(app)
class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable = False)
    cmp_name = db.Column(db.String(120), nullable = False)
    mac = db.Column(db.String(20),nullable = False )
    phone_no = db.Column(db.String(20),nullable = False)
    date = db.Column(db.String(20), nullable = True )

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html', params=params)

@app.route("/about")
def about():
    return render_template('about.html', params=params)
@app.route("/post")
def post():
    return render_template('post.html', params=params)
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    """ add entry to the database"""
    if(request.method == 'POST'):
        name = request.form.get('name')
        mac = request.form.get('mac')
        phone = request.form.get('mob_num')
        cmp_name = request.form.get('cmp_name')

        entry = Contact(name=name, phone_no=phone, date=datetime.now(), mac=mac, cmp_name=cmp_name)
        db.session.add(entry)
        db.session.commit()
       # mail.send_message('new message from blog' + name, sender=email, recipients=params['gmail_username'], body= message + "\n" + phone)

    return render_template('add.html', params=params)


if __name__ == '__main__':
    app.run(debug=True)