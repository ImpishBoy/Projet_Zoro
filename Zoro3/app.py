from flask import Flask,render_template 

app=Flask(__name__)





@app.route("/")
def I1():
    return render_template("zoro1.html")

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


if __name__== "__main__":
    app.run()