#!/usr/bin/env python
# coding: utf-8

# In[10]:


import os
import csv

def extract_file_paths(folder_path, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['path_to_patches'])

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                print(file)
                file_path = os.path.join(root, file)
                print(file_path)
                csv_writer.writerow([file_path])  # Write file_path instead of path_to_patches

# Example usage:
folder_path = '20.0'  # Specify the folder path here
csv_file = 'all_patches.csv'  # Specify the output CSV file name

extract_file_paths(folder_path, csv_file)


# In[8]:


print(root)

