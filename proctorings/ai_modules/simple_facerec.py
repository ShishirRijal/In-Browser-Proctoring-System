import face_recognition
import cv2
import numpy as np
import os

class SimpleFacerec:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        images = os.listdir(images_path)
        for img_name in images:
            img_path = os.path.join(images_path, img_name)
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the face encodings for the face(s) in the image
            face_encodings = face_recognition.face_encodings(rgb_img)

            if len(face_encodings) > 0:
                self.known_face_encodings.append(face_encodings[0])
                self.known_face_names.append(os.path.splitext(img_name)[0])
        print(f"Loaded {len(self.known_face_encodings)} face encodings.")
        print(f"Known faces: {self.known_face_names}")
        
    def detect_known_faces(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=self.frame_resizing, fy=self.frame_resizing)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)

            # Check if face_distances is empty
            if len(face_distances) == 0:
                continue

            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            else:
                name = "Unknown"
            
            face_names.append(name)

        return face_locations, face_names
