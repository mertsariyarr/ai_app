import os

def get_files_info(working_directory, directory="."):
    abs_path = os.path.abspath(working_directory)
    target_path = os.path.abspath(os.path.join(working_directory, directory))

    if not target_path.startswith(abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        myList = os.listdir(target_path)
        myItems = []

        for item in myList:
            my_path = os.path.join(target_path, item)
            a = f"- {item}: file_size={os.path.getsize(my_path)} bytes, is_dir={os.path.isdir(my_path)}"
            myItems.append(a)
        return "\n".join(myItems)
    except Exception as e:
        return f"Error: listing files: {e}"
        

        