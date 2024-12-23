import json
import os

def get_src_folder_path():
    return os.path.abspath(os.getcwd()) + "/"


def get_output_folder_path():
    return get_src_folder_path().replace('src', 'output')


def write_dict_to_txt(data, filename):
    """
    Writes the dictionary data to a .txt file.
    Each key-value pair will be written on a separate line.
    
    Args:
    - data (dict): The dictionary to write to the file.
    - filename (str): The name of the output file.
    """
    try:
        with open(get_output_folder_path() + filename, 'w') as f:
            for key, value in data.items():
                f.write(f"{key} : {value}\n")  # Writing key-value pairs to the file
        print(f"Results have been saved to {filename} (txt).")
    except Exception as e:
        print(f"Error while writing the file: {e}")


def write_dict_to_json(data, filename):
    """
    Writes the dictionary data to a .json file in a readable format (with indentation).
    
    Args:
    - data (dict): The dictionary to write to the file.
    - filename (str): The name of the output file.
    """
    try:
        with open(get_output_folder_path() + filename, 'w') as f:
            json.dump(data, f, indent=4)  # Writing the dictionary as a JSON file
        print(f"Results have been saved to {filename} (json).")
    except Exception as e:
        print(f"Error while writing the file: {e}")



