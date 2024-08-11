
from django.urls import path
from . import views

urlpatterns = [
#    path("<str:month>", views.udemy),
   path("january/", views.udemy),
   path("february/", views.udemy),
   path("march/", views.udemy)
]


