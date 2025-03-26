import pandas as pd
from sentiment_model import analyze_sentiment

# Sample song dataset
data = {
    "Song": ["Happy Now", "Someone Like You", "Rockstar"],
    "Artist": ["Kygo", "Adele", "Post Malone"],
    "Genre": ["EDM", "Pop", "Hip-Hop"],
    "Sentiment": ["positive", "negative", "neutral"]
}

df = pd.DataFrame(data)

# Function to recommend songs based on sentiment
def recommend_song(user_sentiment):
    recommended_songs = df[df["Sentiment"] == user_sentiment]
    if recommended_songs.empty:
        return [{"Song": "No Song Found", "Artist": "N/A"}]
    return recommended_songs.sample(1)[["Song", "Artist"]].to_dict(orient="records")

# Example usage
if __name__ == "__main__":
    text = input("Enter a sentence: ")
    sentiment = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")
    print("Recommendation:", recommend_song(sentiment))
