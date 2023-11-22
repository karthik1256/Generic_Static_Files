from django.shortcuts import render

# Create your views here.

def minions(request):
    return render(request,'minions.html')


def tomjerry(request):
    return render(request,'tomjerry.html')

