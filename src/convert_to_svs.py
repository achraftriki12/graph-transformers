import os
import sys
from PIL import Image
import tifffile as tiff
import numpy as np

def convert_bmp_to_svs(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.BMP'):
            # Open the BMP image
            bmp_image_path = os.path.join(input_folder, filename)
            with Image.open(bmp_image_path) as img:
                # Convert the BMP image to RGB
                img = img.convert('RGB')

                # Create a TIFF file with the same name but .svs extension
                svs_image_path = os.path.join(output_folder, filename[:-4] + '.svs')

                # Save the image as a TIFF file that mimics SVS format
                img_array = np.array(img)
                tiff.imwrite(svs_image_path, img_array, photometric='rgb')
                
                print(f'Converted {bmp_image_path} to {svs_image_path}')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    convert_bmp_to_svs(input_folder, output_folder)
