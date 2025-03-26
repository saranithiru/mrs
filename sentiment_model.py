import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER for sentiment analysis
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score["compound"] >= 0.05:
        return "positive"
    elif sentiment_score["compound"] <= -0.05:
        return "negative"
    else:
        return "neutral"

# Example usage
if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Sentiment:", analyze_sentiment(text))
