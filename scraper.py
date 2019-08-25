import requests
import yaml
from bs4 import BeautifulSoup

from csv_maker import CsvMaker
from parsers.parser import Parser

PER_PAGE_DATA = "250"

COURSE = "COURSE"

PAGES = "PAGE_LIMIT"

BASE_URL = "BASE_URL"


class Scraper(object):

    def __init__(self):
        self.__load_config()
        self.parser = Parser()
        self.csv_maker = CsvMaker()
        self.page_number = 1

    def scrape(self):
        data = []
        for page_no in range(1, self.config[PAGES]):
            self.page_number = page_no
            data  = data + self.scrape_page()
        self.csv_maker.make(data)

    def scrape_page(self):
        print "Scraping Page No: {}".format(self.page_number)
        resp = requests.get(self.__url_endpoint(), self.__query_dict())
        soup = BeautifulSoup(resp.text, 'html.parser')
        table = soup.findAll(True, {'class': ['row0', 'row1']})
        return self.parser.parse(table)

    def __load_config(self):
        self.config = yaml.safe_load(open('config.yaml'))

    def __url_endpoint(self):
        return self.config[BASE_URL]

    def __query_dict(self):
        query_dict = {'pp': PER_PAGE_DATA, 'p': self.page_number}
        if self.config.has_key(COURSE):
            query_dict['q'] = self.config[COURSE]
        print query_dict
        return query_dict
