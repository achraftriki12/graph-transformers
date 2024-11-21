import os
import argparse
from PIL import Image
import numpy as np

def tile_image(input_image_path, output_dir, tile_size, variance_threshold):
    # Load the image
    image = Image.open(input_image_path).convert('L')  # Convert to grayscale to simplify variance calculation
    width, height = image.size

    # Calculate the number of tiles in each dimension
    x_tiles = width // tile_size
    y_tiles = height // tile_size

    # Create tiles
    for i in range(y_tiles):
        for j in range(x_tiles):
            # Define the bounding box for each tile
            left = j * tile_size
            upper = i * tile_size
            right = left + tile_size
            lower = upper + tile_size

            # Crop the image to create the tile
            tile = image.crop((left, upper, right, lower))

            # Convert tile to numpy array and calculate variance
            tile_array = np.array(tile)
            if np.var(tile_array) > variance_threshold:
                # Ensure the output directory exists
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                # Save the tile
                tile.save(os.path.join(output_dir, f"tile_{i}_{j}.jpg"))

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Generate tiles from an image, dropping tiles with low variance.")
    parser.add_argument("input_image", help="Path to the input image")
    parser.add_argument("output_directory", help="Directory where tiles will be saved")
    parser.add_argument("--tile_size", type=int, default=256, help="Size of each tile (default is 256 pixels)")
    parser.add_argument("--variance_threshold", type=float, default=20.0, help="Variance threshold below which tiles will not be saved (default is 20.0)")

    # Parse arguments
    args = parser.parse_args()

    # Run the tiling function
    tile_image(args.input_image, args.output_directory, args.tile_size, args.variance_threshold)

if __name__ == "__main__":
    main()
