from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("best.pt") 

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open webcam")
    exit()

print("Press SPACE to capture an image, or Q to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    cv2.imshow("Webcam - Press SPACE to Capture", frame)

    key = cv2.waitKey(1)

    if key % 256 == 32:  # SPACE pressed
        # Run prediction on captured frame
        results = model.predict(frame)

        # Get top prediction
        probs = results[0].probs
        top_class = probs.top1
        top_conf = probs.top1conf

        label = f"{results[0].names[top_class]} ({top_conf:.2f})"

        # Overlay prediction on the image
        cv2.putText(frame, label, (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("Prediction", frame)

        print(f"✅ Prediction: {label}")

        # Wait until key press to close the prediction window
        cv2.waitKey(0)
        cv2.destroyWindow("Prediction")

    elif key % 256 == ord('q'):  # Quit with Q
        break

cap.release()
cv2.destroyAllWindows()
