import os

try:
    # Specify the file name or path
    fname = input("Enter the file name to delete: ")

    # Attempt to delete the file
    os.remove(fname)
    print(f"The file '{fname}' has been deleted.")
    
except FileNotFoundError:
    print(f"The file '{fname}' does not exist.")
except PermissionError:
    print(f"Permission denied to delete the file '{fname}'.")
except Exception as e:
    print(f"An error occurred: {e}")
