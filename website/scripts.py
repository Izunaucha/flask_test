from flask import Flask,render_template,request,session,make_response,redirect,url_for,g,flash
from models import db, User, Admin

@manager.command
def create_admin():
    usuario={"username":input("Usuario:"),
            "password":getpass("Password:"),
            "nombre":input("Nombre completo:"),
            "email":input("Email:"),
            "admin": True}
    usu=Usuarios(**usuario)
    db.session.add(usu)
    db.session.commit()