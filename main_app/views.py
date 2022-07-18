from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
	return HttpResponse('<h1>Bruh This is the about page</h1>')