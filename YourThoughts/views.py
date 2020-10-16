from django.shortcuts import render,redirect

from YourThoughts.forms import PostForm
from YourThoughts.models import Registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.template.context import RequestContext
# Create your views here.

def Home(request):
    return render(request, "myapp/blog-home.html")
def login(request):
    return render(request, "myapp/login.html")
def register(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/Login/")

    else:
        # GET request, present an empty form
        form = PostForm()
    return render(request, 'myapp/registerpage.html', {"form": form})




