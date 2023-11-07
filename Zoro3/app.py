from flask import Flask, render_template, request, url_for, flash, redirect

import pyodbc

DSN = 'Driver={SQL Server};Server=DESKTOP-P7R44AE\\SQLEXPRESS;Database=gestion;'
conn = pyodbc.connect(DSN)
cursor = conn.cursor()
cursor.execute("select * from magasin")


app=Flask(__name__)#montre le nom (app) de notre application a flask
app.config['SECRET_KEY']='clés_flash'





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

@app.route("/listemagasin", methods=['GET','POST'])
def listemagasin():
    DSN = 'Driver={SQL Server};Server=DESKTOP-P7R44AE\\SQLEXPRESS;Database=gestion;'
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute("select * from magasin")
    data = cursor.fetchall()
    conn.close()
    return render_template("listemagasin.html", data=data)



# @app.route('/ajout', methods=['GET', 'POST'])
# def ajout():
#     if request.method == 'POST':
#          Nom = request.form['nom']
#          adresse = request.form['Adresse']
#          Telephone = request.form["Téléphone"]
#          Mail = request.form['Mail']
#          conn = pyodbc.connect(DSN)
#          cursor = conn.cursor()
#          cursor.execute('''
#             INSERT INTO Produit (Nom, Adresse, telephone, email,)
#             VALUES ( ?, ?, ?, ?)
#          ''', (Nom, adresse, Telephone, Mail))
#          conn.commit()
#          conn.close()
#          flash("Votre magasin a été enregistré avec succès !", 'info')
#          return redirect(url_for('listemagasin'))
#     data=''
#     return render_template('enregistremag.html',data=data)





@app.route("/enregistremag", methods=["GET","POST"])
def enregistremag():
    if request.method == 'POST':

        Nom = request.form["Nom"]
        Adresse = request.form["Adresse"]
        telephone = request.form["Téléphone"]
        email = request.form["Mail"]
        DSN = 'Driver={SQL Server};Server=DESKTOP-P7R44AE\\SQLEXPRESS;Database=gestion;'
        conn = pyodbc.connect(DSN)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Magasin (Nom, Adresse, Téléphone, Mail)
            VALUES
            ( ?, ?, ?, ?)
         ''', (Nom, Adresse, telephone, email))
        conn.commit()
        conn.close()
        flash("Votre magasin a été enregistré avec succès !", 'info')
        return redirect(url_for('listemagasin'))    
    data=''
    return render_template("enregistremag.html",data=data)



@app.route('/MagEdit/<int:item_id>', methods=['GET', 'POST'])
def MagEdit(item_id):
    item_id = int(item_id)
    conn = pyodbc.connect(DSN)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Magasin WHERE ID_Magasin = ?', (item_id,))
    data = cursor.fetchone()
    if request.method == 'POST':
        Nom = request.form["Nom"]
        adresse = request.form["Adresse"]
        telephone = request.form["Téléphone"]
        email = request.form["Mail"]
        cursor.execute('''
            UPDATE Magasin 
            SET Nom = ?, Adresse = ?, Téléphone = ?, Mail = ?
            WHERE ID_Magasin = ?
        ''', (Nom, adresse, telephone, email, item_id))
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
    return render_template("zoro1.html")

@app.route("/base")
def B():
    return render_template("base.html")





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


if __name__== "__main__":
    app.run(debug=True)