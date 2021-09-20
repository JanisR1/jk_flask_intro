from flask import Flask, render_template, request, redirect
from file_proc import pievienot

app = Flask(__name__)

@app.route('/')
def parEasyRedmine():
    return render_template('par-easy-redmine.html')

@app.route('/administresana')
def administresana():
    return render_template('administresana.html')

@app.route('/ieviesana')
def ieviesana():
    return render_template('ieviesana.html')

@app.route('/sazina')
def sazina():
    return render_template('sazina.html')

@app.route('/dati')
def dati():
    rindinas = lasitDatus()
    dati = []
    for rindina in rindinas:
        ieraksts = rindina.split(',')
        dati.append(ieraksts)
        dati2.append({'vards':ieraksts[0], 'uzvards':ieraksts[1], 'hobijs':ieraksts[2]})

    #print(dati)
    return render_template("dati.html", rindinas = dati, rindinas2 = dati2)

if __name__ == '__main__':
    app.run(port=80, debug=True)