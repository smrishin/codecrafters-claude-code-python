import sys
import subprocess
from app.tools.utils import tool

@tool
def read_file(file_path: str) -> str:
    """ Read and return the contents of a file
    :param file_path: The path to the file to read
    """
    try:
        with open(file_path,'r') as file:
            result = file.read()
        return result
    except Exception as e:
        error_msg = f"Error reading file: {e}"
        print(error_msg, file=sys.stderr)
        return error_msg

@tool
def write_file(file_path: str, content: str) -> str:
    """ Write content to a file
    :param file_path: The path to the file to write to
    :param content: The content to write to the file
    """
    try:
        with open(file_path, "w") as file:
            file.write(content)            
        return f"Content written to {file_path}"
    except Exception as e:
        error_msg = f"Error writing to file: {e}"
        print(error_msg, file=sys.stderr)
        return error_msg

@tool
def bash(command: str) -> str:
    """Execute a shell command
    :param command: The command to execute
    """
    output = subprocess.run(command.split(), capture_output=True, text=True)
    return output.stdout or output.stderr
