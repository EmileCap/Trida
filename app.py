
#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.secret_key = 'une cle(token) : grain de sel(any random string)'

                                    ## à ajouter
from flask import session, g
import pymysql.cursors
 # mysql --user=lili --password='Secret123!' --host=localhost --database=base_lili
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




@app.route('/type-sport/show', methods=['GET'])
def show_type_sport():
    mycursor = get_db().cursor()
    sql=''' SELECT * FROM typesSport;'''
    mycursor.execute(sql)
    typesSport = mycursor.fetchall()
    return render_template('type-sport/show_type_sport.html', typesSport=typesSport)


@app.route('/type-sport/add', methods=['GET'])
def add_type_sport():
    mycursor = get_db().cursor()
    sql = '''  SELECT libelleType  FROM typesSport;'''
    mycursor.execute(sql)
    return render_template('type-sport/add_type_sport.html')


@app.route('/type-sport/add', methods=['POST'])
def valid_add_type_sport():
    libelle = request.form.get('libelle', '')
    print(u'type sport ajouté , libellé : ', libelle)
    message = u'type sport ajouté , libelle : ' +libelle
    flash(message, 'alert-success')
    return redirect('/type-sport/show')


@app.route('/type-sport/edit', methods=['GET'])
def edit_type_sport():
    mycursor = get_db().cursor()
    sql = '''  SELECT *
               FROM typesSport;'''
    mycursor.execute(sql)
    type_sport = mycursor.fetchall()
    return render_template('type-sport/edit_type_sport.html', type_sport=type_sport)

@app.route('/type-sport/edit', methods=['POST'])
def valid_edit_type_sport():
    libelle = request.form.get('libelle', '')
    id = request.form.get('id', '')
    print(u'type sport modifié , libelle : ', libelle,' -- identifiant du type de sport : ',id )
    message=u'type sport modifié , libelle : '+ libelle+' -- identifiant du type de sport : '+id
    flash(message, 'alert-success')
    return redirect('/type-sport/show')



@app.route('/type-sport/delete', methods=['GET'])
def delete_type_sport():
    id = request.args.get('id', '')
    libelle = request.args.get('libelle', '')
    print (u'type sport supprimé, libelle : ', libelle,' -- identifiant du type de sport : ',id )
    message=u'type sport supprimé,  libelle : '+ libelle +' -- identifiant du type de sport : '+id
    flash(message, 'alert-warning')
    return redirect('/type-sport/show')





# sports


@app.route('/sport/show', methods=['GET'])
def show_sport():
    mycursor = get_db().cursor()
    sql = ''' SELECT * 
              FROM sports;'''
    mycursor.execute(sql)
    sports = mycursor.fetchall()
    return render_template('sport/show_sport.html', sports=sports)

@app.route('/sport/add', methods=['GET'])
def add_sport():
    mycursor = get_db().cursor()
    sql = '''  SELECT *
               FROM typesSport;'''
    mycursor.execute(sql)
    typesSport = mycursor.fetchall()
    return render_template('sport/add_sport.html', typesSport=typesSport)

@app.route('/sport/add', methods=['POST'])
def valid_add_sport():
    nomSport = request.form.get('nomSport', '')
    typeSport_id = request.form.get('typeSport_id', '')
    prixInscription = request.form.get('prixInscription', '')
    dateLimiteInscription = request.form.get('dateLimiteInscription', '')
    image = request.form.get('image', '')
    nbPratiquants = request.form.get('nbPratiquants', '')
    message = u'sport ajouté , nomSport : '+nomSport + ' -- typeSport_id : ' + typeSport_id + ' -- prixInscription : ' + prixInscription + ' -- dateLimiteInscription : '+  dateLimiteInscription + ' -- nbPratiquants : ' + nbPratiquants + ' -- image : ' + image
    print(message)
    flash(message, 'alert-success')
    return redirect('/sport/show')

