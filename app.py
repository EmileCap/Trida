
#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'

                                    ## à ajouter
from flask import session, g
import pymysql.cursors

# Pour les machines de l'IUT NFC
# mysql --user=login  --password=motDePasse --host=serveurmysql --database=BDD_login

#rachida

def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost",                 # à modifier
            user="root",                     # à modifier
            password="MAMA,22",                # à modifier
            database="bdd_trhebie",        # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        # à activer sur les machines personnelles :
        activate_db_options(g.db)
    return g.db


# MATTEO

# mysql --user=mbronne2 --password=secret --host=serveurmysql --database=BDD_mbronne2 --skip-ssl
'''def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="serveurmysql",  # à modifier
            user="mbronne2",  # à modifier
            password="secret",  # à modifier
            database="BDD_mbronne2",  # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db'''


# LILI
'''
def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost",  # à modifier
            user="lili",  # à modifier
            password="Secret123!",  # à modifier
            database="base_lili",  # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db
'''


# EMILE
'''
def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost",  # à modifier
            user="lili",  # à modifier
            password="Secret123!",  # à modifier
            database="base_lili",  # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db
'''


# RACHIDA
'''
def get_db():
    if 'db' not in g:
        g.db =  pymysql.connect(
            host="localhost",  # à modifier
            user="lili",  # à modifier
            password="Secret123!",  # à modifier
            database="base_lili",  # à modifier
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db
'''


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

# //------- ROUTES MATTEO ------//

@app.route('/camion/show', methods=['GET'])
def show_camion():
    mycursor = get_db().cursor()

    sql=''' 
    SELECT camion.id_camion, camion.kilometrage, camion.date_de_mise_en_service, conducteur.Nom_conducteur, localisation.adresse, modele.nom_modele
    FROM camion
    INNER JOIN conducteur ON camion.id_conducteur = conducteur.id_conducteur    
    INNER JOIN localisation ON camion.id_localisation = localisation.id_localisation
    INNER JOIN modele ON camion.id_modele = modele.id_modele;
    '''

    mycursor.execute(sql)
    camion = mycursor.fetchall()
    return render_template('/camion/show_camion.html', camion=camion)

@app.route('/camion/delete', methods=['GET'])
def delete_camion():
    mycursor = get_db().cursor()
    id_camion = request.args.get('id_camion', '')
    tuple_delete = (id_camion,)
    sql = '''
    DELETE FROM camion WHERE id_camion = %s;
    '''
    mycursor.execute(sql, tuple_delete)
    get_db().commit()
    print('camion: ' + id_camion)
    flash(u'un camion à été supprimé, id: ' + id_camion)
    return redirect('/camion/show')

# // ------ FIN ROUTE MATTEO ------//

# // ------ DEBUT ROUTE RACHIDA ------//





def activate_db_options(db):
    cursor = db.cursor()

@app.route('/conteneur/show', methods=['GET'])
def show_conteneur():
    mycursor = get_db().cursor()

    sql = """
          SELECT conteneur.id_conteneur, \
                 conteneur.id_conteneur, \
                capacite_max AS capacite_max, \
                 type_dechet.nom_dechet AS type_dechet, \
              date_creation AS date_creation, \
                 localisation.adresse AS localisation, \
                 couleur.nom_couleur  AS couleur
          FROM conteneur
                   LEFT JOIN type_dechet
                             ON conteneur.id_type_dechet = type_dechet.id_type_dechet
                   LEFT JOIN localisation
                             ON conteneur.id_localisation = localisation.id_localisation
                   LEFT JOIN couleur
                             ON conteneur.id_couleur = couleur.id_couleur
          ORDER BY conteneur.id_conteneur ASC \
          """

    mycursor.execute(sql)
    conteneurs = mycursor.fetchall()
    return render_template('conteneur/show_conteneur.html', conteneurs=conteneurs)

@app.route('/conteneur/add', methods=['GET'])
def add_conteneur():
    mycursor = get_db().cursor()
    sql="SELECT id_couleur AS id_couleur , nom_couleur AS nom_couleur FROM couleur ORDER BY id_couleur DESC "
    mycursor.execute(sql)
    couleurs = mycursor.fetchall()
    conteneurs = mycursor.fetchall()
    sql = "SELECT id_type_dechet AS id_type_dechet , nom_dechet AS nom_dechet FROM type_dechet ORDER BY id_type_dechet ASC "
    mycursor.execute(sql)
    type_dechets = mycursor.fetchall()
    sql = "SELECT id_localisation AS id_localisation , adresse AS adresse FROM localisation ORDER BY adresse DESC"
    mycursor.execute(sql)
    localisations = mycursor.fetchall()
    return render_template('conteneur/add_conteneur.html',conteneurs=conteneurs , couleurs=couleurs,localisations=localisations,type_dechets=type_dechets)

