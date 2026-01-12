import os, shutil, random

src = "VegSeedsBD_flat"
dst = "VegSeedsBD"

splits = {"train": 0.7, "val": 0.15, "test": 0.15}

for s in splits:
    os.makedirs(os.path.join(dst, s), exist_ok=True)

for cls in os.listdir(src):
    class_path = os.path.join(src, cls)
    if not os.path.isdir(class_path): continue

    images = [img for img in os.listdir(class_path) if img.lower().endswith(("jpg","jpeg","png"))]
    random.shuffle(images)

    total = len(images)
    n_train = int(total * splits["train"])
    n_val = int(total * splits["val"])

    mapping = {
        "train": images[:n_train],
        "val": images[n_train:n_train+n_val],
        "test": images[n_train+n_val:]
    }

    for split, img_list in mapping.items():
        split_dir = os.path.join(dst, split, cls)
        os.makedirs(split_dir, exist_ok=True)

        for img in img_list:
            shutil.copy(os.path.join(class_path, img), os.path.join(split_dir, img))

print("\n🚀 Dataset split complete!")
