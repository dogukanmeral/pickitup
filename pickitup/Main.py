import os
import shutil
import time
import calendar
import json
import argparse

from pickitup.categorize.by_date import by_date
from pickitup.categorize.by_size import by_size
from pickitup.categorize.by_type import by_type
from pickitup.file_operations import is_folder_existing
from pickitup.file_operations import is_file_existing
from pickitup.file_operations import create_folder
from pickitup.file_operations import move_file

def main():
    parser = argparse.ArgumentParser(description='Organize files in a spesific folder.')
    parser.add_argument("folder", type=str, help="Path of the folder containing the files")
    parser.add_argument("organize_type", choices=['s', 'd', 't'], type=str, help="Organizing type (s: by size, d: by date, t: by file type)")
    args = parser.parse_args()

    if not is_folder_existing(args.folder):
        print(f"Specified folder path does not exist: {args.folder}")
        exit()

    files = os.listdir(args.folder)
    
    if args.organize_type == 't':
        files_by_categories = by_type(files, args.folder)
    elif args.organize_type == 'd':
        files_by_categories = by_date(files, args.folder)
    elif args.organize_type == 's':
        files_by_categories = by_size(files, args.folder)

    folders_to_create = [files_by_categories[file] for file in files_by_categories]
    folders_to_create = list(set(folders_to_create)) # delete duplicates

    for folder_path in folders_to_create:
        full_folder_path = os.path.join(args.folder, folder_path)
        
        if not is_folder_existing(full_folder_path):
            create_folder(full_folder_path)

    for file in files_by_categories:
        file_path = os.path.join(args.folder, file)
        new_file_path = os.path.join(args.folder, files_by_categories[file], file)

        if not is_file_existing(new_file_path):
            move_file(file_path, new_file_path)