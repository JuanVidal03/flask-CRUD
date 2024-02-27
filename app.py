# importar Flask
from flask import Flask, render_template, request
#inicializar le proyecto
app = Flask(__name__)

# lista donde se van a almacenar las personas
lista_personas = []

# mostrar formulario para agregar persona
@app.route('/personas')
def render_form_persona():
    return render_template("add_person.html")
 
# guardando los datos de la persona en la lista
@app.route('/personas', methods=['POST'])
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


def persona_id():
    for persona in lista_personas:
        print(persona)

# editando persona por id
@app.route('/editar-persona/<id>')
def edit_person(id):
    # obteniendo el id de la persona a actualizar
    cedula = id
    print(cedula)
    persona_id()
        
    # verificando si hay una actualizacion de datos
    if request.method == 'PUT':
        # obteniendo datos del formulario
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        mail = request.form["mail"]
        telefono = request.form["telefono"]
        
        
        return render_template("update_person.html", mensaje="Persona encontrada")
    # en caso de no encontrar la persona
    else:
        return render_template("update_person.html", mensaje="No fue encontrada la persona!")

# corriendo server
if __name__ == '__main__':
    app.run(port=3000, debug=True)