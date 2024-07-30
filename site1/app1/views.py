from django.http import HttpResponse


def index(request):
    return HttpResponse("This is website of 1337_DaKL")


def index1(request):
    return HttpResponse("come here and chill with me.")


def getout(request):
    return HttpResponse("Wtf , i don't like it , get out")
