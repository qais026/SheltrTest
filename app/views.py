from django.shortcuts import render
from app.models import Provider
# Create your views here.

def index(request):
    providers = Provider.objects.order_by("-name")
    return render(request, 'app/index.html', {"providers": Provider})