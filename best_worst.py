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

def identify_most_reviews(df):
    """Identify hotel with the most positive and negative reviews."""
    positive_reviews_count = df[df['sentiment_label'] == 'positive'].groupby('name')['sentiment_label'].count()
    most_positive_hotel = positive_reviews_count.idxmax()
    most_positive_reviews = positive_reviews_count.max()
    
    negative_reviews_count = df[df['sentiment_label'] == 'negative'].groupby('name')['sentiment_label'].count()
    most_negative_hotel = negative_reviews_count.idxmax()
    most_negative_reviews = negative_reviews_count.max()
    
    return (most_positive_hotel, most_positive_reviews), (most_negative_hotel, most_negative_reviews)

def calculate_average_ratings(df, criteria):
    """Calculate average ratings for each criterion."""
    return df.groupby('name')[criteria].mean()

def identify_best_and_worst_hotels(average_ratings, criteria):
    """Identify the best and worst hotel for each criterion."""
    best_hotels = average_ratings.idxmax()
    worst_hotels = average_ratings.idxmin()

    results = {}
    for criterion in criteria:
        best_hotel_name = best_hotels[criterion]
        best_hotel_rating = average_ratings.loc[best_hotel_name, criterion]

        worst_hotel_name = worst_hotels[criterion]
        worst_hotel_rating = average_ratings.loc[worst_hotel_name, criterion]

        results[criterion] = {
            'best_hotel': (best_hotel_name, best_hotel_rating),
            'worst_hotel': (worst_hotel_name, worst_hotel_rating)
        }
    
    return results

if __name__ == "__main__":
    csv_file = 'namedData.csv'
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
