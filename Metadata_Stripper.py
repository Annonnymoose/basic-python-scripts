import os
from PIL import Image

import traceback

def clean_image_metadata(file_path):
    print(f"Analyzing {file_path}...")

    try:
        image = Image.open(file_path)

        #2. Extract ONLY the Pixel data not EXIF
        clean_data = list(image.getdata())

        #3. Create a new, blank image with the exact same dimension
        clean_image = Image.new(image.mode, image.size)

        #4. Paste the pure pixel data into the new blank image
        clean_image.putdata(clean_data)

        #5. A new name for the clean file
        name, extension = os.path.splitext(file_path)
        clean_path = f"{name}_clean{extension}"

        #6. save the new metadata free image
        clean_image.save(clean_path)
        print(f"Success! Clean file saved as: {clean_path}\n")

    except Exception as e:
        print(f"Failed to clean {file_path}. Error {e}")

if __name__ == "__main__":
    target_file = input("Enter the full path of the file you want to scrub\n Or you can drag and drop the image in the terminal : ")
    target_file = target_file.strip('"')

    if os.path.exists(target_file):
        if target_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            clean_image_metadata(target_file)
        else:
            print("Error: This module currently only supports jpg, jpeg, and png file")
    else:
        print("Error: File not found. Check the path and try again")