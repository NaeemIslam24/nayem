from django.db import models


class About_me(models.Model):

    description = models.TextField(max_length=500, blank=True, null=True)
    age = models.CharField(max_length=5, blank=True, null=True)
    residence = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email


class What_i_do(models.Model):

    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):

    image = models.ImageField(
        upload_to="testimonial", default="testimonial/testimonial-1.jpg"
    )
    comment = models.TextField(max_length=300, blank=True, null=True)
    client_name = models.CharField(max_length=20)
    company = models.CharField(max_length=20)

    def __str__(self):
        return self.company


class Client(models.Model):

    company_logo = models.ImageField(
        upload_to="clients", default="clients/client-1.png"
    )
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.url
