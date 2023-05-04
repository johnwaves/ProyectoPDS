import cv2
import dlib
import numpy as np
import sqlite3
from db import add_user, verify_user

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
predictor_path = "shape_predictor_68_face_landmarks.dat"
predictor = dlib.shape_predictor(predictor_path)
face_recognition_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

def capture_face():
    cap = cv2.VideoCapture(0)
    face_descriptor = None

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        face_detected = False
        for (x, y, w, h) in faces[:1]:
            face_detected = True
            rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
            shape = predictor(gray, rect)
            face_descriptor = np.array(face_recognition_model.compute_face_descriptor(frame, shape))
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        if face_detected:
            print("Cara detectada.")
        else:
            print("No se detectó ninguna cara.")

        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    return face_descriptor


def compare_face_descriptors(descriptor1, descriptor2, threshold=0.6):
    if descriptor1 is None or descriptor2 is None:
        return False
    distance = np.linalg.norm(descriptor1 - descriptor2)
    return distance < threshold

def get_face_descriptor_by_username(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT face_descriptor FROM users WHERE username=?", (username,))
    row = c.fetchone()
    conn.close()

    if row:
        return np.frombuffer(row[0], dtype=np.float64)
    return None

def register(username, password):
    print("Por favor, mire a la cámara para registrar su rostro.")
    face_descriptor = capture_face()

    if face_descriptor is not None:
        add_user(username, password, face_descriptor)
        print("Registro exitoso.")
    else:
        print("No se pudo registrar el rostro. Intente de nuevo.")

def authenticate(username, password):
    user = verify_user(username, password)

    if user:
        print("Usuario y contraseña verificados. Ahora verificando el rostro.")
        face_descriptor = capture_face()
        stored_face_descriptor = get_face_descriptor_by_username(username)

        if compare_face_descriptors(face_descriptor, stored_face_descriptor):
            print("Autenticación exitosa.")
        else:
            print("Error en la autenticación facial. Acceso denegado.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Registrarse")
        print("2. Autenticarse")
        print("3. Salir")
        choice = input("> ")

        if choice == '1':
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            register(username, password)
        elif choice == '2':
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            authenticate(username, password)
        elif choice == '3':
            break
        else:
            print("Opción no válida.")

if __name__ == '__main__':
    main()

main()

