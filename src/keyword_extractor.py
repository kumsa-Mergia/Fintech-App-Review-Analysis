from sklearn.feature_extraction.text import TfidfVectorizer

class KeywordExtractor:
    def __init__(self, max_features=1000):
        self.vectorizer = TfidfVectorizer(max_features=max_features, ngram_range=(1,2))

    def extract_keywords(self, documents):
        tfidf_matrix = self.vectorizer.fit_transform(documents)
        return self.vectorizer.get_feature_names_out()
