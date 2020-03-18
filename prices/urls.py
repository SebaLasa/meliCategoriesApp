from django.urls import path

from . import views

urlpatterns = [
    # ex: /categories/
    path('', views.index, name='index'),
    # ex: /categories/MLA3530/
    path('<category_id>/', views.categories, name='categories'),
    # ex: /categories/MLA3530/prices
    path('<category_id>/prices', views.prices, name='prices')
]
