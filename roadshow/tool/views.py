from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def new(request):
    # Some code
    return render(request, 'tool/new.html')

def old(request):
    # Some code to get db info
    return render(request, 'tool/old.html')
