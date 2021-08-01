from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/<int:pk>/<str:sl>/", views.portfolio, name="portfolio"),
]
