import os
from datetime import datetime
from google_play_scraper import reviews, Sort
import pandas as pd

class PlayStoreReviewScraper:
    def __init__(self, apps):
        self.apps = apps
        self.all_reviews = []

    def fetch_reviews(self, count=450, languages=['en', 'am']):
        """
        Fetch up to `count` most recent reviews for each app, combining all languages.
        """
        for package, bank_name in self.apps.items():
            print(f"\nFetching reviews for {bank_name}...")
            all_results = []
            
            # Store the initial length of self.all_reviews before processing this bank
            initial_all_reviews_len = len(self.all_reviews)

            for lang_code in languages:
                lang_results = []
                next_token = None
                target = count - len(all_results)  # Remaining reviews needed

                # If we've already reached the target count for this app, no need to fetch more
                if target <= 0:
                    break 

                while len(lang_results) < target:
                    try:
                        batch, next_token = reviews(
                            package,
                            lang=lang_code,
                            country='et',
                            count=min(200, target - len(lang_results)), # Fetch in batches, respecting the remaining needed
                            sort=Sort.NEWEST,
                            continuation_token=next_token
                        )
                    except Exception as e:
                        print(f"    Error fetching {lang_code} reviews for {bank_name}: {e}")
                        break # Stop if an error occurs

                    if not batch:
                        break # No more reviews for this language

                    lang_results.extend(batch)

                    if not next_token:
                        break # No more pages
                
                # Add language-specific results to all_results, stopping if count is reached
                for review in lang_results:
                    if len(all_results) < count: # Only add if we haven't reached the overall count for this app
                        all_results.append((review, lang_code))
                    else:
                        break # Reached the count limit for this app

                # If we've reached the overall count for this app, break from language loop
                if len(all_results) >= count:
                    break

            # Process and store the collected reviews for this app into self.all_reviews
            # This loop now just formats the reviews collected in all_results
            for review, lang_code in all_results: # `all_results` is already capped at `count`
                self.all_reviews.append({
                    'user_name': review.get('userName'),
                    'review': review.get('content'),
                    'rating': review.get('score'),
                    'date': review.get('at').strftime('%Y-%m-%d') if review.get('at') else 'unknown',
                    'bank': bank_name,
                    'language': lang_code,
                    'source': 'Google Play Store'
                })
            
            # Calculate and print the number of reviews added for this specific bank
            reviews_added_for_bank = len(self.all_reviews) - initial_all_reviews_len
            print(f"  Added {reviews_added_for_bank} reviews for {bank_name} to the main list.")

    def save_to_csv(self, filename="data/bank_reviews.csv"):
        """
        Save raw scraped reviews to a CSV file.
        """
        df = pd.DataFrame(self.all_reviews)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        df.to_csv(filename, index=False)
        print(f"\nSaved raw reviews to {filename}")
        print(f"Total raw reviews in CSV: {len(df)}")

if __name__ == "__main__":
    apps = {
        'com.combanketh.mobilebanking': 'Commercial Bank of Ethiopia',
        'com.boa.boaMobileBanking': 'Bank of Abyssinia',
        'com.dashen.dashensuperapp': 'Dashen Bank'
    }

    scraper = PlayStoreReviewScraper(apps)
    scraper.fetch_reviews(count=450, languages=['en', 'am'])  # Fetch up to 450 reviews per bank
    scraper.save_to_csv(filename="data/bank_reviews.csv")  # Save raw data