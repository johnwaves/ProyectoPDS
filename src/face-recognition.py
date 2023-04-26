#
# https://omes-va.com/face-recognition-python/
#
# pip install face-recognition
# pip install opencv-contrib-python

import cv2
import face_recognition as fr

def identificar (ruta_foto, nombre):
     
     # imagen a comparar
     image = cv2.imread(ruta_foto)
     face_loc = fr.face_locations(image)[0]
     face_image_encodings = fr.face_encodings(image, known_face_locations=[face_loc])[0]
     '''
     cv2.rectangle(image, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (0, 255, 0))
     cv2.imshow("Image", image)
     cv2.waitKey(0)
     cv2.destroyAllWindows()
     '''

     # Video Streaming
     cap = cv2.VideoCapture(0)
     while True:
          ret, frame = cap.read()
          if ret == False: break
          frame = cv2.flip(frame, 1)

          face_locations = fr.face_locations(frame, model="cnn")
          
          if face_locations != []:
               for face_location in face_locations:
                    face_frame_encodings = fr.face_encodings(frame, known_face_locations=[face_location])[0]
                    result = fr.compare_faces([face_image_encodings], face_frame_encodings)
                    #print("Result:", result)
                    if result[0] == True:
                         text = nombre
                         color = (125, 220, 0)
                    else:
                         text = "Desconocido"
                         color = (50, 50, 255)
                    cv2.rectangle(frame, (face_location[3], face_location[2]), (face_location[1], face_location[2] + 30), color, -1)
                    cv2.rectangle(frame, (face_location[3], face_location[0]), (face_location[1], face_location[2]), color, 2)
                    cv2.putText(frame, text, (face_location[3], face_location[2] + 20), 2, 0.7, (255, 255, 255), 1)
          
          cv2.imshow("Frame", frame)
          k = cv2.waitKey(1)
          if k == 27 & 0xFF:
               break

     cap.release()
     cv2.destroyAllWindows()

foto = "../images/manolo.jpg"
nombre = "Manolo"
identificar(foto, nombre)