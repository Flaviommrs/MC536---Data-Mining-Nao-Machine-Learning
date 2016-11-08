from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def updateDB(request):
	return HttpResponse("Place Holder. Should update the DB.")

def fit(request):
	return HttpResponse("Should fit the machine learning")
