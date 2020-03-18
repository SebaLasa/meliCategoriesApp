from django.http import HttpResponse, Http404
from prices.controllers.api.meliAPI import MeliAPI

def index(request):
    meliApi = MeliAPI()
    response = meliApi.categories_request()
    return HttpResponse(response)


def categories(request, category_id):
    meliApi = MeliAPI()
    response = meliApi.category_request(category_id)
    return HttpResponse(response)


def prices(request, category_id):
    meliApi = MeliAPI()
    response = meliApi.suggested_category_prices(category_id)
    return HttpResponse(response)
