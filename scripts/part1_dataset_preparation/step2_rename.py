import os

base_path = "cleaned_images"
#base_path = "test"

for class_name in os.listdir(base_path):
    class_folder = os.path.join(base_path, class_name)

    if not os.path.isdir(class_folder):
        continue

    print(f"Processing folder: {class_name}")

    # ONLY pick .jpg files
    files = [f for f in os.listdir(class_folder) if f.lower().endswith(".jpg")]
    files = sorted(files)

    temp_paths = []

    # STEP 1: rename to temporary names
    for i, file in enumerate(files):
        old_path = os.path.join(class_folder, file)

        ext = os.path.splitext(file)[1]
        temp_name = f"temp_{i}{ext}"
        temp_path = os.path.join(class_folder, temp_name)

        os.rename(old_path, temp_path)
        temp_paths.append(temp_path)

    # STEP 2: rename to final names
    count = 1
    for temp_path in temp_paths:
        ext = os.path.splitext(temp_path)[1]
        new_name = f"{class_name}_{count}{ext}"
        new_path = os.path.join(class_folder, new_name)

        os.rename(temp_path, new_path)
        count += 1

print("All JPG files renamed successfully!")