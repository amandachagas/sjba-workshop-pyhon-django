from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato

# Create your views here.

def index(request):
	# return HttpResponse('Ola Mundo!')
	return render(request, 'agenda.html')

