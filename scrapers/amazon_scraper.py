import requests
import json
import re
from pprint import pprint
from app.core.config import settings

def AmazonScraper():

    def extract_product_ids(data):
        product_ids = []
        if isinstance(data, dict):
            for key, value in data.items():
                product_ids.extend(extract_product_ids(value))
        elif isinstance(data, list):
            for item in data:
                product_ids.extend(extract_product_ids(item))
        elif isinstance(data, str):
            matches = re.findall(r'/dp/(\w+?)/', data)
            product_ids.extend(matches)
        return product_ids

    def get_product_info(product_id):
        payload = {
            'source': 'amazon_product',
            'domain': 'com',
            'query': product_id,
            'parse': True,
            'context': [
                {'key': 'autoselect_variant', 'value': True}
            ],
        }

        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=(settings.OXYLAB_USERNAME, settings.OXYLAB_PASSWORD),  
            json=payload,
        )
        return response.json()

    def get_product_reviews(product_id):
        payload = {
            'source': 'amazon_reviews',
            'domain': 'com',
            'query': product_id,
            'parse': True,
            'start_page': 1,
            'pages': 5
        }

        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=(settings.OXYLAB_USERNAME, settings.OXYLAB_PASSWORD),
            json=payload,
        )
        return response.json()

    search_payload = {
        'source': 'amazon_search',
        'query': 'watch',
        'domain': 'com'
    }

    search_response = requests.request(
        'POST',
        'https://realtime.oxylabs.io/v1/queries',
        auth=(settings.OXYLAB_USERNAME, settings.OXYLAB_PASSWORD),
        json=search_payload,
    )

    search_response_json = search_response.json()
    product_ids = extract_product_ids(search_response_json)

    for product_id in product_ids:
        product_info = get_product_info(product_id)
        with open(f'./data/product/{product_id}_details.json', 'w') as file:
            json.dump(product_info, file, indent=4)

    for product_id in product_ids:
        product_reviews = get_product_reviews(product_id)
        with open(f'./data/reviews/{product_id}_reviews.json', 'w') as file:
            json.dump(product_reviews, file, indent=4)
