from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods = ['GET'])
def search():
    import pandas as pd
    regione = request.args['regione']
    dati_regioni = pd.read_csv('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-statistici-riferimento/popolazione-istat-regione-range.csv')
    risultato = dati_regioni[dati_regioni['denominazione_regione']==regione.capitalize()].index
    if len(risultato) == 0:
        table = 'Regione non trovata'
    else:
        table = list(risultato)
    return render_template('radiobutton.html', tabella = table)

@app.route('/info', methods = ['GET'])
def info()
import pandas as pd
    regione = request.args['id']

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)