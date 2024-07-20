import pandas as pd
import ast

def load_data(csv_file):
    """Load data from CSV file."""
    return pd.read_csv(csv_file)

def convert_ratings(df):
    """Convert string representation of dictionary to actual dictionary."""
    df['ratings'] = df['ratings'].apply(ast.literal_eval)
    criteria_columns = df['ratings'].apply(pd.Series)
    return pd.concat([df, criteria_columns], axis=1)

def count_reviews(df):
    """Count the number of positive and negative reviews for each hotel."""
    positive_reviews_count = df[df['sentiment_label'] == 'positive'].groupby('name').size()
    negative_reviews_count = df[df['sentiment_label'] == 'negative'].groupby('name').size()
    reviews_counts = pd.concat([positive_reviews_count, negative_reviews_count], axis=1, keys=['Positive_Reviews', 'Negative_Reviews'])
    reviews_counts.fillna(0, inplace=True)
    reviews_counts.reset_index(inplace=True)
    return reviews_counts

def save_reviews_counts(reviews_counts, output_file):
    """Save the reviews counts DataFrame to a CSV file."""
    reviews_counts.to_csv(output_file, index=False)
    print(f"CSV file with positive and negative reviews counts has been created successfully at {output_file}.")

def calculate_average_ratings(df, criteria):
    """Calculate average ratings for each criterion."""
    return df.groupby('name')[criteria].mean()

def save_average_ratings(criteria, average_ratings_criteria, output_folder):
    """Save separate CSV files for average ratings of each criterion."""
    for criterion in criteria:
        output_filename = f'{criterion}_ratings.csv'
        output_df = pd.DataFrame({
            'Hotel': average_ratings_criteria.index,
            'Average_Rating': average_ratings_criteria[criterion]
        })
        output_df.to_csv(output_folder + output_filename, index=False)
        print(f'Successfully saved {criterion} ratings to {output_folder + output_filename}')

if __name__ == "__main__":
    csv_file = 'labeledData.csv'
    output_folder = 'graphs/'
    criteria = ['service', 'cleanliness', 'overall', 'value', 'location', 'sleep_quality', 'rooms']
    
    # Load data
    df = load_data(csv_file)
    
    # Convert ratings
    df = convert_ratings(df)
    
    # Count reviews
    reviews_counts = count_reviews(df)
    
    # Save reviews counts
    save_reviews_counts(reviews_counts, output_folder + 'reviews_counts.csv')
    
    # Calculate average ratings for each criterion
    average_ratings_criteria = calculate_average_ratings(df, criteria)
    
    # Save separate CSV files for average ratings of each criterion
    save_average_ratings(criteria, average_ratings_criteria, output_folder)
