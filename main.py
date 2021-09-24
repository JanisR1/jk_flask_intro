from flask import Flask, render_template, request, redirect
from datu_apstrade import lasitDatus, pievienotEpastu, pievienotUzvardu, pievienotVardu, pievienotZinojumu

app = Flask(__name__)

@app.route("/")
def parEasyRedmine():
    return render_template("par-easy-redmine.html")

@app.route("/administresana")
def administresana():
    return render_template("administresana.html")

@app.route("/galerija")
def galerija():
    return render_template("galerija.html")

@app.route("/sazina")
def sazina():
    statuss = request.args.get("statuss")
    return render_template("sazina.html", nosutits = statuss)

@app.route("/sutisana", methods = ["POST"])
def sutisana():
    vards = request.form.get("vards")
    pievienotVardu(vards)

    uzvards = request.form.get("uzvards")
    pievienotUzvardu(uzvards)

    epasts = request.form.get("epasts")
    pievienotEpastu(epasts)

    zinojums = request.form.get("zinojums")
    pievienotZinojumu(zinojums)

    return redirect("/sazina?statuss=1")

@app.route("/dati")
def dati():
    ieraksti = lasitDatus()
    dati = []
    for ieraksts in ieraksti:
        dati.append(ieraksts)
    grupetiDati = [dati[n:n+4] for n in range(0, len(dati), 4)]

    return render_template("dati.html", ieraksti = grupetiDati)

if __name__ == "__main__":
    app.run(port=80, debug=True)