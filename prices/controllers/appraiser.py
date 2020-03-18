import math
import statistics


class Appraiser:

    def get_suggested_price(self, items_list):
        minimum = items_list[0]["price"]
        maximum = items_list[0]["price"]
        price_list = list()
        for item in items_list:
            if item["price"] < minimum:
                minimum = item["price"]
            if item["price"] > maximum:
                maximum = item["price"]
            price_list.append(item["price"])

        median = math.floor(statistics.median(price_list))
        price_result = {
            "max": maximum,
            "suggested": median,
            "min": minimum
        }
        return price_result
