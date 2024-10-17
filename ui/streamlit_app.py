import streamlit as st
import requests
from app.core.config import settings

API_URL = settings.API_URL

st.title("Watch Data System")

def get_product(product_id):
    response = requests.get(f"{API_URL}/products/{product_id}")
    return response.json()

product_id = st.number_input("Enter Product ID", min_value=1, step=1)
if st.button("Get Product"):
    product = get_product(product_id)
    st.json(product)
