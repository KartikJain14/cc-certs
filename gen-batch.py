from gen import generate_certificate

def process_names_from_file(file_path):
    """
    Reads names from a text file line by line and applies the `format_name` function to each.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                formatted_name = generate_certificate(line.strip(), "Advcanced", 2)  # Strip to remove any trailing newlines
                print(formatted_name)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function with the path to your .txt file
file_path = 'sample.txt'  # Replace with the actual path to your text file
process_names_from_file(file_path)