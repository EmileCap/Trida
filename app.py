
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
            host="localhost",                 # à modifie
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
def show_lieux_collecte():
    mycursor = get_db().cursor()
    sql=''' SELECT * FROM lieux_collecte;'''
    mycursor.execute(sql)
    lieu = mycursor.fetchall()
    return render_template('/lieux_collecte/show_lieux_collecte.html', lieux_collecte=lieu)


@app.route('/lieux_collecte/add', methods=['GET'])
def add_lieux_collecte():
    mycursor = get_db().cursor()
    sql = '''SELECT localisation.adresse, lieux_collecte.libelle_lieu_de_collecte FROM lieux_collecte JOIN localisation ON lieux_collecte.id_localisation = localisation.id_localisation'''
    mycursor.execute(sql)
    lieu = mycursor.fetchall()
    return render_template('/lieux_collecte/add_lieu_collecte.html', lieux_collecte=lieu)




@app.route('/lieux_collecte/edit', methods=['GET'])
def edit_lieux_collecte():
    id_lieu = request.args.get('id')
    mycursor = get_db().cursor()
    sql = '''SELECT localisation.adresse, lieux_collecte.libelle_lieu_de_collecte FROM lieux_collecte JOIN localisation ON lieux_collecte.localisation_id = localisation_id'''
    mycursor.execute(sql, (id_lieu,))
    lieu = mycursor.fetchall()  # fetchone() car tu veux un seul lieu
    return render_template('/lieux_collecte/edit_lieu_collecte.html', lieux_collecte=lieu)


# // ------ FIN ROUTE LILI ------//

if __name__ == '__main__':
    app.run()
