
from ultralytics import YOLO
model = YOLO("runs/classify/train5/weights/best.pt")

results = model(r"C:\Users\mahesam\OneDrive - Tecnotree\Documents\DLBASP\VegSeedsBD_raw\Bitter Gourd\Single\IMG20241222140544.jpg")
print(results[0].probs)
results[0].show()
