import pandas as pd
from src.data_loader import DataLoader
from src.preprocessor import TextPreprocessor
from src.sentiment_analyzer import SentimentAnalyzer
from src.keyword_extractor import KeywordExtractor
from src.theme_classifier import ThemeClassifier

class AnalysisPipeline:
    def __init__(self, input_path, output_path):
        self.loader = DataLoader(input_path)
        self.preprocessor = TextPreprocessor()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.keyword_extractor = KeywordExtractor()
        self.theme_classifier = ThemeClassifier()
        self.output_path = output_path

    def run(self):
        df = self.loader.load()
        df["cleaned_review"] = df["review"].astype(str).apply(self.preprocessor.preprocess)
        df[["sentiment_label", "sentiment_score"]] = df["review"].apply(lambda text: pd.Series(self.sentiment_analyzer.analyze(text)))
        df["themes"] = df["cleaned_review"].apply(self.theme_classifier.classify)

        top_keywords = self.keyword_extractor.extract_keywords(df["cleaned_review"])
        print("Sample Keywords:", top_keywords[:10])

        df.to_csv(self.output_path, index=False)
        print(f"[✓] Analysis saved to {self.output_path}")
