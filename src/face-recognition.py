#
# https://omes-va.com/face-recognition-python/
#
# pip install face-recognition
# pip install opencv-contrib-python

import numpy as np
import cv2
import face_recognition as fr
import imutils

# compara las imagenes codificadas de dimension 128 usando la distancia euclidea
def comparar_codif(encod1, encod2, umbral):
     resultado = False
     dist_eucl = np.linalg.norm(encod1 - encod2)  # distancia euclidea normalizada [0,1], cuanto mas cercano al 0, mas similitud

     print(f'Distancia euclidea: {dist_eucl}')

     if(dist_eucl < umbral):
          resultado = True

     return resultado


def identificar (ruta_foto, nombre):
     
     # imagen a comparar
     imagen = cv2.imread(ruta_foto)
     face_loc = fr.face_locations(imagen)[0]       # devuelve la localización de la cara que detecta en la imagen
     face_image_encodings = fr.face_encodings(imagen, known_face_locations=[face_loc])[0]       # devuelve la codificación facial en dimensión 128 de la imagen dada, sabiendo la localización de la cara

     # cv2.rectangle(image, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 255, 0))
     # cv2.imshow("Image", image)

     cap = cv2.VideoCapture(0)
     while True:
          ret, frame = cap.read()
          if ret == False: break
          frame = cv2.flip(frame, 1)
          frame = imutils.resize(frame, width=150)          # a la hora de realizar calculos sobre el frame => width=150

          face_locations = fr.face_locations(frame)         # devuelve el array de la localización de la cara en un frame concreto
          print(face_locations)

          if face_locations != []:
               for face_location in face_locations:
                    face_frame_encodings = fr.face_encodings(frame, known_face_locations=[face_location])[0]       # codificamos el frame a 128 dimensiones, sabiendo la localización de la cara
                    
                    # comparar imagen con frame
                    # si el resultado es True: printear rectangulo verde y el nombre
                    # si no, printear rectangulo rojo y nombre desconocido
                    
                    resultado = comparar_codif(face_image_encodings, face_frame_encodings, 0.6)
                    if resultado == True:
                         texto = nombre
                         color = (0, 255, 0)
                    else:
                         texto = "Desconocido"
                         color = (0, 0, 255)

                    cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
                    cv2.putText(frame, texto, (face_location[3], face_location[2] + 20), 1, 0.7, (255, 255, 255), 1)

          frame = imutils.resize(frame, width=500)          # cuando mostramos el frame => widht=500
          cv2.imshow("Frame", frame)
          k = cv2.waitKey(1)       
          if k == 27 & 0xFF:       # SALIR PULSANDO ESC
               break

     cap.release()
     cv2.destroyAllWindows()



# -------------------------------------------------------------

foto = "../img/manolo.jpg"
nombre = "Manolo"
identificar(foto, nombre)     # SALIR PULSANDO ESC