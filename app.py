
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

#test


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
    sql=''' SELECT * FROM planning JOIN passe ON planning.id_tournee = passe.id_tournee;'''
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

# //------- ROUTES MATTEO ------//

@app.route('/camion/show', methods=['GET'])
def show_camion():
    mycursor = get_db().cursor()

    sql=''' 
    SELECT camion.id_camion, camion.kilometrage, camion.date_de_mise_en_service, conducteur.Nom_conducteur, localisation.adresse, modele.nom_modele
    FROM camion
    INNER JOIN conducteur ON camion.id_conducteur = conducteur.id_conducteur    
    INNER JOIN localisation ON camion.id_localisation = localisation.id_localisation
    INNER JOIN modele ON camion.id_modele = modele.id_modele
    ORDER BY camion.id_camion ASC;
    '''

    mycursor.execute(sql)
    camion = mycursor.fetchall()
    return render_template('/camion/show_camion.html', camion=camion)

@app.route('/camion/add', methods=['GET'])
def add_camion():
    mycursor = get_db().cursor()
    sql = '''
    SELECT id_camion, kilometrage, date_de_mise_en_service FROM camion;
    '''
    mycursor.execute(sql)
    camion = mycursor.fetchall()

    sql = '''
    SELECT id_localisation, adresse FROM localisation;
    '''
    mycursor.execute(sql)
    localisation = mycursor.fetchall()

    sql = '''
    SELECT id_modele, nom_modele FROM modele;
    '''
    mycursor.execute(sql)
    id_modele = mycursor.fetchall()

    sql = '''
    SELECT id_conducteur, Nom_conducteur, prenom_conducteur FROM conducteur;
    '''
    mycursor.execute(sql)
    conducteurs = mycursor.fetchall()

    return render_template('/camion/add_camion.html', camion=camion , localisation=localisation, id_modele=id_modele, conducteurs=conducteurs)

@app.route('/camion/add', methods=['POST'])
def valid_add_camion():
    mycursor = get_db().cursor()

    kilometrage = request.form.get('kilometrage', '')
    date_de_mise_en_service = request.form.get('date_de_mise_en_service', '')
    id_localisation = request.form.get('id_localisation', '')
    id_modele = request.form.get('id_modele', '')
    id_conducteur = request.form.get('id_conducteur', '')
    tuple_insert = (kilometrage, date_de_mise_en_service, id_localisation, id_modele, id_conducteur)

    sql = '''
    INSERT INTO camion (kilometrage, date_de_mise_en_service, id_localisation, id_modele, id_conducteur)
    VALUES (%s, %s, %s, %s, %s);
    '''
    mycursor.execute(sql, tuple_insert)
    get_db().commit()

    message = u'Camion ajouté: kilometrage: ' + kilometrage + ', date de mise en service: ' + date_de_mise_en_service + ', localisation: ' + id_localisation + ', id_modele: ' + id_modele + ', conducteur: ' + id_conducteur
    flash(message, 'alert-success')
    return redirect('/camion/show')

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

    message = f'Conteneur modifié : ID : {id_conteneur}, Capacité : {capacite_max}, Localisation : {id_localisation}, Date_creation : {date_creation} Couleur : {id_couleur}, Type Déchet: {id_type_dechet}'
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

    sql_1 = """SELECT COUNT(conteneur.id_conteneur) AS Total, couleur.nom_couleur
               FROM conteneur
               INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
               GROUP BY couleur.nom_couleur;"""
    mycursor.execute(sql_1)
    Total = mycursor.fetchall()

    sql_2 = """SELECT AVG(conteneur.capacite_max) AS capacite_moyenne_par_couleur, couleur.nom_couleur
               FROM conteneur
               INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
               GROUP BY couleur.nom_couleur
               ORDER BY couleur.nom_couleur ASC;"""
    mycursor.execute(sql_2)
    capacite_moyenne_par_couleur = mycursor.fetchall()

    sql_3 = """SELECT couleur.nom_couleur,
                      COUNT(conteneur.id_conteneur) AS total_conteneurs,
                      AVG(conteneur.capacite_max) AS capacite_moyenne
               FROM conteneur
               INNER JOIN couleur ON conteneur.id_couleur = couleur.id_couleur
               GROUP BY couleur.nom_couleur
               ORDER BY couleur.nom_couleur;"""
    mycursor.execute(sql_3)
    capacite_moyenne_par_couleur_total_conteneur = mycursor.fetchall()

    sql_4 = """SELECT COUNT(conteneur.id_conteneur) AS Total_conteneur_par_type_dechet, type_dechet.nom_dechet
               FROM conteneur
               INNER JOIN type_dechet ON conteneur.id_type_dechet = type_dechet.id_type_dechet
               GROUP BY type_dechet.nom_dechet
               ORDER BY type_dechet.nom_dechet ASC;"""
    mycursor.execute(sql_4)
    Total_conteneur_par_type_dechet = mycursor.fetchall()

    return render_template(
        '/conteneur/etat_conteneur.html',
        Total=Total,
        capacite_moyenne_par_couleur=capacite_moyenne_par_couleur,
        capacite_moyenne_par_couleur_total_conteneur=capacite_moyenne_par_couleur_total_conteneur,
        Total_conteneur_par_type_dechet=Total_conteneur_par_type_dechet
    )






