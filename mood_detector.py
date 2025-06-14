import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# Map emojis to moods
EMOJI_MOOD_MAP = {
    "😊": "happy",
    "😢": "sad",
    "😎": "chill",
    "⚡": "energetic",
    "😡": "angry",
    # Add more if needed
}

def detect_mood_from_text(text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.4:
        return "happy"
    elif compound <= -0.4:
        return "sad"
    else:
        # Neutral or mixed feelings
        if "chill" in text.lower() or "relax" in text.lower():
            return "chill"
        elif "energy" in text.lower() or "excited" in text.lower():
            return "energetic"
        else:
            return "chill"

def detect_mood(input_str):
    input_str = input_str.strip()
    if input_str in EMOJI_MOOD_MAP:
        return EMOJI_MOOD_MAP[input_str]
    else:
        return detect_mood_from_text(input_str)
