from src.scraper import scrape_by_bbox
from src.bbox_generator import generate_usa_bboxes
import time
import sys
import logging


sys.path.append('/app/src')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Scraper starting...")
    try:
        while True:  # Sonsuz döngü
            for bbox in generate_usa_bboxes():
                scrape_by_bbox(bbox)
                time.sleep(2)
            logger.info("Scraping cycle completed")
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")