from .simple_facerec import SimpleFacerec
from django.contrib.auth import login
from django.contrib.auth.models import User
import cv2
from django.http import StreamingHttpResponse

sfr = SimpleFacerec()
sfr.load_encoding_images("C:/Users/Angel/OneDrive/Desktop/InBrowserProctoring/proctoring_systems/media/photos")


def gen_frames(camera, request):  # Generator function to yield frames
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Detect faces and encode known faces
        face_locations, face_names = sfr.detect_known_faces(frame)

        # Draw rectangles around recognized faces and label them
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    camera = cv2.VideoCapture(0)  # Use the webcam
    return StreamingHttpResponse(gen_frames(camera, request),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
