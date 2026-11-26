
# Duplicate File Cleaner - Automated Duplicate Detection System

## Description
A Python-based automation tool designed to identify and remove duplicate files from a specified directory using MD5 checksum comparison. The application scans directories and subdirectories, calculates file checksums, identifies duplicate files, and automatically removes redundant copies while preserving one original file.

## Features
- Scans directories and subdirectories recursively.
- Calculates MD5 checksums using the hashlib module.
- Identifies duplicate files based on file content.
- Automatically deletes duplicate copies while retaining one copy.
- Displays the total number of deleted duplicate files.
- Supports automated file management through Python scripting.

## Technologies Used
- Python
- OS Module
- hashlib
- sys
- File Handling
- Automation Scripting

## Modules Used
- os: Directory traversal and file deletion.
- hashlib: MD5 checksum generation.
- sys: Command-line functionality.

## How It Works
1. Accepts a directory path for scanning.
2. Checks whether the specified directory exists.
3. Traverses files using os.walk().
4. Calculates the MD5 checksum of each file.
5. Groups files having identical checksums.
6. Identifies duplicate files.
7. Deletes redundant copies while retaining one copy.
8. Displays the total number of deleted files.

## Execution

Run the Python script:

    python DuplicateFileCleaner.py

## Important Note
This project permanently deletes duplicate files. Test it using a sample directory and keep a backup of important data before execution.

## Author
Sanskruti Sameer Saste

GitHub: https://github.com/sanskrutisaste5
