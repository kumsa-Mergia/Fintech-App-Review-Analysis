# Fintech-App-Review-Analysis

Customer experience analytics for Ethiopian banking apps. This project scrapes Google Play reviews, performs sentiment and thematic NLP, and visualizes key user insights.

This project scrapes user reviews from three Ethiopian bank apps on the Google Play Store and preprocesses them for analysis.

## Banks Covered

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

## Preprocessing Steps

- Scraped 400+ reviews per bank using `google-play-scraper`
- Preprocessed:
  - Removed duplicates
  - Dropped rows with missing review/rating/date
  - Normalized dates to `YYYY-MM-DD`
- Saved clean data as `cleaned_reviews.csv

## Output

- with 1200+ reviews

## Environment Setup

Follow the steps below to set up the development environment on your local machine:

### 1. Clone the Repository

Start by cloning the repository:

```bash
git https://github.com/kumsa-Mergia/Fintech-App-Review-Analysis.git

cd Fintech-App-Review-Analysis.git
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment to isolate the project's dependencies:

```bash
python -m venv venv #python3 for Linux
```

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all the required Python packages as listed in the `requirements.txt` file.

After completing these steps, your development environment will be set up and ready to go.
