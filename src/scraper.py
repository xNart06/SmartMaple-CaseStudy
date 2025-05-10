import requests
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def scrape_by_bbox(bbox):
    url = "https://thedyrt.com/api/v6/locations/search-results"
    params = {
        "filter[search][bbox]": bbox,
        "sort": "recommended",
        "page[size]": 500,
        "page[number]": 1,
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json",
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        if data.get("data"):
            logger.info(f"BBOX: {bbox} → {len(data['data'])} kamp alanı bulundu")
            for camp in data["data"]:
                logger.info("🏕️ " + camp["attributes"]["name"])
        else:
            logger.info(f"BBOX: {bbox} → Veri bulunamadı.")
    except requests.exceptions.RequestException as e:
        logger.error(f"API Hatası: {e}")

def generate_usa_bboxes():
    bboxes = []
    for lat in range(25, 50):    
        for lng in range(-125, -65): 
            bbox = f"{lng},{lat},{lng+1},{lat+1}"
            bboxes.append(bbox)
    return bboxes

if __name__ == "__main__":
    logger.info("Scraper başlatılıyor...")
    try:
        bboxes = generate_usa_bboxes()
        for bbox in bboxes:
            logger.info(f"BBOX taranıyor: {bbox}")
            scrape_by_bbox(bbox)
            time.sleep(1.5)  # API limitine takılmamak için
        logger.info("✅ Tüm BBOX'lar tarandı. İşlem tamamlandı.")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
