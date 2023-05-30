from tkinter import *
import os
import cv2
import numpy as np
import face_recognition as fr


#----------------- Calcula el encoding 128 de una imagen dada --------------------------------
def face_encodings(img):
    face_loc = fr.face_locations(img)[0]
    face_encodings = fr.face_encodings(img, known_face_locations=[face_loc])[0]
        
    return face_encodings


#----------------- Compara las imagenes codificadas de dimension 128 usando la distancia euclidea ---------------
def comparar_codif(encod1, encod2, umbral):
     resultado = False
     dist_eucl = np.linalg.norm(encod1 - encod2)  # distancia euclidea normalizada [0,1], cuanto mas cercano al 0, mas similitud

     print(f'Distancia euclidea: {dist_eucl}')

     if(dist_eucl < umbral):
          resultado = True

     return resultado, dist_eucl
    

#------------------------ Crearemos una funcion que se encargara de registrar el usuario ---------------------
def registrar_usuario():
    usuario_info = usuario.get() #Obetnemos la informacion alamcenada en usuario
    contra_info = contra.get() #Obtenemos la informacion almacenada en contra

    archivo = open(usuario_info, "w") #Abriremos la informacion en modo escritura
    archivo.write(usuario_info + "\n")   #escribimos la info
    archivo.write(contra_info)
    archivo.close()

    #Limpiaremos los text variable
    usuario_entrada.delete(0, END)
    contra_entrada.delete(0, END)

    #Ahora le diremos al usuario que su registro ha sido exitoso
    Label(pantalla_reg, text = "Registro Convencional Exitoso", fg = "green", font = ("Calibri",11)).pack()

