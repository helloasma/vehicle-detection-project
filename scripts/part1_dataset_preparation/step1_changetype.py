import os
from PIL import Image

root_dir = "."

converted = 0
failed = 0

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith((".jpeg", ".png")):
            jpeg_path = os.path.join(subdir, file)
            jpg_path = os.path.splitext(jpeg_path)[0] + ".jpg"

            try:
                with Image.open(jpeg_path) as img:
                    img = img.convert("RGB")
                    img.save(jpg_path, "JPEG")

                os.remove(jpeg_path)

                print(f"Converted: {jpeg_path}")
                converted += 1

            except Exception as e:
                print(f"Failed: {jpeg_path} -> {e}")
                failed += 1

print("\n--- SUMMARY ---")
print(f"Converted: {converted}")
print(f"Failed: {failed}")