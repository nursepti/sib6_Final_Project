import finnhub
import config as conf

def scrape_news():
    finnhub_client = finnhub.Client(conf.API_KEY)

    news = finnhub_client.general_news('general', min_id=0)

    return news