# Base de datos local (de prueba): almacenará los datos de los usuarios para
# poder identificarlos y hacer el matching.

# 1. Creación de la base de datos.
# Lista que contendrá los diccionarios, y cada diccionario almacenará los datos
# de los usuarios que se registran en la aplicación.
usuarios = []

# Añadimos los diccionarios a la lista
usuarios.append({'nombre': 'emilio', 'dni': '23245678G', 'email': 'emilio@mail.es'})
usuarios.append({'nombre': 'eustaquio', 'dni': 'X0672135T', 'email': 'eustaquio@mail.es'})

# 2. Emparejaiento de resultados.
# Se busca el usuario en la base de datos a partir de lo reconocido por la cámara.
def matching_results(nombre):
    
    coincide = False
    
    for usuario in usuarios:
        if (usuario['nombre'] == nombre):
            coincide = True
        
    return coincide

# 3. Mostrar datos del usuario.
def show_userdata(nombre):
    
    for usuario in usuarios:
        if (usuario['nombre'] == nombre):
            text = '\nSe ha encontrado el usuario. Sus datos son:'
            text += '\n - Nombre: ' + usuario['nombre']
            text += '\n - DNI: ' + usuario['dni']
            text += '\n - Email: ' + usuario['email']
            text += '\n'
            print(text)    
            
    # NOTA: se muestran estos datos en la consola para verificar su correcto
    # funcionamiento. Próximamente esta función desaparecerá para poder 
    # adecuarlo a los requisitos del proyecto.

def show_error():
    print('\nERROR: No se ha encontrado el usuario en la base de datos.\n')
    
# Pruebas
nombre = 'emilio'
if matching_results(nombre):
    show_userdata(nombre)
else: 
    show_error()



