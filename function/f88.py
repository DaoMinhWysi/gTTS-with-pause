import os
from pathlib import Path
def mFolder(folder_path):
    folder_path = Path(folder_path)
    if not os.path.isdir(folder_path):
        os.makedirs(folder_path)
def mFile(file_path,content):
   file_path = Path(file_path)
   if not os.path.isfile(file_path):
    with open(file_path, 'w') as f:
     f.write(content)
def count_files(folder_path):
    folder_path = Path(folder_path)
    file_count = 0
    for _, _, files in os.walk(folder_path):
        file_count += len(files)
    return file_count
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')