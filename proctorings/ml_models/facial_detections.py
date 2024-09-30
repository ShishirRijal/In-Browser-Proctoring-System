import dlib
import cv2
from imutils import face_utils

# Path to the pre-trained shape predictor model for facial landmarks
shapePredictorModel = 'shape_predictor_model/shape_predictor_68_face_landmarks.dat'

# Initialize the shape predictor from dlib using the pre-trained model
shapePredictor = dlib.shape_predictor(shapePredictorModel)

def detectFace(frame):
    """
    Input: It will receive a video frame, from the front camera
    Output: Returns the count of faces (detect all the faces and localize them) detected by dlib's face detector
    """
    # Converting 3-channel images to 1-channel image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Initialize the face detector from dlib 
    faceDetector = dlib.get_frontal_face_detector()
    
    # Detect faces in the grayscale frame
    faces = faceDetector(gray, 0)

    # Count the number of faces detected
    faceCount = len(faces)

    # Iterate through each detected face
    for face in faces:
        # Extract the bounding box coordinates for each face
        x, y, w, h = face.left(), face.top(), face.width(), face.height()

        # Draw bounding box around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Determine the facial landmarks for the face region
        facialLandmarks = shapePredictor(gray, face)

        # Convert the facial landmark (x, y) coordinates to a numpy array
        facialLandmarks = face_utils.shape_to_np(facialLandmarks)

        for (a, b) in facialLandmarks:
            # Draw the circle on the face
            cv2.circle(frame, (a, b), 2, (255, 255, 0), -1)

    # Display an alert message if more than one face is detected
    if faceCount > 1:
        cv2.putText(frame, 'Alert: Multiple Faces Detected!', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    return (faceCount, faces)



# Test the facial detection with the updated features
# if __name__ == "_main_":
#     cap = cv2.VideoCapture(0)
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         faceCount, faces = detectFace(frame)
#         cv2.imshow('Facial Detection', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     cap.release()
#     cv2.destroyAllWindows()
