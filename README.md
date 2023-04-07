# ProyectoPDS

1. Resumen del proyecto.
La idea es implementar un sistema de inicio de sesión mediante el reconocimiento facial del usuario. El modelo procederá a reconocer la persona mediante un previo entrenamiento con imágenes precargadas de la misma.

Objetivos:

●      Reconocer a la persona cuando esta lleve accesorios (gafas, mascarilla…).

●      Reconocimiento en condiciones de iluminación escasa. 

●      Reconocimiento cuando la persona está orientada de forma diferente a las imágenes precargadas.

Adicionalmente, y en caso de disponer de suficiente tiempo, se podría añadir un sistema complementario de autenticación mediante voz, donde el usuario pronunciaría en voz alta una palabra. De esta forma, el sistema reconocería su voz comparándolo con un patrón previamente cargado, al igual que ocurre en el sistema de imágenes.


2. Requisitos funcionales.
●      Captura de imágenes: La aplicación debe permitir la captura de imágenes de alta calidad de caras desde diferentes ángulos y con diferentes iluminaciones.

●      Preprocesamiento de imágenes: La aplicación debe ser capaz de procesar las imágenes de entrada para mejorar la calidad de la imagen y eliminar el ruido, garantizando la precisión del reconocimiento.

●      Detección de caras: La aplicación debe ser capaz de detectar caras en imágenes de entrada.

●      Extracción de características: La aplicación debe ser capaz de extraer características de la cara detectada, como la posición y forma de los ojos, nariz, boca, etc.

●      Comparación de características: La aplicación debe ser capaz de comparar las características extraídas de la cara detectada con las características almacenadas en una base de datos para identificar a la persona.

●      Verificación y autenticación: La aplicación debe ser capaz de verificar la identidad de una persona comparando su cara con la información almacenada en la base de datos.

3.    Bibliografía
-        https://docs.opencv.org/3.4/da/d60/tutorial_face_main.html

-        https://pyimagesearch.com/2018/09/24/opencv-face-recognition/

-        https://datagen.tech/guides/face-recognition/face-recognition-with-python/

-        Build a Python Facial Recognition App

NOTA: Esta lista se irá actualizando conforme se vaya desarrollando el sistema. Más adelante se añadirán o modificarán las referencias usadas.
