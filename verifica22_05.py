from flask import Flask, render_template
app = Flask(__name__)
import pandas as pd
df = pd.read_csv('/workspace/Input/data/vendite.csv')
@app.route('/')
def homepage():
    risultato = sorted(list(set(df['Country'])))
    return render_template('nazioni.html', lista = risultato)

@app.route('/elencoCitta/<nazione>', methods=['GET'])
def elencoCitta(nazione):
    citta = df[df['Country'] == nazione].groupby('City').size().reset_index(name='CustomerCount')
    citta = citta.sort_values(by='CustomerCount', ascending=False)
    cities = list(zip(citta['City'], citta['CustomerCount']))
    return render_template('radiobutton2.html', cities=cities, nazione=nazione)

@app.route('/elencoClienti/<nazione>/<citta>', methods=['GET'])
def elencoClienti(nazione, citta):
    clienti = df[(df['Country'] == nazione) & (df['City'] == citta)]
    return render_template('table.html', tabella = clienti)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)