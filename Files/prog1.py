# program to create and read content from the file
fname = input("Enter your file name: ")
try:
    f = open(fname, "w")
    content = ""
    while content != "quit":
        f.write(content + "\n")  # Adding a newline for readability
        content = input("Enter content (type 'quit' to stop): ")
    f.close()  # Closing the file after writing

    # Re-opening the file in read mode to display the contents
    f = open(fname, "r")
    print("File contents:")
    print(f.read())
    
except: 
    print("an error occured")
finally:
    # Ensuring the file is closedr
    f.close()

