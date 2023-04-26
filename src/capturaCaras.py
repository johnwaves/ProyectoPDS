# Importamos las librerias necesarias
import cv2
import os
import time
import uuid

# Numero de imagenes a capturar
NUM_IMAGENES = 10

# Path donde se guardaran las imagenes
DATA_IMG_PATH = os.path.join('data','img')

# Capturamos las imagenes de la camara
def captura_caras(nombre):
    path = os.path.join(DATA_IMG_PATH,nombre)
    if not os.path.exists(path):
        os.mkdir(path)
    captura = cv2.VideoCapture(0)
    print('Obteniendo imagenes para {}'.format(nombre))
    time.sleep(5)
    for num in range(NUM_IMAGENES):
        print('Obteniendo imagen {}'.format(num))
        ret, frame = captura.read()
        imgname = os.path.join(path, nombre+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    captura.release()
    cv2.destroyAllWindows()

captura_caras('fran')