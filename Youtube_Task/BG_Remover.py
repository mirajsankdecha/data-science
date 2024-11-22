from rembg import remove
from PIL import Image
import os

# Paths
input_path = r"E:\python\Youtube_Task\img.jpg"
output_path = r"E:\python\Youtube_Task\output_img.png"

# Check if the file exists
if not os.path.exists(input_path):
    raise FileNotFoundError(f"File not found: {input_path}")

# Try opening the image
try:
    inp = Image.open(input_path)
    inp.verify()  # Check if the image is valid
    inp = Image.open(input_path)  # Reload after verification
    output = remove(inp)
    output.save(output_path)
    print(f"Processed image saved at: {output_path}")
except Exception as e:
    print(f"Error processing image: {e}")
