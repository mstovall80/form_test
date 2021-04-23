from typing import ContextManager
from django.shortcuts import render
def index(request):
    return render(request,"index.html")

def create_user(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['location']
    Language_from_form = request.POST['language']
    context = {
    "name_on_template" : name_from_form,
    "Dojo_Location_on_template" : location_from_form,
    "Favorite_Language_on_template" : Language_from_form
    }
    return render(request,"show.html", context)
    
def success(request):
    return render(request,"show.html")
