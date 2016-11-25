from django.shortcuts import render
from django.http import HttpResponse

from models import Medicamento, Doenca, Causa, Trata, Relaciona

# Create your views here.

def updateDB(request):
	return HttpResponse("Place Holder. Should update the DB.")

def fit(request):
	return HttpResponse("Should fit the machine learning")

def medicamentos(request, nomeDoenca):
	doenca = Doenca.objects.get(nome=nomeDoenca)
	causas = Causa.objects.filter(doenca=doenca)
	medicamentos = []

	for causa in causas:
		med = Trata.objects.filter(sintoma=causa.sintoma)
		for m in med:
			medicamentos.append(m)

	context = {'medicamentos': medicamentos}
	return render(request, 'estoque/medicamentos.html', context)

# def previsao(request, idRemedio):
# 	medicamento = Medicamentos.objects.get(registro=idRemedio)
# 	trata = Trata.objects.get(medicamento=medicamento)
# 	relaciona = Relaciona.objects(sintoma=trata.sintoma)


# 	return HttpResponse("Should Return prevision")


