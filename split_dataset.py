import os
import shutil
import random
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)


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
        continue  # skip non-folders

    # Collect only image files
    images = [f for f in os.listdir(class_path) 
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    # Shuffle images
    random.shuffle(images)

    # Split
    n_total = len(images)
    n_train = int(n_total * train_split)
    n_val = int(n_total * val_split)

    train_files = images[:n_train]
    val_files = images[n_train:n_train + n_val]
    test_files = images[n_train + n_val:]

    # Copy files into train/val/test
    for split, files in zip(["train", "val", "test"], [train_files, val_files, test_files]):
        split_class_dir = os.path.join(output_dir, split, class_name)
        os.makedirs(split_class_dir, exist_ok=True)
        for f in files:
            src = os.path.join(class_path, f)
            dst = os.path.join(split_class_dir, f)
            shutil.copy(src, dst)

print("✅ Dataset split completed!")
