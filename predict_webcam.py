from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/classify/train5/weights/best.pt")

# Open webcam and predict in real-time
results = model.predict(source=0, show=True)
