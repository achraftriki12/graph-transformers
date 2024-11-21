import os
import csv
import argparse

def extract_file_paths(folder_path, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['path_to_patches'])

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)  # Print file paths to the console
                csv_writer.writerow([file_path])  # Write file path to the CSV file

def main():
    parser = argparse.ArgumentParser(description="Extract file paths from a folder and write them to a CSV file.")
    parser.add_argument("folder_path", help="The path of the folder to scan for files.")
    parser.add_argument("csv_file", help="The CSV file path where the paths will be written.")
    
    args = parser.parse_args()
    
    extract_file_paths(args.folder_path, args.csv_file)

if __name__ == "__main__":
    main()
