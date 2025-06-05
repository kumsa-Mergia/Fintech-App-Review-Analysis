from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def analyze(self, text):
        score = self.sia.polarity_scores(text)['compound']
        label = 'positive' if score > 0.05 else 'negative' if score < -0.05 else 'neutral'
        return label, score
