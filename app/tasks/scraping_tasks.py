from app.core.celery_app import celery
from app.scrapers.amazon_scraper import AmazonScraper

@celery.task
def scrape_product_data(product_id: int):
    scraper = AmazonScraper()
    return scraper.scrape_product_data(product_id)