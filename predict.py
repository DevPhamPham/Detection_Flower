import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path
import numpy as np
import os
from ultralytics import YOLO

# Load the trained model
model_path = "./runs/detect/train3/weights/best.pt"
model = YOLO(model_path)  # Load the trained model

# Path to the image
# image_path = "./data/images/train/Screenshot 2024-03-21 235403.png"
image_path = "./test3.png"

# Load image using PIL
image_pil = Image.open(image_path)

# # Convert RGBA image to RGB if it has alpha channel
if image_pil.mode == 'RGBA':
    image_pil = image_pil.convert('RGB')

image = np.array(image_pil)  # Convert to NumPy array

# Detect objects in the image
results = model(image)[0]  # Detect objects in the image
threshold = 0
class_names = ["Hoa Dao", "Hoa Mai"]
fig, ax = plt.subplots()
ax.imshow(image)
print(results.boxes.data.tolist())
for result in results.boxes.data.tolist():
    x1, y1, x2, y2, score, class_id = result
    if score > threshold:
        # Draw bounding box
        rect = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=2, edgecolor='g', facecolor='none')
        ax.add_patch(rect)
        # Add label
        ax.text(x1, y1 - 10, class_names[int(class_id)].upper()+" "+ str(format(score,'.2f')) , fontsize=12, color='g')
plt.axis('off')  # Turn off axis
plt.show()
