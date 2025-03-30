import os

def rename_files_in_directory(directory):
    """
    Renames all .png files in the given directory from {Name} - Advanced.png to {Name} - Elementary.png.
    """
    # Check if the directory exists
    if not os.path.exists(directory):
        print(f"Error: The directory '{directory}' does not exist.")
        return

    # Get the list of all files in the directory
    files_in_directory = os.listdir(directory)

    # Check if there are any files at all
    if not files_in_directory:
        print("No files found in the directory.")
        return

    print(f"Files found in the directory: {files_in_directory}")

    # Loop through each file in the specified directory
    renamed_count = 0
    for filename in files_in_directory:
        if filename.endswith(" - Advanced.png"):  # Adjusted to match the "Advanced.png" ending
            # Get the name without " - Advanced.png"
            new_name = filename.replace(" - Advanced.png", " - Elementary.png")
            
            # Get the full paths for the old and new file names
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            
            # Rename the file
            try:
                os.rename(old_file, new_file)
                renamed_count += 1
                print(f"Renamed: {filename} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

    if renamed_count == 0:
        print("No files were renamed. Please check the file names or pattern.")
    else:
        print(f"{renamed_count} file(s) renamed successfully.")

# Specify the directory where your files are located
directory = './elem-r1'  # Replace with your directory path if needed (e.g., '/path/to/your/files')

# Call the function to rename files
rename_files_in_directory(directory)
