#!/usr/bin/env python3


import os
from PIL import Image

def compress_images_in_directory(directory, quality=85):
    # Make sure the specified directory exists
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    # Traverse the directory and process each image file
    for filename in os.listdir(directory):
        if filename.lower().endswith('.png'):
            # Full path of the original image
            image_path = os.path.join(directory, filename)
            # Create a new filename for the compressed image
            compressed_image_path = os.path.join(directory, f"compressed_{filename}")

            try:
                # Open the image
                with Image.open(image_path) as img:
                    # Compress and save the image with reduced quality
                    img.save(compressed_image_path, optimize=True, quality=quality)
                    print(f"Compressed image saved as: {compressed_image_path}")
            except Exception as e:
                print(f"Failed to compress {filename}: {e}")

if __name__ == "__main__":
    # Specify the directory containing the images
    directory = '/home/rkadmin/01_Projects/netbox/Device-Type-Library-Import/repo/elevation-images/MikroTik/'
    # Call the function to compress images
    compress_images_in_directory(directory)
