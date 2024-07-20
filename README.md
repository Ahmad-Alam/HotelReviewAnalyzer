# Hotel Review Analyzer
This project uses natural language processing (NLP) and sentiment analysis techniques to analyze hotel reviews. It aims to extract valuable insights from the reviews, identify the best and worst performing hotels based on different criteria, and visualize key trends using word clouds.

## Key Features
- **Data Merging:** Combines review data and hotel offerings for comprehensive analysis.
- **Text Preprocessing:** Cleans and standardizes review text for NLP tasks.
- **Sentiment Analysis**:
	- Classifies reviews as positive, negative, or neutral.
	- Generates word clouds to visually represent common themes in each sentiment category.
- **Rating Analysis:**
	- Calculates average ratings for various criteria (service, cleanliness, overall, etc.).
	- Identifies the best and worst hotels based on these ratings.

## Requirements
- Python 3.x
- Pandas
- NLTK
- scikit-learn
- WordCloud
- Matplotlib (optional, for word cloud visualization)

## Usage
### Prepare Data
Ensure you have CSV files named reviews.csv and offerings.csv in the dataset directory. The dataset is available on Kaggle at the following [link](https://www.kaggle.com/datasets/joebeachcapital/hotel-reviews/data).
### Install Dependencies
```sh
    pip install -r requirements.txt
```
### Run the Script
```sh
    python main.py
```
- The script will process the data, perform sentiment analysis, and calculate ratings.
- You will be prompted whether you want to generate word clouds (type 'yes' to confirm).
- The script will generate output files (merged_reviews.csv, preProcessed.csv, and optionally labeledData.csv) and print results to the console.

## Disclaimer
This project is intended for educational and exploratory purposes. The analysis results are based on historical data and may not perfectly predict future trends. Use the information responsibly.


