from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# CONFIGURAZIONE DATABASE
# L'endpoint lo prendiamo dopo da AWS RDS.
# Formato: mysql+pymysql://USERNAME:PASSWORD@ENDPOINT:3306/NOMEDB
# Esempio: mysql+pymysql://admin:Pippo123@guestbook.cx...us-east-1.rds.amazonaws.com:3306/guestbook
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:LA_TUA_PASSWORD@IL_TUO_ENDPOINT_RDS:3306/guestbook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# IL MODELLO (La tabella nel DB)
class GuestMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# LE ROTTE
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Salva nel DB
        name = request.form['name']
        message = request.form['message']
        new_msg = GuestMessage(name=name, message=message)
        db.session.add(new_msg)
        db.session.commit()
        return redirect('/')
    
    # Leggi dal DB
    messages = GuestMessage.query.order_by(GuestMessage.timestamp.desc()).all()
    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    # Crea le tabelle se non esistono (magia!)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
