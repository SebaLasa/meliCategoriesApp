from django.test import TestCase, Client, override_settings
from prices.controllers.appraiser import Appraiser


class PriceTests(TestCase):

    def test_appraiser_response_object_with_max_min_suggested_prices(self):
        appraiser = Appraiser()

        price_list = [{"price": 1},
                      {"price": 10}]
        price_result = {
            "max": 10,
            "suggested": 5,
            "min": 1
        }
        price_suggested = appraiser.get_suggested_price(price_list)
        self.assertDictEqual(price_result, price_suggested)


class ClientTest(TestCase):

    def test_index_response_404_status_code(self):
        client = Client()

        response = client.get('/')

        self.assertEqual(response.status_code, 404)

    def test_categories_json_response(self):
        client = Client()

        response = client.get('/categories/')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.content)

    def test_category_json_response(self):
        client = Client()

        response = client.get('/categories/MLA3530/')
        self.assertContains(response, "price", None, 200)

    def test_category_suggested_price_json_response(self):
        client = Client()

        response = client.get('/categories/MLA3530/prices')

        self.assertContains(response, "max", None, 200)
        self.assertContains(response, "min", None, 200)
        self.assertContains(response, "suggested", None, 200)


