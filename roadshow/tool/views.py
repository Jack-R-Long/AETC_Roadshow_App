from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # Some code to get db info
    return render(request, 'tool/index.html')