@app.route('/sport/delete', methods=['GET'])
def delete_sport():
    id = request.args.get('id', '')
    nomSport = request.args.get('nomSport', '')
    typeSport_id = request.args.get('typeSport_id', '')
    prixInscription = request.args.get('prixInscription', '')
    dateLimiteInscription = request.args.get('dateLimiteInscription', '')
    image = request.args.get('image', '')
    nbPratiquants = request.args.get('nbPratiquants', '')
    message=u'sport supprimé , nomSport : '+nomSport + ' -- typeSport_id : ' + typeSport_id + ' -- prixInscription : ' + prixInscription + ' -- dateLimiteInscription : '+  dateLimiteInscription + ' -- nbPratiquants : ' + nbPratiquants + ' -- image : ' + image+' -- pour le sport d\'identifiant : '+ id
    flash(message, 'alert-warning')
    return redirect('/sport/show')

@app.route('/sport/edit', methods=['GET'])
def edit_sport():
    mycursor = get_db().cursor()
    sql = '''  SELECT *
               FROM typesSport;'''
    sql2 = '''SELECT * FROM sports;'''
    mycursor.execute(sql)
    typesSport = mycursor.fetchall()
    mycursor.execute(sql2)
    sport = mycursor.fetchall()
    return render_template('sport/edit_sport.html', sport=sport, typesSport=typesSport)

@app.route('/sport/edit', methods=['POST'])
def valid_edit_sport():
    nomSport = request.form.get('nomSport', '')
    id = request.form.get('id', '')
    typeSport_id = request.form.get('typeSport_id', '')
    prixInscription = request.form.get('prixInscription', '')
    dateLimiteInscription = request.form.get('dateLimiteInscription', '')
    image = request.form.get('image', '')
    nbPratiquants = request.form.get('nbPratiquants', '')
    message = u'sport modifié , nomSport : ' + nomSport + ' -- typeSport_id : ' + typeSport_id + ' -- prixInscription : ' + prixInscription + ' -- dateLimiteInscription : ' + dateLimiteInscription + ' -- nbPratiquants : ' + nbPratiquants + ' -- image : ' + image +' -- pour le sport d\'identifiant : '+ id
    print(message)
    flash(message, 'alert-success')
    return redirect('/sport/show')



# Filtre


@app.route('/sport/filtre', methods=['GET'])
def filtre_sport():
    mycursor = get_db().cursor()
    sql = ''' SELECT *
              FROM sports;'''
    mycursor.execute(sql)
    sports = mycursor.fetchall()
    typesSport = mycursor.fetchall()
    return render_template('sport/front_sport_filtre_show.html', sports=sports, typesSport=typesSport)


@app.route('/sport/filtre', methods=['POST'])
def filtre_sport_valid():
    filter_word = request.form.get('filter_word', None)
    filter_value_min = request.form.get('filter_value_min', None)
    filter_value_max = request.form.get('filter_value_max', None)
    filter_items = request.form.getlist('filter_items', None)
    if filter_word and filter_word != "":
        message = u'filtre sur le mot :' + filter_word
        flash (message, 'alert-success')
    if filter_value_min or filter_value_max:
        min=str(filter_value_min).replace(' ','').replace(',','.')
        max = str(filter_value_max).replace(' ', '').replace(',', '.')
        if min.replace('.','', 1).isdigit() and max.replace('.','', 1).isdigit():
            if float(min) < float(max):
                message = u'filtre sur la colonne avec un numérique entre:' + min+" et "+ max
                flash (message, 'alert-success')
            else:
                message=u'min < max'
                flash (message, 'alert-warning')
        else:
            message=u'min '+ min +' et max '+max+' doivent être des numériques positifs'
            flash(message, 'alert-warning')
    if filter_items and filter_items != []:
        message=u'case à cocher selectionnée: '
        for case in filter_items:
            message+= ' id: '+case+' '
        flash (message, 'alert-success')
    return redirect('/sport/filtre')

if __name__ == '__main__':
    app.run()
