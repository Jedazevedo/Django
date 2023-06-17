
from recipes.views import home,about,contato
from django.urls import path

# HTTP REQUEST

urlpatterns = [
        path('home/',home),
        path('sobre/', about),
        path('contato/',contato),
        path('/',home),
]
