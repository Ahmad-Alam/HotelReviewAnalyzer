import pandas as pd
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    # Lowercasing
    text = text.lower()

    # Removing special characters
    text = ''.join(char for char in text if char.isalnum() or char.isspace())

    return text

def tokenize_remove_stopwords_and_stem(text):
    # Tokenization
    tokens = word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Stemming using Porter stemmer
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return ' '.join(stemmed_tokens)

def extract_columns(input_file, output_file, chunk_size=100000):
    # Create an iterator for reading the CSV file in chunks
    reader = pd.read_csv(input_file, chunksize=chunk_size)

    # Initialize an empty list to store the processed chunks
    processed_chunks = []

    # Get the total number of rows in the input file
    total_rows = sum(1 for _ in pd.read_csv(input_file, chunksize=chunk_size))

    # Initialize the tqdm loading bar
    with tqdm(total=total_rows, unit='row') as pbar:
        # Iterate over chunks and extract the specified columns
        for chunk in reader:
            # Apply text processing to the 'text' column
            chunk['text'] = chunk['text'].apply(preprocess_text)
            chunk['text'] = chunk['text'].apply(tokenize_remove_stopwords_and_stem)
            
            processed_chunks.append(chunk)
            pbar.update(chunk.shape[0])  # Update the loading bar with the number of rows processed

    # Concatenate all processed chunks into a single DataFrame
    extracted_data = pd.concat(processed_chunks, ignore_index=True)

    # Save the processed data to a new CSV file
    extracted_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Specify the input and output file paths
    input_csv_file = 'merged_reviews.csv'
    output_csv_file = 'preProcessed.csv'

    # Call the function to extract columns, process text, and save to a new CSV file
    extract_columns(input_csv_file, output_csv_file)
