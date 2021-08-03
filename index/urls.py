from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/<int:pk>/<slug:sl>/", views.portfolio, name="portfolio"),
    path("post/<int:pk>/<slug:sl>/", views.post, name="post"),
]
