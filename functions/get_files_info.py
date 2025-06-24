import os
from constants import MAX_CHARS

def is_within_subdirectory(path, parent):
    path = os.path.abspath(path)
    parent = os.path.abspath(parent)
    return os.path.commonpath([path, parent]) == parent


def get_files_info(working_directory, directory=None):
    directory = os.path.join(working_directory, directory)

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'
    if not is_within_subdirectory(directory, working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    files_info = []
    for item_name in os.listdir(directory):
        item_path = os.path.join(directory, item_name)
        try:
            file_size = os.stat(item_path).st_size
            is_dir = os.path.isdir(item_path)
            files_info.append(f"- {item_name}: file_size={file_size} bytes, is_dir={is_dir}")
        except FileNotFoundError:
            return f"- {item_name}: Error retrieving info (possibly a broken symlink)"
    return "\n".join(files_info)


"""
Read file and return its contents as a string
"""
def get_file_content(working_directory, file_path):
    file_path = os.path.join(working_directory, file_path)

    if not is_within_subdirectory(file_path, working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    file_content_string = ""
    try:
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= 10000:
                file_content_string += f" File {file_path} truncated at 10000 characters"
    except Exception as e:
        return f"Error opening file: {file_path} {e}"

    return file_content_string


