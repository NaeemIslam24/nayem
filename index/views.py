from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from about.models import *
from portfolio.models import *

# Create your views here.
def index(request):

    template = "index.html"
    home = Home.objects.all()
    bio = Slide_bio.objects.all()
    about = About_me.objects.all()
    i_do = What_i_do.objects.all()
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()
    portfolio = Portfolio.objects.all()

    context = {
        "home": home,
        "portfolio": portfolio,
        "bio": bio,
        "about": about,
        "i_do": i_do,
        "clients": client,
        "testimonial": testimonial,
    }

    return render(request, template_name=template, context=context)


def portfolio(request, pk, sl):
    template = "portfolio-1.html"

    portfolio = Portfolio.objects.all()

    detail = get_object_or_404(portfolio, id=pk, title=sl)

    context = {
        "portfolio": detail,
    }

    return render(request, template_name=template, context=context)
