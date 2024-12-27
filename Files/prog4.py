fname = input("Enter your file name: ")

try:
    # Open file in exclusive creation mode
    with open(fname, "x") as f:
        content = ""
        while content != "quit":
            f.write(content + "\n")  # Write content with newline
            content = input("Enter content (type 'quit' to stop): ")

    # Re-open the file in read mode to display contents
    with open(fname, "r") as f:
        print("File contents:")
        print(f.read())

except FileExistsError:
    print("File already exists! Please choose a different name.")
except Exception as e:
    print(f"An error occurred: {e}")

