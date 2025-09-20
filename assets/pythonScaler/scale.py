import os
from PIL import Image

# List of portfolio folders to process
folders = [
    "aws",
    "azure",
    "expresslink",
    "greengrass",
    "microRos",
    "paccar",
    "rover"
]

root_dir = "../"
max_width = 1200
max_height = 800

for folder in folders:
    folder_path = os.path.join(root_dir, folder)
    if os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                img_path = os.path.join(folder_path, filename)
                with Image.open(img_path) as img:
                    img.thumbnail((max_width, max_height), Image.LANCZOS)
                    if img.mode == "RGBA" and img_path.lower().endswith((".jpg", ".jpeg")):
                        img = img.convert("RGB")
                    img.save(img_path)
                    print(f"Scaled {img_path}")

print("All selected images have been scaled.")