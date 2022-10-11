from encuesta_app import app
from flask import render_template, redirect, session, request

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['post'])
def formulario():
    session['Name'] = request.form['Name']
    session['Dojo_Location'] = request.form['Dojo_Location']
    session['Favorite_Language'] = request.form['Favorite_Language']
    session['Comments'] = request.form['Comments']
    
    return redirect('/result')


@app.route('/result')
def resultado():
    return render_template('result.html')