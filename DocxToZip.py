import os
import zipfile


def crack_word_doc(file_path):
    print(f"Cracking open: {file_path}")

    # 1. Make sure it's actually a .docx file
    if not file_path.lower().endswith(".docx"):
        print("Error: This script only works on .docx files.")
        return

    # 2. Figure out the new paths
    name, extension = os.path.splitext(file_path)
    zip_path = f"{name}.zip"
    extract_folder = f"{name}_Extracted_XML"

    try:
        # 3. Rename the .docx to .zip using the 'os' module
        os.rename(file_path, zip_path)
        print(f"Successfully converted to {zip_path}")

        # 4. Extract the contents using the 'zipfile' module
        print(f"Extracting XML files to folder: {extract_folder}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)

        print("\nSuccess! The Word document has been unzipped.")
        print(f"Go check the '{extract_folder}' folder to see the hidden XML files!")

    except Exception as e:
        print(f"An error occurred: {e}")


# --- Main Logic ---
if __name__ == "__main__":
    target_file = input("Enter the path to your .docx file (USE A COPY!): ").strip('"')

    if os.path.exists(target_file):
        crack_word_doc(target_file)
    else:
        print("File not found.")