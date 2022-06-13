import BBC_scraper
import flights_scraper
from articles_manager import ArticleManager
from flight_manager import FlightManager
import threading

class KillableThread(threading.Thread):
    def __init__(self, target, args=None, sleep_interval=1):
        super().__init__()
        self._kill = threading.Event()
        self._interval = sleep_interval
        self._function = target
        self._function_args = args if args else []

    def run(self):
        while True:
            self._function(*self._function_args)
            self._kill.wait(self._interval)
            if self.killed():
                break

    def killed(self):
        return self._kill.isSet()

    def kill(self):
        self._kill.set()

def thread_flight_scraper():
    flight_manager = FlightManager()
    data = flights_scraper.scrape_flights()
    flight_manager.create_new_flights_table(data)

def run_flight_scraper():
    t = KillableThread(target=thread_flight_scraper, sleep_interval=60)
    t.start()
    operation = input("Press any key to stop\n")
    t.kill()
    print("Stopping for the scraper...")
    t.join()

def run_flight_search():
    flight_manager = FlightManager()
    if flight_manager.get_flight_table_count() == 0:
        print("database is empty")
        return
    company_name = input("Please enter a company name\n")
    result = flight_manager.search_flight_by_company(company_name)
    for f in result:
        print(f)

def run_BBC_scraper():
    articles_manager = ArticleManager()
    data = BBC_scraper.scrape_BBC_articles()
    articles_manager.update_articles_table(data)

def run_BBC_articles_search():
    articles_manager = ArticleManager()
    if articles_manager.get_articles_count() == 0:
        print("database is empty")
        return
    keyword = input("Please enter a keyword for search\n")
    result = articles_manager.search_article_by_keyword(keyword)
    print(result)

def main():
    operation = input("Please choose operation:\n1 - BBC scraping\n2 - Flights scraping\n3 - Search BBC's articles\n4 - Search for flights\n")
    operation = int(operation)

    if operation == 1:
        run_BBC_scraper()
    elif operation == 2:
        run_flight_scraper()
    elif operation == 3: #Search for articles
        run_BBC_articles_search()
    elif operation == 4:  # Search for flights
        run_flight_search()
    else:
        print("Incorrect number!")


if __name__ == '__main__':
    main()