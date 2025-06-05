import os
import pandas as pd
from google_play_scraper import reviews, Sort

class PlayStoreReviewScraper:
    def __init__(self, apps, count=450, languages=['en', 'am']):
        """
        :param apps: dict in format {package_name: bank_name}
        :param count: max reviews per app
        :param languages: languages to fetch reviews in
        """
        self.apps = apps
        self.count = count
        self.languages = languages
        self.all_reviews = []

    def fetch_all(self):
        for package, bank in self.apps.items():
            print(f"\n Fetching reviews for: {bank}")
            collected_reviews = []
            seen_ids = set()
            total_collected = 0

            for lang in self.languages:
                next_token = None

                while total_collected < self.count:
                    remaining = self.count - total_collected
                    try:
                        batch, next_token = reviews(
                            package,
                            lang=lang,
                            country='et',
                            count=min(200, remaining),
                            sort=Sort.NEWEST,
                            continuation_token=next_token
                        )

                        if not batch:
                            break

                        # Filter duplicates
                        new_reviews = [r for r in batch if r['reviewId'] not in seen_ids]

                        for r in new_reviews:
                            seen_ids.add(r['reviewId'])
                            collected_reviews.append(r)
                            total_collected += 1

                            if total_collected >= self.count:
                                break

                        if not next_token or total_collected >= self.count:
                            break

                    except Exception as e:
                        print(f" Error in {lang}: {e}")
                        break

                if total_collected >= self.count:
                    break  # Stop if we've reached enough for this bank

            print(f" Final count for {bank}: {len(collected_reviews)} reviews")

            for r in collected_reviews:
                self.all_reviews.append({
                    "review": r.get("content"),
                    "rating": r.get("score"),
                    "date": r.get("at").strftime('%Y-%m-%d') if r.get("at") else None,
                    "bank": bank,
                    "source": "Google Play Store"
                })

    def save_raw_reviews(self, path="data/bank_reviews.csv"):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        pd.DataFrame(self.all_reviews).to_csv(path, index=False)
        print(f"\n Saved {len(self.all_reviews)} reviews to {path}")