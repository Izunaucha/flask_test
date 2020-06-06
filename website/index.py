from flask import Flask,render_template,request,session,make_response,redirect,url_for,g,flash
from flask_wtf import CsrfProtect
from config import DevelopmentConfig
from models import db, User, Admin
import forms
import json

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect(app)

@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['home','create','logout','cookie','inventario','about','admin'] and 'admin' not in session:
        return redirect(url_for('login'))
    else:
        if 'admin' in session and request.endpoint in ['login','admin']:
            return redirect(url_for('home'))
        elif 'username'in session and request.endpoint in ['login','create','admin']:
            return redirect(url_for('home'))

@app.route('/',methods = ['GET'])
def home():
    status=False
    if 'admin' in session:
        status=True
    return render_template('home.html', title="Malichas",status=status)

@app.route('/login',methods = ['GET','POST'])
def login():
    login_form = forms.Login_form(request.form)
    if request.method == 'POST':
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username = username).first()
        admin = Admin.query.filter_by(username = username).first()
        if admin is not None and admin.verify_password(password):
            session['admin'] = username
            return redirect(url_for('home'))
        elif user is not None and user.verify_password(password):
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('login.html', title="Ingreso",form = login_form)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    if 'admin' in session:
        session.pop('admin')
    return redirect(url_for('login'))

@app.route('/register',methods = ['GET','POST'])
def create():
    create_form = forms.Create_form(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User(create_form.username.data,
                    create_form.password.data)
        db.session.add(user)
        db.session.commit()

        redirect(url_for('login'))

    return render_template('create.html',title="Crear Usuario")

@app.route('/admin',methods = ['GET','POST'])
def admin():
    create_form = forms.Create_form(request.form)
    if request.method == 'POST' and create_form.validate():
        user = Admin(create_form.username.data,
                    create_form.password.data)
        db.session.add(user)
        db.session.commit()

        redirect(url_for('login'))

    return render_template('admin.html')

@app.route('/cookies')
def cookie():
    response = make_response(render_template('cookies.html'))
    response.set_cookie("username")
    return response

@app.route('/stock',methods = ['GET'])
@app.route('/stock/<int:page>',methods = ['GET'])
def inventario(page=1):
    status=False
    if 'admin' in session:
        status=True
    return render_template('inventario.html', title="Productos",status=status)

@app.route('/newstock',methods = ['GET','POST'])
def agregarItem():
    return render_template('newstock.html',title="Nuevo")

@app.route('/newcategory',methods = ['GET','POST'])
def newevent():
    return render_template('newcategory.html',title="Nuevo")

@app.route('/about')
def about():
    status=False
    if 'admin' in session:
        status=True
    return render_template('about.html',title="Nosotros",status=status)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
