from apscheduler.schedulers.blocking import BlockingScheduler
from src.scraper import scrape_all_us_campgrounds

def scheduled_job():
    try:
        scrape_all_us_campgrounds()
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # Günlük her saat 12'de çalışacak şekilde ayarladım
    scheduler.add_job(scheduled_job, 'cron', hour=0, minute=0)
    scheduler.start()
