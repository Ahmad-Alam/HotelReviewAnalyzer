import csv
import random

def filter_csv(input_file, output_file, num_entries):
    # Dictionary to store rows based on sentiment_label
    data = {'positive': [], 'negative': [], 'neutral': []}

    # Read the original CSV file and categorize rows based on sentiment_label
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            sentiment_label = row.get('sentiment_label', '').lower()  # Get lowercase version of sentiment_label
            if sentiment_label in data:
                data[sentiment_label].append(row)

    # Select the required number of rows for each sentiment_label
    selected_data = []
    for label, rows in data.items():
        if len(rows) >= num_entries // 3:
            selected_data.extend(random.sample(rows, num_entries // 3))
        else:
            selected_data.extend(rows)

    # Shuffle the selected data
    random.shuffle(selected_data)

    # Remove 'sentiment_label' and 'sentiment_score' fields
    for row in selected_data:
        del row['sentiment_label']
        del row['sentiment_score']

    # Write the selected data to the output CSV file
    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        fieldnames = ['name', 'ratings', 'text']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(selected_data)

# Example usage
input_file = 'labeledData.csv'  # Replace 'original.csv' with your original CSV file path
output_file = 'preProcessed.csv'  # Replace 'filtered.csv' with the output CSV file path
num_entries = 25  # Number of entries in the output CSV file

filter_csv(input_file, output_file, num_entries)
