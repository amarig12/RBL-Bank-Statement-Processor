import os
import json

def pdf():
    # Get current script's directory
    current_folder = os.path.dirname(__file__)  
    config_file_path = os.path.join(current_folder, "path.json")

    # Open config file to read
    with open(config_file_path, "r") as file:
        config = json.load(file)

        statement_folder = config["statement_folder"]

        excel_folder = config["excel_folder"]

    folder_path = os.path.join(current_folder, statement_folder)

    # Initialize lists to store results
    pdf_paths = []
    excel_outputs = []

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)  # Get full path

        # Check if it is a PDF file
        if filename.lower().endswith(".pdf"):
            print(f"Processing file: {file_path}")

            pdf_path = os.path.join(current_folder, statement_folder, filename)
            excel_filename = os.path.splitext(filename)[0] + ".xlsx"
            excel_output = os.path.join(current_folder, excel_folder, excel_filename)

            # Append to lists
            pdf_paths.append(pdf_path)
            excel_outputs.append(excel_output)
    
    return pdf_paths, excel_outputs

