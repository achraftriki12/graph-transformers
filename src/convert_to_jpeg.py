import os
import sys
from PIL import Image

def convert_bmp_to_jpg(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.BMP'):
            # Open the BMP image
            bmp_image_path = os.path.join(input_folder, filename)
            with Image.open(bmp_image_path) as img:
                # Convert the BMP image to JPG format
                jpg_image_path = os.path.join(output_folder, filename[:-4] + '.jpg')
                img.convert('RGB').save(jpg_image_path, 'JPEG')
                print(f'Converted {bmp_image_path} to {jpg_image_path}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    convert_bmp_to_jpg(input_folder, output_folder)
