from PIL import Image
import os

def resize_and_compress_images(input_folder, output_folder, max_size=(1800, 1800), max_kb=350):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for img_name in os.listdir(input_folder):
        img_path = os.path.join(input_folder, img_name)
        if not os.path.isfile(img_path):
            continue
        
        img = Image.open(img_path)
        img.thumbnail(max_size, Image.LANCZOS)
        
        quality = 95  # initial quality
        output_path = os.path.join(output_folder, img_name)
        
        while True:
            img.save(output_path, format="JPEG", quality=quality)
            if os.path.getsize(output_path) <= max_kb * 1024 or quality <= 10:
                break
            quality -= 5 
        
        print(f"Imagem processada: {output_path} ({os.path.getsize(output_path) / 1024:.2f} KB)")

resize_and_compress_images("images", "output")