# // ------ FIN ROUTE RACHIDA ------//


# // ------ DEBUT ROUTE EMILE ------//


@app.route('/modele/show', methods=['GET'])
def modele_show():
    mycursor = get_db().cursor()
    sql = '''SELECT * FROM modele'''
    mycursor.execute(sql)
    modele = mycursor.fetchall()
    return render_template('modele/modele_show.html', modele=modele)


@app.route("/modele/add", methods=["GET"])
def modele_add():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM marque")
    marques = cursor.fetchall()
    return render_template("modele/modele_add.html", marques=marques)


@app.route("/modele/add", methods=["POST"])
def modele_add_post():
    nom = request.form["nom_modele"]
    poids = request.form["poids"]
    capacite = request.form["capacité_de_conteneur"]
    poids_max = request.form["poids_max"]
    conso = request.form["consommation_moyenne"]
    hauteur = request.form["hauteur"]
    id_marque = request.form["id_marque"]

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO modele(nom_modele, poids, capacité_de_conteneur, poids_max, consommation_moyenne, hauteur, id_marque) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (nom, poids, capacite, poids_max, conso, hauteur, id_marque)
    )
    db.commit()

    flash("Modèle ajouté avec succès", "success")
    return redirect("/modele/show")


@app.route("/modele/edit", methods=["GET"])
def modele_edit():
    id = request.args.get("id")
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM modele WHERE id_modele = %s", (id,))
    modele = cursor.fetchone()
    cursor.execute("SELECT * FROM marque")
    marques = cursor.fetchall()
    return render_template("/modele/modele_edit.html", modele=modele, marques=marques)


@app.route("/modele/edit", methods=["POST"])
def modele_edit_post():
    id = request.args.get("id")

    nom = request.form["nom_modele"]
    poids = request.form["poids"]
    poids_max = request.form["poids_max"]
    hauteur = request.form["hauteur"]
    capacite_max = request.form["capacité_de_conteneur"]
    consomation = request.form["consommation_moyenne"]
    marque = request.form["id_marque"]

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "UPDATE modele SET nom_modele=%s, poids=%s,poids_max=%s , hauteur=%s , capacité_de_conteneur=%s, consommation_moyenne = %s, id_marque =%s WHERE id_modele=%s",
        (nom, poids, poids_max, hauteur, capacite_max, consomation, marque, id)
    )
    db.commit()

    flash("Modèle modifié avec succès", "warning")
    return redirect("/modele/show")


