import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.scraper import PlayStoreReviewScraper

import unittest

class TestPlayStoreReviewScraper(unittest.TestCase):
    def test_init(self):
        apps = {'test.package': 'Test Bank'}
        scraper = PlayStoreReviewScraper(apps)
        self.assertEqual(scraper.apps, apps)

if __name__ == '__main__':
    unittest.main()