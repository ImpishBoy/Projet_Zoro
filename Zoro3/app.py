from flask import Flask, render_template, request, url_for, flash, redirect
import pyodbc

DSN = 'Driver={SQL Server};Server=DESKTOP-P7R44AE\\SQLEXPRESS;Database=gestion;'
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from magasin")


app=Flask(__name__)#montre le nom (app) de notre application a flask
app.config['SECRET_KEY']='clés_flash'



@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    item_id = int(item_id)

# Connexion à la base de données
    conn = pyodbc.connect(DSN)

    # Création d'un objet curseur
    cursor = conn.cursor()

    # Récupération des données du produit depuis la base de données
    cursor.execute('SELECT * FROM produit WHERE CodeProduit = ?', (item_id,))
    data = cursor.fetchone()

    # Si la méthode de la requête est POST, mise à jour des données du produit dans la base de données
    if request.method == 'POST':
        # Récupération des données du formulaire
       Nom = request.form['Nom']
       Adresse = request.form['Adresse']
       Telephone = request.form['Téléphone']
       Email = request.form['Mail']

        # Mise à jour des données du produit dans la base de données
    cursor.execute('''
            UPDATE produit
            SET Nom = ?, Descriptions = ?, StockActuel = ?, PrixUnitaire = ?
            WHERE CodeProduit = ?
        ''', (Nom,  Adresse, Telephone, Email , item_id))

        # Validation des modifications dans la base de données
    conn.commit()

        # Fermeture de la connexion à la base de données
    conn.close()

        # Affichage d'un message de succès à l'utilisateur
    flash(f'Le magasin numéro {item_id} a été modifié avec succès !', 'info')

        # Redirection de l'utilisateur vers la page du produit
    return redirect(url_for('listemagasin'))

   

@app.route('/delete/<int:item_id>', methods=['GET', 'POST'])
def delete(item_id):
    item_id = int(item_id)

    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM magasin WHERE ID_magasin = ?', (item_id,))

    conn.commit()
    conn.close()

    flash(f'Le magasin numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('listemagasin'))



DSN = 'Driver={SQL Server};Server=DESKTOP-P7R44AE\\SQLEXPRESS;Database=gestion;'
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from magasin")

@app.route('/MagEdit/<int:item_id>', methods=['GET', 'POST'])
def MagEdit(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Magasin WHERE ID_Magasin = ?', (item_id,))
    data = cursor.fetchone()
    if request.method == 'POST':
        nom = request.form["Nom"]
        adresse = request.form["Adresse"]
        telephone = request.form["Téléphone"]
        email = request.form["Mail"]
        cursor.execute('''
            UPDATE Magasin
            SET Nom = ?, Adresse = ?, Telephone = ?, Email = ?
            WHERE ID_Magasin = ?
        ''', (nom, adresse, telephone, email, item_id))
        conn.commit()
        conn.close()
        flash(f'Le magasin numéro {item_id} a été modifié avec succès !', 'info')
        return redirect(url_for('listemagasin'))
    return render_template('enregistremag.html', data=data)


@app.route('/MagDelete/<int:item_id>', methods=['GET', 'POST'])
def MagDelete(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Magasin WHERE ID_Magasin = ?', (item_id,))
    conn.commit()
    conn.close()
    flash(f'Le magasin numéro {item_id} a été supprimé avec succès !', 'info')
    return redirect(url_for('listemagasin'))



@app.route("/")
def I1():
    return render_template("connexion.html")

@app.route("/base")
def B():
    return render_template("base.html")

@app.route("/Addmagasin")
def addmagasin():
    return render_template("Addmagasin.html")

@app.route("/listemagasin")
def listemagasin():
    return render_template("listemagasin.html")

@app.route("/enregistre")
def enregistre():
    return render_template("enregistremag.html")

@app.route("/sup")
def sup():
    return render_template("sup.html")

@app.route("/supprimer")
def supprimer():
    return render_template("supprmer.html")

@app.route("/modif")
def modif():
    return render_template("modif.html")

@app.route("/modifier")
def modifier():
    return render_template("modifier.html")

if __name__== '__main__': # si notre nom = a main executer app
    app.run(debug=True) #debug=True pour ne pas avoir a relancer a chaque fois l'application


