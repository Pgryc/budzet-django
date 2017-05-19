from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index (request):
 	return render(request, 'mainapp/index.html', {}, content_type='text/html')

def widok (request):
 	return render(request, 'mainapp/widok.html', {}, content_type='text/html')