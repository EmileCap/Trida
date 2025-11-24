
#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'

                                    ## à ajouter
from flask import session, g
import pymysql.cursors

# Pour les machines de l'IUT
# mysql --user=login  --password=motDePasse --host=serveurmysql --database=BDD_login
def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost",                 # à modifier
            user="lili",                     # à modifier
            password="Secret123!",                # à modifier
            database="base_lili",        # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@app.route('/')
def show_layout():  # put application's code here
    return render_template('layout.html')


# //------- ROUTES LILI ------//

@app.route('/lieux_collecte/show', methods=['GET'])
def show_type_sport():
    mycursor = get_db().cursor()
    sql=''' SELECT * FROM lieux_collecte;'''
    mycursor.execute(sql)
    lieu = mycursor.fetchall()
    return render_template('/lieux_collecte/show_lieux_collecte.html', lieux_collecte=lieu)


# // ------ FIN ROUTE LILI ------//

if __name__ == '__main__':
    app.run()