@app.route("/modele/delete")
def modele_delete():
    id = request.args.get("id")
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM camion WHERE id_modele = %s", (id,))
    cursor.execute("DELETE FROM modele WHERE id_modele = %s", (id,))
    db.commit()
    flash("Modèle supprimé", "danger")
    return redirect("/modele/show")


@app.route("/modele/stats", methods=["GET"])
def modele_stats():
    marque_moy = request.args.get("marque_moyenne") or None
    pmin = request.args.get("pmin") or None
    pmax = request.args.get("pmax") or None
    conso_max = request.args.get("conso_max") or None
    marque_tri = request.args.get("marque_tri") or None

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT AVG(poids) AS avg_poids FROM modele")
    avg_poids = cursor.fetchone().get("avg_poids")

    cursor.execute("SELECT SUM(poids) AS sum_poids FROM modele")
    sum_poids = cursor.fetchone().get("sum_poids")

    cursor.execute("SELECT MIN(poids) AS min_poids FROM modele")
    min_poids = cursor.fetchone().get("min_poids")

    cursor.execute("SELECT MAX(poids) AS max_poids FROM modele")
    max_poids = cursor.fetchone().get("max_poids")

    cursor.execute("SELECT COUNT(*) AS total_modele FROM modele")
    total_modele = cursor.fetchone().get("total_modele")

    cursor.execute("SELECT AVG(consommation_moyenne) AS avg_conso FROM modele")
    avg_conso = cursor.fetchone().get("avg_conso")

    cursor.execute("SELECT AVG(hauteur) AS avg_hauteur FROM modele")
    avg_hauteur = cursor.fetchone().get("avg_hauteur")

    cursor.execute("SELECT COUNT(*) AS nb_marques FROM marque")
    nb_marques = cursor.fetchone().get("nb_marques")

    cursor.execute("""
        SELECT marque.nom_marque, COUNT(*) AS nb
        FROM modele
        INNER JOIN marque ON modele.id_marque = marque.id_marque
        GROUP BY marque.id_marque
        ORDER BY nb DESC
    """)
    nb_par_marque = cursor.fetchall()

    cursor.execute("""
        SELECT marque.nom_marque, AVG(consommation_moyenne) AS conso
        FROM modele
        INNER JOIN marque ON modele.id_marque = marque.id_marque
        GROUP BY marque.id_marque
        ORDER BY conso ASC
    """)
    conso_par_marque = cursor.fetchall()

    cursor.execute("SELECT * FROM marque ORDER BY nom_marque")
    marques = cursor.fetchall()

    cursor.execute(
        "SELECT AVG(poids) AS moy FROM modele WHERE (%s IS NULL OR id_marque = %s)",
        (marque_moy, marque_moy)
    )
    moy_marque = cursor.fetchone().get("moy")

    cursor.execute(
        "SELECT * FROM modele WHERE (%s IS NULL OR poids BETWEEN %s AND %s)",
        (pmin, pmin, pmax)
    )
    modele_poids_range = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM modele WHERE (%s IS NULL OR consommation_moyenne <= %s)",
        (conso_max, conso_max)
    )
    modele_conso = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM modele WHERE (%s IS NULL OR id_marque = %s) ORDER BY poids DESC",
        (marque_tri, marque_tri)
    )
    modele_tri_marque = cursor.fetchall()

    db.commit()
    return render_template(
        "/modele/modele_stats.html", avg_poids=avg_poids, sum_poids=sum_poids, min_poids=min_poids, max_poids=max_poids,
        total_modele=total_modele, avg_conso=avg_conso, avg_hauteur=avg_hauteur, nb_marques=nb_marques,
        nb_par_marque=nb_par_marque, conso_par_marque=conso_par_marque, marques=marques, moy_marque=moy_marque,
        modele_poids_range=modele_poids_range, modele_conso=modele_conso, modele_tri_marque=modele_tri_marque
    )


# // ------ FIN ROUTE EMILE ------//

if __name__ == '__main__':
    app.run(debug=True)
