import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    abs_path = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                return file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error: Cannot convert txt {file_path} as {e}"

    
schema_get_files_content = types.FunctionDeclaration( ## schema for the get file content
    name="get_file_content",
    description="Read and returns the specific file's content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read and return.",
            ),
        },
        required=["file_path"]
    ),
)