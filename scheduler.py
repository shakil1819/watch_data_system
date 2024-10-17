import schedule
import time
from scrapers.amazon_scraper import AmazonScraper

def run_scraper():
    scraper = AmazonScraper()
    scraper.scrape_and_save_data("watches", max_pages=5)

def schedule_scraper():
    schedule.every(12).hours.do(run_scraper)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_scraper()
