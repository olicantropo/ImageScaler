# ImageScaler
This project contains a Python script to automatically resize and compress images, ensuring that their maximum size does not exceed 1800x1800 pixels and 350 KB.

# 🚀 How to Use

1. Install Dependencies
Make sure you have Pillow installed:

pip install pillow

2. Folder Structure

Place the images you want to process inside the images folder.
The script will generate the processed images inside the output folder.

📂 project
 ├── 📂 images  # Original images
 ├── 📂 output  # Processed images
 ├── resize_images.py  # Main script
 ├── README.md  # This file

3. Run the Script

python main.py

# ⚙️ How It Works

The script scans all images inside the images folder.

Resizes them while maintaining the aspect ratio, without exceeding 1800x1800 pixels.

Compresses the file until it reaches 350 KB.

Saves the new version in the output folder.
