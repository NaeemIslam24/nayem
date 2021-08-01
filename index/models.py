from django.db import models
from django.utils import timezone

# Create your models here.
class Home(models.Model):

    profile_image = models.ImageField(upload_to="profile", null=True, blank=True)
    profile_name = models.CharField(max_length=20)
    profile_bio = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    wallpaper_name = models.CharField(max_length=50)
    wallpaper_last_name = models.CharField(max_length=50)
    footer_text = models.CharField(max_length=100)
    add_cv = models.FileField()

    def __str__(self):
        return self.profile_name


class Slide_bio(models.Model):

    bio = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.bio
