import os
import shutil
import time
import calendar
import json
import argparse

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
        files_by_categories = by_type(files)
    elif args.organize_type == 'd':
        files_by_categories = by_date(files, args.folder)
    elif args.organize_type == 's':
        files_by_categories = by_size(files)

    folders_to_create = [files_by_categories[file] for file in files_by_categories]
    folders_to_create = list(set(folders_to_create)) # delete duplicates

    # FIND A CONSISTENT WAY TO CREATE PATHS