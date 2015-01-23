from django.shortcuts import render
from app.models import Provider
# Create your views here.

def index(request):
    providers = Provider.objects.order_by("-name")
    return render(request, 'app/index.html', {"providers": Provider})

# About Us page
def about(request):
    return render(request, "about.html")

# Contact Us page
def contact(request):
    return render(request, "contact.html")

