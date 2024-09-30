import cv2
import numpy as np
from ultralytics import YOLO

# Initialize the YOLOv8 model
model = YOLO('yolov8n.pt')  # Choose the model variant (e.g., yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.)

def detectObject(frame):
    labels_this_frame = []

    # Perform object detection
    results = model(frame)

    for result in results:
        for box in result.boxes.data.cpu().numpy():
            x1, y1, x2, y2, score, class_id = box

            if score > 0.5:  # Confidence threshold
                label = model.names[int(class_id)]
                labels_this_frame.append((label, float(score)))

                # Draw bounding box in blue
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                # Draw label and confidence value in red
                cv2.putText(frame, f"{label} {score:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return labels_this_frame

# # Test the object detection with the updated features
# if __name__ == "__main__":
#     cap = cv2.VideoCapture(0)

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         labels = detectObject(frame)
#         cv2.imshow("Object Detection", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()