#--------------------------- Funcion para almacenar el registro facial --------------------------------------
def registro_facial():
    #Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)            
    while(True):
        ret,frame = cap.read()          
        cv2.imshow('Registro Facial',frame)
        if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
            break
    usuario_img = usuario.get()
    cv2.imwrite("../img/"+usuario_img+".jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                          
    cv2.destroyAllWindows()

    usuario_entrada.delete(0, END)
    Label(pantalla_reg, text = "Registro Facial Exitoso", fg = "green", font = ("Calibri",11)).pack()  

    
#----------------------- Funcion para el registro tradicional -----------------------------------
def ventana_reg_tradicional():
    global usuario_entrada
    global contra_entrada
    global pantalla_reg
    pantalla_reg = Toplevel(pantalla1) #Esta pantalla es de un nivel superior a la principal
    pantalla_reg.title("Registro tradicional")
    pantalla_reg.geometry("400x250")

    Label(pantalla_reg, text = "Registro tradicional: debe asignar usuario y contraseña").pack()
    Label(pantalla_reg, text = "").pack()
    Label(pantalla_reg, text = "Usuario * ").pack()  #Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla_reg, textvariable = usuario) #Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()
    Label(pantalla_reg, text = "Contraseña * ").pack()  #Mostramos en la pantalla 1 la contraseña
    contra_entrada = Entry(pantalla_reg, textvariable = contra) #Creamos un text variable para que el usuario ingrese la contra
    contra_entrada.pack()

    Label(pantalla_reg, text = "").pack()  #Dejamos un espacio para la creacion del boton
    Button(pantalla_reg, text = "Registro Tradicional", width = 15, height = 1, command = registrar_usuario).pack()


#----------------------- Funcion para el registro facial -----------------------------------
def ventana_reg_facial():
    global usuario_entrada
    global pantalla_reg
    pantalla_reg = Toplevel(pantalla1) #Esta pantalla es de un nivel superior a la principal
    pantalla_reg.title("Registro facial")
    pantalla_reg.geometry("300x200")

    Label(pantalla_reg, text = "Registro facial: debe asignar un usuario").pack()
    Label(pantalla_reg, text = "").pack()
    Label(pantalla_reg, text = "Usuario * ").pack()  #Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla_reg, textvariable = usuario) #Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()

    # Boton para el registro facial
    Label(pantalla_reg, text = "").pack()
    Button(pantalla_reg, text = "Registro Facial", width = 15, height = 1, command = registro_facial).pack()


#------------------------ Funcion para asignar al boton registro --------------------------------
def registro():
    global usuario
    global contra
    global pantalla1
    pantalla1 = Toplevel(pantalla) #Esta pantalla es de un nivel superior a la principal
    pantalla1.title("Registro")
    pantalla1.geometry("300x150")
    
    
    usuario = StringVar()
    contra = StringVar()

    Label(pantalla1, text="Selecciona un metodo de registro").pack()
    Label(pantalla1, text="").pack()

    Button(pantalla1, text="Registro Tradicional", width = 15, height = 1, command=ventana_reg_tradicional).pack()
    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registro Facial", width = 15, height = 1, command=ventana_reg_facial).pack()
    

#-------------------------- Funcion para verificar los datos ingresados al login ------------------------------------
def verificacion_login():
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()

    usuario_entrada2.delete(0, END)
    contra_entrada2.delete(0, END)

    lista_archivos = os.listdir()   #Vamos a importar la lista de archivos con la libreria os
    if log_usuario in lista_archivos:   #Comparamos los archivos con el que nos interesa
        archivo2 = open(log_usuario, "r")  #Abrimos el archivo en modo lectura
        verificacion = archivo2.read().splitlines()  #leera las lineas dentro del archivo ignorando el resto
        if log_contra in verificacion:
            print("Inicio de sesion exitoso")
            Label(pantalla_log, text = "Inicio de Sesion Exitoso", fg = "green", font = ("Calibri",11)).pack()
        else:
            print("Contraseña incorrecta, ingrese de nuevo")
            Label(pantalla_log, text = "Contraseña Incorrecta", fg = "red", font = ("Calibri",11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla_log, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()


#-------------------------- Funcion para el Login Facial --------------------------------------------------------
def login_facial():
    cap = cv2.VideoCapture(0)
    while(True):
        ret,frame = cap.read()              
        cv2.imshow('Login Facial',frame)         
        if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
            break
    usuario_login = verificacion_usuario.get() 
    cv2.imwrite("../img/"+usuario_login+"LOG.jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                             
    cv2.destroyAllWindows()

    usuario_entrada2.delete(0, END)

        
    # Importamos las imagenes y llamamos la funcion de comparacion

    im_archivos = os.listdir("../img/")   #Vamos a importar la lista de archivos con la libreria os
    if usuario_login+".jpg" in im_archivos:   #Comparamos los archivos con el que nos interesa
        rostro_reg = cv2.imread("../img/"+usuario_login+".jpg")     #Importamos el rostro del registro
        rostro_log = cv2.imread("../img/"+usuario_login+"LOG.jpg")  #Importamos el rostro del inicio de sesion

        rostro_reg_encodings = face_encodings(rostro_reg)
        rostro_log_encodings = face_encodings(rostro_log)
        similitud, porcent = comparar_codif(rostro_reg_encodings, rostro_log_encodings, 0.6)

        if similitud:
            Label(pantalla_log, text = "Inicio de Sesion Exitoso", fg = "green", font = ("Calibri",11)).pack()
            print("Bienvenido al sistema usuario: ",usuario_login)
            print("Compatibilidad con la foto del registro: ", 1-porcent)
        else:
            print("Rostro incorrecto, Verifique su usuario")
            print("Compatibilidad con la foto del registro: ", 1-porcent)
            Label(pantalla_log, text = "Incompatibilidad de rostros", fg = "red", font = ("Calibri",11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla_log, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()


#---------------------- Funcion para el login tradicional ------------------------------------------
def ventana_log_tradicional():
    global usuario_entrada2
    global contra_entrada2
    global pantalla_log
    
    pantalla_log = Toplevel(pantalla2) #Esta pantalla es de un nivel superior a la principal
    pantalla_log.title("Login tradicional")
    pantalla_log.geometry("400x250")
    
    Label(pantalla_log, text="Login tradicional: debe indicar usuario y contraseña").pack()
    Label(pantalla_log, text="").pack()

    Label(pantalla_log, text = "Usuario * ").pack()
    usuario_entrada2 = Entry(pantalla_log, textvariable = verificacion_usuario)
    usuario_entrada2.pack()
    Label(pantalla_log, text = "Contraseña * ").pack()
    contra_entrada2 = Entry(pantalla_log, textvariable = verificacion_contra)
    contra_entrada2.pack()

    Label(pantalla_log, text = "").pack()
    Button(pantalla_log, text = "Inicio de Sesion Tradicional", width = 20, height = 1, command = verificacion_login).pack()



#----------------------- Funcion para el login facial ----------------------------------------------
def ventana_log_facial():
    global usuario_entrada2
    global pantalla_log

    pantalla_log = Toplevel(pantalla2) #Esta pantalla es de un nivel superior a la principal
    pantalla_log.title("Login facial")
    pantalla_log.geometry("300x200")

    Label(pantalla_log, text = "Login facial: debe indicar un usuario").pack()
    Label(pantalla_log, text = "").pack()
    Label(pantalla_log, text = "Usuario * ").pack()  #Mostramos en la pantalla 1 el usuario
    usuario_entrada2 = Entry(pantalla_log, textvariable = verificacion_usuario) #Creamos un text variable para que el usuario ingrese la info
    usuario_entrada2.pack()

    # Boton para el registro facial
    Label(pantalla_log, text = "").pack()
    Button(pantalla_log, text = "Login Facial", width = 15, height = 1, command = login_facial).pack()


#------------------------ Funcion que asignaremos al boton login -------------------------------------------------
def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2
    
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("300x150")   #Creamos la ventana
    
    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()

    Label(pantalla2, text="Selecciona un metodo de inicio de sesion").pack()
    Label(pantalla2, text="").pack()

    Button(pantalla2, text="Login Tradicional", width = 15, height = 1, command=ventana_log_tradicional).pack()
    Label(pantalla2, text="").pack()
    Button(pantalla2, text="Login Facial", width = 15, height = 1, command=ventana_log_facial).pack()
    
        

#------------------------- Funcion de nuestra pantalla principal ------------------------------------------------
def pantalla_principal():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("400x300") 
    pantalla.title("Biometria Facial")
    Label(text = "Login Inteligente", bg = "gray", width = "300", height = "2", font = ("Verdana", 13)).pack() #Asignamos caracteristicas de la ventana
    
    # Botones
    Label(text = "").pack()
    Button(text = "Iniciar Sesion", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Registro", height = "2", width = "30", command = registro).pack()

    pantalla.mainloop()


pantalla_principal()
