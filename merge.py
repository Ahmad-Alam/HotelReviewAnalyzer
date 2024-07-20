import pandas as pd

# Load data from CSV files
reviews_df = pd.read_csv('dataset/reviews.csv')
offerings_df = pd.read_csv('dataset/offerings.csv')

# Merge the two DataFrames on the common key (offering_id and id)
merged_df = pd.merge(reviews_df, offerings_df, left_on='offering_id', right_on='id')

# Select only the relevant columns
result_df = merged_df[['name', 'ratings', 'text']]

# Save the result to a new CSV file
result_df.to_csv('merged_reviews.csv', index=False)
