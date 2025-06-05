from src.pipeline import AnalysisPipeline

if __name__ == "__main__":
    pipeline = AnalysisPipeline("bank_reviews_clean.csv", "task2_review_analysis.csv")
    pipeline.run()
