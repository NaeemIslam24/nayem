from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):

    template= 'index.html'
    home = Home.objects.all()
    bio = Slide_bio.objects.all()
    about = About_me.objects.all()
    i_do = What_i_do.objects.all()
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()

    context={

        'home': home,
        'bio': bio,
        'about': about,
        'i_do': i_do,
        'clients': client,
        'testimonial': testimonial,
    }

    return render(request, template_name=template, context=context)

def portfolio(request):

    template= 'portfolio-1.html'
 
    return render(request, template_name=template)