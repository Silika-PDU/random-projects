import os
import uuid

def sort_and_rename_safely(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    files_with_size = [(f, os.path.getsize(os.path.join(folder_path, f))) for f in files]
    files_sorted = sorted(files_with_size, key=lambda x: x[1], reverse=True)
    temp_names = []

    for filename, _ in files_sorted:
        ext = os.path.splitext(filename)[1]
        temp_name = f"temp_{uuid.uuid4().hex}{ext}"
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, temp_name))
        temp_names.append((temp_name, ext))

    for index, (temp_name, ext) in enumerate(temp_names, start=1):
        final_name = f"{index}{ext}"
        os.rename(os.path.join(folder_path, temp_name), os.path.join(folder_path, final_name))

    print("Files renamed safely without overwriting any existing files.")

folder = input("Enter the folder path: ")
sort_and_rename_safely(folder)