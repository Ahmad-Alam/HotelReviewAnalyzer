import csv

def truncate_csv(input_file, output_file, rows_to_keep):
    with open(input_file, 'r', encoding='utf-8') as infile:  # Specify encoding here
        reader = csv.reader(infile)
        data = list(reader)[:rows_to_keep]

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:  # Specify encoding here
        writer = csv.writer(outfile)
        writer.writerows(data)

# Example usage
input_file = 'reviews.csv'  # Replace 'input.csv' with your input CSV file path
output_file = 'reviews.csv'  # Replace 'output.csv' with your output CSV file path
rows_to_keep = 25  # Number of rows to keep
truncate_csv(input_file, output_file, rows_to_keep)
