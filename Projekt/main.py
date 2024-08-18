#Импорт
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_zhik = request.form.get('button_zhik')
    button_prom = request.form.get('button_prom')
    button_selo = request.form.get('button_selo')
    button_vysel = request.form.get('button_vysel')
    button_urban = request.form.get('button_urban')
    button_auto = request.form.get('button_auto')
    button_gas = request.form.get('button_gas')
    button_tech = request.form.get('button_tech')
    button_zachran = request.form.get('button_zachran')
    button_umelo = request.form.get('button_umelo')
    button_finansis = request.form.get('button_finansis')
    button_sotr = request.form.get('button_sotr')
    button_ucit = request.form.get('button_ucit')
    button_izmenc = request.form.get('button_izmenc')
    return render_template('index.html', button_zhik=button_zhik,button_prom=button_prom,button_selo=button_selo,button_vysel=button_vysel,
                           button_urban=button_urban,button_auto=button_auto,button_gas=button_gas,button_tech=button_tech,
                           button_zachran=button_zachran,button_umelo=button_umelo,button_finansis=button_finansis,button_sotr=button_sotr,
                           button_ucit=button_ucit,button_izmenc=button_izmenc)

if __name__ == "__main__":
    app.run(debug=True)