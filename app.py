from flask import Flask, render_template, request

app = Flask(__name__)

def bahşişHesapla(gelenHesap, hesapOrani):
	return gelenHesap*hesapOrani/100

@app.route('/', methods = ['POST', 'GET'])
def bahsis():
	bahsis=''
	bahsisOrani=''
	if request.method=='POST' and 'Hesap' in request.form:
		Hesap = float(request.form.get('Hesap'))
		bahsisOrani = float(request.form.get('bahsisOrani'))
		bahsis = bahşişHesapla(Hesap, bahsisOrani)

	return render_template('index.html', bahsis=bahsis, bahsisOrani=bahsisOrani)


app.run()