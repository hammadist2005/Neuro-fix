import requests
from bs4 import BeautifulSoup
import urllib.parse
import streamlit as st
import json
import os

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=10, pool_maxsize=10)
session.mount('https://', adapter)

session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate', 
    'Connection': 'keep-alive'
})

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database', 'price_memory.json'))

@st.cache_data(ttl=600, show_spinner=False)
def check_czone_price(component_name):
    # 1. Clean Query
    clean_query = component_name.replace("I need to buy a ", "").replace("new ", "").lower()
    
    # 2. SAFETY NET (This will save your Demo)
    try:
        if os.path.exists(DB_PATH):
            with open(DB_PATH, 'r') as f:
                data = json.load(f)
            
            # Smart Matching: If input is "nvme ssd", and we have "ssd", use it.
            for key in data:
                if key in clean_query:
                    return {
                        "found": True,
                        "title": data[key]['title'],
                        "price": data[key]['price'],
                        "link": data[key]['link'],
                        "source": data[key]['source']
                    }
    except Exception:
        pass 

    # 3. LIVE SCRAPER (Backup - Reverted to 'q')
    try:
        base_url = "https://www.czone.com.pk/search.aspx"
        params = {'q': clean_query}  # Back to standard 'q'
        search_url = f"{base_url}?{urllib.parse.urlencode(params)}"
        
        response = session.get(search_url, timeout=5)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            first_product = soup.find('div', class_='product')
            
            if first_product:
                title_tag = first_product.find('h4')
                price_tag = first_product.find('div', class_='price')
                link_tag = first_product.find('a')
                
                if title_tag and price_tag and link_tag:
                    return {
                        "found": True,
                        "title": title_tag.text.strip(),
                        "price": price_tag.text.strip(),
                        "link": "https://www.czone.com.pk" + link_tag['href'],
                        "source": "CZone (Live)"
                    }
        
        return {"found": False, "link": search_url}

    except Exception:
        return {"found": False, "link": search_url}