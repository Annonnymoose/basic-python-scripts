import os
import shutil
import traceback

fl = input("enter the folder name (Folder name's first letter should be big): ")

FolderToMoveFrom = os.path.join(r"C:\Users\bhagw", fl)
if not os.path.exists(FolderToMoveFrom):
    print(f"Error: The folder {FolderToMoveFrom} doesn't exists!!")
    exit()

textFolder = r"C:\Users\bhagw\Desktop\TextFiles"
pdfFolder = r"C:\Users\bhagw\Documents\PDFs"

if not os.path.exists(textFolder):
    os.makedirs(textFolder)
    print(f"Created Folder : {textFolder}")
if not os.path.exists(pdfFolder):
    os.makedirs(pdfFolder)
    print(f"Created Folder: {pdfFolder}")

for filename in os.listdir(FolderToMoveFrom):
    if filename.lower().endswith(".txt"):
        source_path = os.path.join(FolderToMoveFrom, filename)
        if os.path.isfile(source_path):
            choice = input(f"Found a text file {filename}. Move it? (y/n): ")

            if choice.lower() == 'y':
                destination_path = os.path.join(textFolder, filename)

                if os.path.exists(destination_path):
                    name, extension = os.path.splitext(filename)
                    new_fileName = input(f"Naming Conflict!! \n File Name: {filename}\n Rename it to: ")
                    lst = ['\\', '/', ':', '*', '?', '"', '<', '>', '|']
                    is_safe = True
                    for i in new_fileName:
                        if i in lst:
                            print(f"Illegal character in Renaming {i}")
                            is_safe = False
                            break
                    if not is_safe:
                        continue
                    destination_path = os.path.join(textFolder, new_fileName + extension)

                try:
                    shutil.move(source_path, destination_path)
                    print(f"Success: Moved {filename} to {destination_path}")

                except PermissionError:
                    print(f"Error: Skipped '{filename}'. It is currently opened/locked by another program \n")

                except FileNotFoundError:
                    print(f"Error: '{filename}' was not found!\n")

                except Exception as e:
                    print(f"An unexpected error occurred with '{filename}': {e}\n")
                    traceback.print_exc()

            else:
                print("Skipped.\n")


        elif filename.lower().endswith(".pdf"):
            source_path = os.path.join(FolderToMoveFrom, filename)
            if os.path.isfile(source_path):
                choice = input(f"Found a pdf file {filename}. Move it? (y/n): ")

                if choice.lower() == 'y':
                    destination_path = os.path.join(pdfFolder, filename)

                    if os.path.exists(destination_path):
                        name, extension = os.path.splitext(filename)
                        new_fileName = input(f"Naming Conflict!! \n File Name: {filename}\n Rename it to: ")
                        lst = ['\\','/', ':', '*','?','"', '<', '>', '|']
                        is_safe = True
                        for i in new_fileName:
                            if i in lst:
                                print(f"Illegal character in Renaming {i}")
                                is_safe = False
                                break
                        if not is_safe:
                            continue
                        destination_path = os.path.join(pdfFolder, new_fileName + extension)

                    try:
                        shutil.move(source_path, destination_path)
                        print(f"Success: Moved {filename} to {destination_path}")

                    except PermissionError:
                        print(f"Error: Skipped '{filename}'. It is currently opened/locked by another program \n")

                    except FileNotFoundError:
                        print(f"Error: '{filename}' was not found!\n")

                    except Exception as e:
                        print(f"An unexpected error occurred with '{filename}': {e}\n")
                        traceback.print_exc()

            else:
                print("Skipped.\n")