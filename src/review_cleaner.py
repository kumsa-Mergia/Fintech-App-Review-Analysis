import pandas as pd
import os

class ReviewCleaner:
    def __init__(self, input_path):
        self.input_path = input_path
        self.df = None

    def load_data(self):
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"{self.input_path} not found.")
        self.df = pd.read_csv(self.input_path)

    def clean(self):
        self.df.drop_duplicates(subset=["review"], inplace=True)
        self.df.dropna(subset=["review", "rating", "date"], inplace=True)
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df.dropna(subset=["date"], inplace=True)
        self.df['date'] = self.df['date'].dt.strftime('%Y-%m-%d')
        self.df = self.df[["review", "rating", "date", "bank", "source"]]

    def save_clean(self, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.df.to_csv(output_path, index=False)
        print(f" Cleaned data saved to {output_path}")
