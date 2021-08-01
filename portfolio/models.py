from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Portfolio(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tech = models.ManyToManyField(Technology)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="portfolio", default="portfolio/portfolio.jpg")
    description = models.TextField(max_length=300, blank=True, null=True)
    client_name = models.CharField(max_length=50)
    company_url = models.CharField(max_length=20)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
