# importar Flask
from flask import Flask, render_template, request
#inicializar le proyecto
app = Flask(__name__)

# lista donde se van a almacenar las personas
lista_personas = []

# mostrar formulario para agregar persona

@app.route('/persona')
def render_form_persona():
    return render_template("add_person.html")

 
# guardando los datos de la persona en la lista
@app.route('/persona', methods=['POST'])
def add_persona():
    # verificando si hay algun envio de datos
    if request.method == 'POST':
        # accediendo a los elementos del formulario
        cedula = request.form["id"]
        nombre = request.form["nombre"]
        mail = request.form["mail"]
        telefono = request.form["telefono"]
        # estructura del diccionario persona
        persona = {"id": cedula, "nombre": nombre, "mail": mail, "telefono": telefono}
        # agregar la persona a la lista
        lista_personas.append(persona)
        # mostrar mensaje de confirmacion
        return render_template("add_person.html", mensaje="Persona agregada con exito!")
    else:
        return render_template("add_person.html", mensaje="Error al agregar la persona!")


# mostar las personas registradas
@app.route('/personas-registradas')
def render_personas():
    return render_template("show_person.html", personas=lista_personas)


# corriendo server
if __name__ == '__main__':
    app.run(port=3000, debug=True)