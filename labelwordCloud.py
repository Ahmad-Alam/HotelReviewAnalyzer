import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm import tqdm
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load data from CSV file
df = pd.read_csv('preProcessed.csv')

# Choose sentiment analysis method
sia = SentimentIntensityAnalyzer()  # Option 1: SentimentIntensityAnalyzer

# Function to categorize sentiment
def categorize_sentiment(score):
    if score >= 0.05:
        return 'positive'
    elif score <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Function to analyze sentiment for each row
def analyze_sentiment(row, method='sia'):
    text = row['text']
    if pd.isna(text):
        return pd.Series([None, None], index=['sentiment_score', 'sentiment_label'])
    if method == 'sia':
        scores = sia.polarity_scores(text)
    else:
        raise ValueError("Invalid sentiment analysis method")
    sentiment_label = categorize_sentiment(scores['compound'])
    return pd.Series([scores['compound'], sentiment_label], index=['sentiment_score', 'sentiment_label'])

# Function to generate and display Word Cloud
def generate_word_cloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

# Apply sentiment analysis to each row using tqdm
tqdm.pandas(desc="Analyzing Sentiment")
sentiment_columns = df.progress_apply(analyze_sentiment, axis=1)

# Concatenate the new columns to the original DataFrame
df = pd.concat([df, sentiment_columns], axis=1)

# Filter positive, negative, and neutral reviews
positive_reviews = df[df['sentiment_label'] == 'positive']
negative_reviews = df[df['sentiment_label'] == 'negative']
neutral_reviews = df[df['sentiment_label'] == 'neutral']

# Generate Word Clouds for positive, negative, and neutral reviews
generate_word_cloud(' '.join(positive_reviews['text']), 'Positive Reviews Word Cloud')
generate_word_cloud(' '.join(negative_reviews['text']), 'Negative Reviews Word Cloud')
generate_word_cloud(' '.join(neutral_reviews['text']), 'Neutral Reviews Word Cloud')

# Print and save results
print(df)
df.to_csv('namedData.csv', index=False)
