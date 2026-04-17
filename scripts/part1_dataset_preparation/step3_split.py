import os
import random
import shutil

random.seed(42)

SOURCE_DIR = "cleaned_images"

classes = ["bus", "car", "motorcycle", "truck"]

TRAIN_COUNT = 180
VAL_COUNT = 20
TEST_COUNT = 20

# Create folders
for split in ["train", "val", "test"]:
    os.makedirs(os.path.join(split, "images"), exist_ok=True)

for cls in classes:
    print(f"\nProcessing {cls}")

    class_path = os.path.join(SOURCE_DIR, cls)
    images = os.listdir(class_path)

    random.shuffle(images)

    train_images = images[:TRAIN_COUNT]
    val_images = images[TRAIN_COUNT:TRAIN_COUNT + VAL_COUNT]
    test_images = images[TRAIN_COUNT + VAL_COUNT:TRAIN_COUNT + VAL_COUNT + TEST_COUNT]

    for img in train_images:
        shutil.copy(
            os.path.join(class_path, img),
            os.path.join("train/images", img)
        )

    for img in val_images:
        shutil.copy(
            os.path.join(class_path, img),
            os.path.join("val/images", img)
        )

    for img in test_images:
        shutil.copy(
            os.path.join(class_path, img),
            os.path.join("test/images", img)
        )

    print(f"{cls}: Train={len(train_images)}, Val={len(val_images)}, Test={len(test_images)}")

print("\nDataset split completed successfully!")