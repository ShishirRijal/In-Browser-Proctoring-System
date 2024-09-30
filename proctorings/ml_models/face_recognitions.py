from .simple_facerec import SimpleFacerec
from django.contrib.auth import login
from django.contrib.auth.models import User
import cv2
from django.http import StreamingHttpResponse

sfr = SimpleFacerec()
sfr.load_encoding_images("C:/Users/Angel/OneDrive/Desktop/InBrowserProctoring/proctoring_systems/media/photos")

def gen_frames(camera, request):  # Generator function to yield frames
    name = "No face detected"  # Initialize name with a default value
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Detect faces and encode known faces
        face_locations, face_names = sfr.detect_known_faces(frame)

        if face_names:  # If any face is detected
            name = face_names[0]  # Assuming you're only interested in the first detected face
            # Initialize a list in the session if not already present
            if 'recognized_names' not in request.session:
                request.session['recognized_names'] = []

            # Append the recognized name to the session list if it's not already in the list
            if name not in request.session['recognized_names']:
                request.session['recognized_names'].append(name)

            # Save the updated list back to the session
            request.session.modified = True

        # Draw rectangles around recognized faces and label them
        for (top, right, bottom, left), name_in_frame in zip(face_locations, face_names):
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name_in_frame, (left+6, bottom-6), font, 1, (0,0,255), 2)

        # Encode the frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame and recognized name
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

