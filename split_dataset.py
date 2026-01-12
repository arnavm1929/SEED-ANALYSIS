import os
import shutil
import random

# Paths
raw_data_dir = "VegSeedsBD_raw"
output_dir = "VegSeedsBD"

# Train/val/test split ratios
train_split = 0.7
val_split = 0.15
test_split = 0.15

# Ensure output dirs exist
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(output_dir, split), exist_ok=True)

# Loop through each class folder
for class_name in os.listdir(raw_data_dir):
    class_path = os.path.join(raw_data_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    # Recursively collect all image files inside this class
    images = []
    for root, dirs, files in os.walk(class_path):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg", ".png")):
                images.append(os.path.join(root, f))

    if len(images) == 0:
        print(f"⚠ WARNING: No images found for class: {class_name}")
        continue

    random.shuffle(images)

    # Compute splits
    n_total = len(images)
    n_train = int(n_total * train_split)
    n_val = int(n_total * val_split)

    train_files = images[:n_train]
    val_files = images[n_train:n_train + n_val]
    test_files = images[n_train + n_val:]

    # Copy files into train/val/test/<class>
    for split, file_list in zip(["train", "val", "test"], [train_files, val_files, test_files]):
        out_dir = os.path.join(output_dir, split, class_name)
        os.makedirs(out_dir, exist_ok=True)

        for src in file_list:
            dst = os.path.join(out_dir, os.path.basename(src))
            shutil.copy(src, dst)

print("✅ Dataset split completed successfully using recursive search!")
