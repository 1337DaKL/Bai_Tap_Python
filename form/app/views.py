from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .forms import PostForm


def add_post(request):
    a = PostForm()
    return render(request, 'app/ok.html', {'f': a})


def save_post(request):
    if request.method == "POST":
        a = PostForm(request.POST)
        if a.is_valid():
            a.save()
            return HttpResponse("ok")

        else:
            return HttpResponse("no")
    else:
        return HttpResponse("okkkkkk gooo")
