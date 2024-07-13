from checkoutbot.core import start_scraping
from checkoutbot.ui.utils import load_template
from datetime import datetime

def run_template2():
    settings = load_template("examples/config/example_template2.json")
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
    run_template2()
