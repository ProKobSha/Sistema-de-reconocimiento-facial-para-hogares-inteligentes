import cv2
import face_recognition
import os
import pickle
import numpy as np

def register_user(name):
    cam = cv2.VideoCapture(0)
    print("Capturando rostro... Presiona 'q' para guardar")
    while True:
        ret, frame = cam.read()
        cv2.imshow("Captura", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

   
    image_path = f"dataset/{name}.jpg"
    cv2.imwrite(image_path, frame)


    image = face_recognition.load_image_file(image_path)
    encodings = face_recognition.face_encodings(image)
    if len(encodings) == 0:
        print("No se detectó ningún rostro.")
        return

  
    if os.path.exists("encodings/embeddings.pkl"):
        with open("encodings/embeddings.pkl", "rb") as f:
            data = pickle.load(f)
    else:
        data = {}

    data[name] = encodings[0]

    with open("encodings/embeddings.pkl", "wb") as f:
        pickle.dump(data, f)

    print("Usuario registrado exitosamente.")
