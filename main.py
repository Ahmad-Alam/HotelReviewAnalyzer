from preProcessing import extract_columns
from best_worst import load_data, convert_ratings, identify_most_reviews, calculate_average_ratings, identify_best_and_worst_hotels
import graphCSVforR
from labelwordCloud import analyze_sentiment, generate_word_cloud
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm


print("Reading the reviews and offerings csv files from the dataset folder!")
# Load data from CSV files
reviews_df = pd.read_csv('dataset/reviews.csv')
offerings_df = pd.read_csv('dataset/offerings.csv')

# Merge the two DataFrames on the common key (offering_id and id)
merged_df = pd.merge(reviews_df, offerings_df, left_on='offering_id', right_on='id')

# Select only the relevant columns
result_df = merged_df[['name', 'ratings', 'text']]

# Save the result to a new CSV file
result_df.to_csv('merged_reviews.csv', index=False)
print("merged_reviews.csv file created by merging both csv files.")

# Specify the input and output file paths
input_csv_file = 'merged_reviews.csv'
output_csv_file = 'preProcessed.csv'

print("A function is being called to extract columns, process text, and save to a new CSV file!")
# Call the function to extract columns, process text, and save to a new CSV file
extract_columns(input_csv_file, output_csv_file)

print("The preProcessed.csv file has been created successfully!")

# Sentiment Analysis, Labeling and Word Clouds ---------------------------------------

# Load data from CSV file
df = pd.read_csv('preProcessed.csv')

# Choose sentiment analysis method
sia = SentimentIntensityAnalyzer()

# Apply sentiment analysis to each row using tqdm
tqdm.pandas(desc="Analyzing Sentiment")
sentiment_columns = df.progress_apply(analyze_sentiment, axis=1)

# Concatenate the new columns to the original DataFrame
df = pd.concat([df, sentiment_columns], axis=1)

# Filter positive, negative, and neutral reviews
positive_reviews = df[df['sentiment_label'] == 'positive']
negative_reviews = df[df['sentiment_label'] == 'negative']
neutral_reviews = df[df['sentiment_label'] == 'neutral']

print("The sentiment analysis has been completed successfully!")
print("Please enter yes to generate the word clouds for positive, negative, and neutral reviews!")
print(">>> ", end='')
input_word_cloud = input()
if input_word_cloud.lower() == 'yes':
    print("Generating Word Clouds for positive, negative, and neutral reviews!")
    # Generate Word Clouds for positive, negative, and neutral reviews
    generate_word_cloud(' '.join(positive_reviews['text']), 'Positive Reviews Word Cloud')
    generate_word_cloud(' '.join(negative_reviews['text']), 'Negative Reviews Word Cloud')
    generate_word_cloud(' '.join(neutral_reviews['text']), 'Neutral Reviews Word Cloud')
else:
    print("Word Clouds will not be generated!")

print("The labeledData.csv file has been created successfully!")
df.to_csv('labeledData.csv', index=False)

# BEST AND WORST HOTELS ------------------------------------------------------

csv_file = 'labeledData.csv'
criteria = ['service', 'cleanliness', 'overall', 'value', 'location', 'sleep_quality', 'rooms']

# Load data
df = load_data(csv_file)

# Convert ratings
df = convert_ratings(df)

# Identify hotels with most positive and negative reviews
most_positive, most_negative = identify_most_reviews(df)
print(f"The hotel with the most positive reviews is: {most_positive[0]} with {most_positive[1]} reviews")
print(f"The hotel with the most negative reviews is: {most_negative[0]} with {most_negative[1]} reviews")

# Calculate average ratings for each criterion
average_ratings = calculate_average_ratings(df, criteria)

# Identify best and worst hotels for each criterion
results = identify_best_and_worst_hotels(average_ratings, criteria)
for criterion, hotels in results.items():
    print(f"The best hotel for {criterion} is: {hotels['best_hotel'][0]} with an average rating of {hotels['best_hotel'][1]:.2f}")
    print(f"The worst hotel for {criterion} is: {hotels['worst_hotel'][0]} with an average rating of {hotels['worst_hotel'][1]:.2f}")
    print()

