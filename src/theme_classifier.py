class ThemeClassifier:
    def __init__(self):
        self.theme_keywords = {
            "Account Access Issues": ["login", "password", "reset", "authentication", "access"],
            "Transaction Performance": ["transfer", "processing", "delay", "slow", "transaction"],
            "UI/UX": ["interface", "design", "navigation", "app", "layout"],
            "Customer Support": ["support", "help", "agent", "customer", "response"],
            "Feature Requests": ["feature", "missing", "option", "update", "add"]
        }

    def classify(self, text):
        matched = set()
        for theme, keywords in self.theme_keywords.items():
            if any(kw in text for kw in keywords):
                matched.add(theme)
        return list(matched) if matched else ["Other"]