@app.route('/conteneur/add', methods=['POST'])
def valid_add_conteneur():
    mycursor = get_db().cursor()
    capacite_max = request.form.get('capacite_max', '')
    id_localisation = request.form.get('id_localisation', '')
    date_creation = request.form.get('date_creation', '')
    id_couleur = request.form.get('id_couleur', '')
    id_type_dechet = request.form.get('id_type_dechet', '')

    tuple_insert = (capacite_max, id_localisation, date_creation, id_couleur, id_type_dechet)

    sql = """
          INSERT INTO conteneur (capacite_max, id_localisation, date_creation, id_couleur, id_type_dechet)
          VALUES (%s, %s, %s, %s, %s)
          """
    mycursor.execute(sql, tuple_insert)
    get_db().commit()

    message = f'Conteneur ajouté : Capacité: {capacite_max}, Localisation :{id_localisation}, Couleur: {id_couleur}, Type Déchet :{id_type_dechet}'
    flash(message, 'alert-success')
    return redirect('/conteneur/show')

@app.route('/conteneur/edit', methods=['GET'])
def edit_conteneur():
    mycursor = get_db().cursor()
    id_conteneur = request.args.get('id', '')
    sql = ("SELECT id_conteneur as id_conteneur,"
           "capacite_max as capacite_max ,id_localisation as id_localisation,"
           "id_couleur as Id_couleur,id_type_dechet as id_type_dechet FROM conteneur WHERE id_conteneur=%s")
    mycursor.execute(sql, (id_conteneur,))

    conteneur = mycursor.fetchone()
    sql= "SELECT id_couleur as id_couleur,nom_couleur AS nom_couleur FROM couleur ORDER BY id_couleur DESC"
    mycursor.execute(sql)
    couleurs = mycursor.fetchall()
    sql = "SELECT id_localisation as id_localisation,adresse AS adresse FROM localisation ORDER BY adresse DESC"
    mycursor.execute(sql)
    localisations = mycursor.fetchall()
    sql = "SELECT id_type_dechet as id_type_dechet,nom_dechet AS nom_dechet FROM type_dechet ORDER BY nom_dechet DESC"
    mycursor.execute(sql)
    type_dechets = mycursor.fetchall()
    return render_template('conteneur/edit_conteneur.html', conteneur=conteneur ,couleurs = couleurs,localisations=localisations,type_dechets=type_dechets)

@app.route('/conteneur/edit', methods=['POST'])
def valid_edit_conteneur():
    mycursor = get_db().cursor()
    id_conteneur = request.form.get('id_conteneur', '')
    capacite_max = request.form.get('capacite_max', '')
    id_localisation = request.form.get('id_localisation', '')
    date_creation = request.form.get('date_creation', '')
    id_couleur = request.form.get('id_couleur', '')
    id_type_dechet = request.form.get('id_type_dechet', '')

    tuple_update = (capacite_max, id_localisation, date_creation, id_couleur, id_type_dechet, id_conteneur)

    sql = """
          UPDATE conteneur
          SET capacite_max = %s,
              id_localisation = %s,
              date_creation = %s,
              id_couleur = %s,
              id_type_dechet = %s
          WHERE id_conteneur = %s
          """
    mycursor.execute(sql, tuple_update)
    get_db().commit()

    message = f'Conteneur modifié : ID : {id_conteneur}, Capacité : {capacite_max}, Localisation : {id_localisation}, Couleur : {id_couleur}, Type Déchet: {id_type_dechet}'
    flash(message, 'alert-success')
    return redirect('/conteneur/show')
@app.route('/conteneur/delete', methods=['GET'])
def delete_conteneur():
    mycursor = get_db().cursor()
    id_conteneur = request.args.get('id')
    if id_conteneur and id_conteneur.isdigit():
        mycursor.execute("DELETE FROM conteneur WHERE id_conteneur = %s", (int(id_conteneur),))
        get_db().commit()
        flash(f'Conteneur supprimé : ID : {id_conteneur}', 'alert-warning')
    else:
        flash("ID de conteneur invalide", "alert-danger")
    return redirect('/conteneur/show')



from flask import request


@app.route('/conteneur/etat', methods=['GET'])
def show_etat_conteneur():
    mycursor = get_db().cursor()
    sql = """SELECT COUNT(conteneur.id_conteneur) AS Total, couleur.nom_couleur
             FROM conteneur
                      INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
             GROUP BY couleur.nom_couleur;"""

    mycursor.execute(sql)
    Total = mycursor.fetchall()
    return render_template('/conteneur/etat_conteneur.html', Total=Total)



# // ------ FIN ROUTE RACHIDA ------//

if __name__ == '__main__':
    app.run()
