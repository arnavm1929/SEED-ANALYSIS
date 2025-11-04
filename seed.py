print("✅ seed.py started")

from ultralytics import YOLO

# Load a pre-trained YOLOv8 model for classification
model = YOLO("yolov8n-cls.pt")

# Train on your dataset
model.train(
    data="VegSeedsBD",   # path to dataset folder
    epochs=10,
    imgsz=224
)

# Validate model
metrics = model.val()
print("Validation metrics:", metrics)
