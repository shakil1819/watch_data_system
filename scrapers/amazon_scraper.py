import requests
from datetime import datetime
from app.core.db import SessionLocal, Watch, Review

class AmazonScraper:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.scrapingdog.com/amazon"

    def search_watches(self, query, page=1):
        params = {
            "api_key": self.api_key,
            "domain": "com",
            "type": "search",
            "search": query,
            "page": page
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def get_product_details(self, asin):
        params = {
            "api_key": self.api_key,
            "domain": "com",
            "type": "product",
            "asin": asin
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def get_product_reviews(self, asin, page=1):
        params = {
            "api_key": self.api_key,
            "domain": "com",
            "type": "reviews",
            "asin": asin,
            "page": page
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

    def scrape_and_save_data(self, search_query, max_pages=5):
        db = SessionLocal()
        try:
            for page in range(1, max_pages + 1):
                search_results = self.search_watches(search_query, page)
                for product in search_results.get("products", []):
                    asin = product.get("asin")
                    if not asin:
                        continue

                    details = self.get_product_details(asin)
                    
                    watch = Watch(
                        brand=details.get("brand"),
                        model=details.get("title"),
                        price=float(details.get("price", "0").replace("$", "").replace(",", "")),
                        material=details.get("product_information", {}).get("Material"),
                        water_resistance=details.get("product_information", {}).get("Water Resistance Depth"),
                        image_url=details.get("images", [{}])[0].get("src"),
                        category=details.get("product_information", {}).get("Department"),
                        asin=asin
                    )
                    db.add(watch)
                    db.commit()

                    reviews = self.get_product_reviews(asin)
                    for review_data in reviews.get("reviews", []):
                        review = Review(
                            watch_id=watch.id,
                            rating=float(review_data.get("rating", 0)),
                            review_text=review_data.get("review"),
                            reviewer_name=review_data.get("name"),
                            review_date=datetime.strptime(review_data.get("date"), "%B %d, %Y")
                        )
                        db.add(review)
                    db.commit()
        finally:
            db.close()
