# importar Flask
from flask import Flask, render_template
#inicializar le proyecto
app = Flask(__name__)

# lista donde se van a almacenar las personas
lista_personas = []

#agregar persona
@app.route('/persona')
def add_persona():
    return render_template("add_person.html")
    



# corriendo server
if __name__ == '__main__':
    app.run(port=3000, debug=True)