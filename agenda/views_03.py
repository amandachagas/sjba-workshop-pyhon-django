from django.shortcuts import render
from django.http import HttpResponse
from .models import Contato

# Create your views here.

def index(request):
	if request.method == 'POST':
		Contato.objects.create(
				nome=request.POST['this-nome'],
				telefone=request.POST['this-telefone']
			)

	contatos = Contato.objects.all()
	# return HttpResponse('Ola Mundo!')
	return render(request, 'agenda.html',
		{'contatos': contatos})

