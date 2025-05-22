import cv2
import face_recognition
import pickle
import numpy as np

def recognize_user():
    with open("encodings/embeddings.pkl", "rb") as f:
        data = pickle.load(f)

    known_names = list(data.keys())
    known_encodings = list(data.values())

    cam = cv2.VideoCapture(0)
    print("Muestra tu rostro para autenticar. Presiona 'q' para verificar.")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Reconocimiento", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_encodings(rgb_frame)

    if not faces:
        print("No se detectó ningún rostro.")
        return

    face = faces[0]
    distances = face_recognition.face_distance(known_encodings, face)
    min_distance = min(distances)
    min_index = np.argmin(distances)

    if min_distance < 0.5:
        print(f"Bienvenido, {known_names[min_index]}!")
    else:
        print("Rostro no reconocido. Acceso denegado.")
