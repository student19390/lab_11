from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
     dane = {'tytul':'Strona Główna', 'tresc':'Witaj na stronie głównej.'}
     return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])

	
@app.route("/about")
def about():
     dane = {'tytul':'O mnie', 'tresc':'Witam na mojej stronie internetowej dotyczącej grafiki komputerowej!'}
     return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/info')
def info():
    posty = [
        {
         'author': {'username': 'Admin'},
         'body': 'Tablety!'
        },
        {
         'author': {'username': 'FanGrafiki'},
         'body': 'Tablety dostępne na rynku.'
    }]
    dane = {'tytul':'Informacje', 'tresc':'Szczegółowe informacje.'}
    return render_template('info.html', tytul=dane['tytul'], tresc=dane['tresc'], posty=posty)
 
@app.route("/kontent")
def kontent():
     dane = {'tytul':'Kontent', 'tresc':'To jest kontent . . .'}
     return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])
	
if __name__ == "__main__":
	app.run()
