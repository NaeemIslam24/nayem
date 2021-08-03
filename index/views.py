from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from about.models import *
from portfolio.models import *
from blog.models import *

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
    post = Post.objects.all()

    context = {
        "home": home,
        "portfolios": portfolio,
        "bio": bio,
        "about": about,
        "i_do": i_do,
        "clients": client,
        "testimonial": testimonial,
        "posts": post,
    }

    return render(request, template_name=template, context=context)


def portfolio(request, pk, sl):
    template = "portfolio-1.html"

    portfolio = Portfolio.objects.all()

    detail = get_object_or_404(portfolio, id=pk, slug=sl)

    context = {
        "portfolio": detail,
    }

    return render(request, template_name=template, context=context)


def post(request, pk, sl):

    template = "blog-post-1.html"

    post = Post.objects.all()
    home = Home.objects.all()

    detail = get_object_or_404(post, id=pk, slug=sl)

    context = {
        "post": detail,
        "home": home,
    }

    return render(request, template_name=template, context=context)
