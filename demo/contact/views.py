from django.shortcuts import render
from .forms import contact_Form
from django.http import HttpResponse


def show(request):
    cf = contact_Form()
    cotext = {'cf01': cf}
    return render(request, 'contact/ok.html', cotext)


def getcontact(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            cf.save()
            return HttpResponse("Save sucessful !!!")
    else:
        return HttpResponse("Nhap sai thong tin cmnr ?????")
