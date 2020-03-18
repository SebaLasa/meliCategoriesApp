import urllib.request
from prices.utils.jsonParser import JsonParser
from prices.controllers.appraiser import Appraiser

class MeliAPI:
    URL_MELI_CATEGORY = "https://api.mercadolibre.com/sites/MLA/search?category="
    URL_MELI_CATEGORIES = "https://api.mercadolibre.com/sites/MLA/categories"

    def categories_request(self):
        url = self.URL_MELI_CATEGORIES
        parser = JsonParser()
        categories = parser.parse(self.__request(url))
        return parser.dumps(categories)

    def category_request(self, category_id):
        url = self.URL_MELI_CATEGORY + category_id
        parser = JsonParser()
        category = parser.parse(self.__request(url))
        return category["results"]

    def suggested_category_prices(self, category_id):
        category_items = self.category_request(category_id)
        appraiser = Appraiser()
        prices_suggested = appraiser.get_suggested_price(list(category_items))
        parser = JsonParser()
        return parser.dumps(prices_suggested)

    def __request(self, url):
        response = urllib.request.urlopen(url)
        return response.read()


