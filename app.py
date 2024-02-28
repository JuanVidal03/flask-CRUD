# importar Flask
from flask import Flask, render_template, request, redirect
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

# renderizando el form de actalizar persona
@app.route('/editar-persona/<id>')
def edit_person_render_form(id):
    # almacenar persona
    persona = None
    # ncontrando persona
    for person in lista_personas:
        if person["id"] == id:
            persona = person
            break
    return render_template("update_person.html", mensaje="Persona encontrada", persona = persona)

# editando persona por id
@app.route('/editar-persona/<id>', methods=["POST"])
def edit_person_by_id(id):
    # almacenar persona
    persona = None
    # ncontrando persona
    for person in lista_personas:
        if person["id"] == id:
            persona = person
            break
        
    # verificando si hay una actualizacion de datos
    if request.method == 'POST':
        # obteniendo datos del formulario
        cedula = request.form["cedula"]
        nombre = request.form["nombre"]
        mail = request.form["mail"]
        telefono = request.form["telefono"]
        
        # persona actualizada
        new_person = {"id": cedula, "nombre": nombre, "mail": mail, "telefono": telefono}
        
        # encontrar persona y obtener su índice
        person_index = None
        for index, person in enumerate(lista_personas):
            if person["id"] == id:
                person_index = index
                break
            
        # actualizar la persona en su posicion actual
        if person_index is not None:
            lista_personas[person_index] = new_person
        
        return redirect("/personas-registradas")
    # en caso de no encontrar la persona
    else:
        return render_template("update_person.html", mensaje="No fue encontrada la persona!", persona = persona)


# corriendo server
if __name__ == '__main__':
    app.run(port=3000, debug=True)