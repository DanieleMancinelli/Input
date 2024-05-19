'''
Scrivere una pagina html/flask che visualizzi l'elenco delle regioni in un menu a tendina
'''
from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati_regioni = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')

@app.route('/')
def home():
    regioni = dati_regioni.drop_duplicates(subset=['denominazione_regione'])
    lista_regioni = list(regioni['denominazione_regione'])
    return render_template('homepage.html', lista_regioni = lista_regioni)

@app.route('/search', methods = ['GET'])
def search():
    regione = request.args['menu']
    risultato = dati_regioni[dati_regioni['denominazione_regione']==regione.capitalize()].index
    if len(risultato) == 0:
        table = 'Regione non trovata'
    else:
        table = list(risultato)
    return render_template('checkbox.html', tabella = table)

@app.route('/info', methods = ['GET'])
def info():
    indici = request.args.getlist('id')  # ottengo la lista degli indici selezionati
    indici = [int(indice) for indice in indici]  # converto gli indici in interi
    righe_selezionate = dati_regioni.iloc[indici]
    return righe_selezionate.to_html()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)