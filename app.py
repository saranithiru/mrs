from flask import Flask, render_template, request, redirect, url_for
import json
import os
from sentiment_model import analyze_sentiment

app = Flask(__name__)

# Load song dataset from JSON file
SONG_FILE = 'songs.json'

def load_songs():
    if os.path.exists(SONG_FILE):
        with open(SONG_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        return {
            "positive": [
                {"Song": "Vaathi Coming", "Artist": "Anirudh Ravichander", "Language": "Tamil"},
                {"Song": "Shape of You", "Artist": "Ed Sheeran", "Language": "English"}
            ],
            "negative": [
                {"Song": "Ennodu Nee Irundhaal", "Artist": "A. R. Rahman", "Language": "Tamil"},
                {"Song": "Someone Like You", "Artist": "Adele", "Language": "English"}
            ],
            "neutral": [
                {"Song": "Aaluma Doluma", "Artist": "Anirudh Ravichander", "Language": "Tamil"},
                {"Song": "Counting Stars", "Artist": "OneRepublic", "Language": "English"}
            ]
        }

songs = load_songs()

# Function to recommend songs based on sentiment
def recommend_song(user_sentiment):
    return songs.get(user_sentiment, [{"Song": "No Song Found", "Artist": "N/A", "Language": "N/A"}])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')


@app.route('/recommendation', methods=['GET', 'POST'])
def index():
    recommendation = []
    sentiment = None
    
    if request.method == 'POST':
        user_text = request.form['user_text']
        if user_text.strip():  # Ensure input is not empty
            sentiment = analyze_sentiment(user_text)
            recommendation = recommend_song(sentiment)

    return render_template('index.html', sentiment=sentiment, recommendation=recommendation)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
