from encuesta_app import app
from encuesta_app.controllers import controller
app.secret_key = "supersecreto"

if __name__=="__main__": 
    app.run(debug=True)   