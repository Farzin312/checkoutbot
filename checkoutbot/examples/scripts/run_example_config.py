from checkoutbot.core import start_scraping
from checkoutbot.ui.utils import load_all_settings
from datetime import datetime

def run_example():
    settings = load_all_settings("examples/config/example_config.json")
    product_url = settings['scraping']['product_url']
    start_datetime = datetime.strptime(f"{settings['scraping']['start_date']} {settings['scraping']['start_time']}", "%Y-%m-%d %H:%M")
    
    start_scraping(
        product_url,
        settings['scraping']['min_price'],
        settings['scraping']['max_price'],
        settings['scraping']['quantity'],
        start_datetime,
        int(settings['scraping']['duration']),
        int(settings['scraping']['frequency']),
        settings['settings'].get('proxies'),
        settings['settings'].get('enable_ai')
    )

if __name__ == "__main__":
    run_example()
