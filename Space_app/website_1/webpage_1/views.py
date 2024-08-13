from django.shortcuts import render



def index(request):
    return render(request, 'webpage_1/index.html')