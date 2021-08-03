from django.db import models

# Create your models here.
STATUS_CHOICE = (
    ("freelance available", "Freelance Available"),
    ("freelance not available", "Freelance not available"),
)


class Contact(models.Model):

    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    working_status = models.CharField(choices=STATUS_CHOICE, max_length=100)

    def __str__(self):
        return self.email


class Contact_Form(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.name
