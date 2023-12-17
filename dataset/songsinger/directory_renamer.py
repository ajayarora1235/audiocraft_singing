import json
import os
import unicodedata

def unicode_to_ascii(s):
    """
    Convert a Unicode string with escape sequences to its ASCII equivalent.
    """
    return unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')

def rename_files_in_directory(directory):
    """
    Rename files in the given directory whose names contain Unicode characters,
    converting them to ASCII equivalents.
    """
    for file_name in os.listdir(directory):
        ascii_file_name = unicode_to_ascii(file_name)
                
        # Check if the file name needs to be updated
        if file_name.lower().endswith('.mp3') and file_name != ascii_file_name:
            original_full_path = os.path.join(directory, file_name)
            ascii_full_path = os.path.join(directory, ascii_file_name)
            
            # Rename the file
            os.rename(original_full_path, ascii_full_path)
            print(f"Renamed '{file_name}' to '{ascii_file_name}'")

directory='.'
rename_files_in_directory(directory)
