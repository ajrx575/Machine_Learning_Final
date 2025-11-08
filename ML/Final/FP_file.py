import pandas as pd
import numpy as np

input_file_path = 'dataJAPPL-2021-00246.csv'
output_file_path = 'cleaned_coffee.csv'

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        cleaned_line = line.replace('"', '')
        outfile.write(cleaned_line)

coffeedf = pd.read_csv('cleaned_coffee.csv', delimiter=';')