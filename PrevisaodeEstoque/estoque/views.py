from django.shortcuts import render
from django.http import HttpResponse
import json

from models import Medicamento, Doenca, Causa, Trata

# Create your views here.

# def updateDB(request):
# 	return HttpResponse("Place Holder. Should update the DB.")

# def fit(request):
# 	return HttpResponse("Should fit the machine learning")

def filtro(request):
	return render(request, 'estoque/filtro.html')

def equipe(request):
	return render(request, 'estoque/equipe.html')

def help(request):
	return render(request, 'estoque/help.html')

def mapa(request):
	return render(request, 'estoque/mapa.html')


def medicamentos(request, nomeDoenca):
	doenca = Doenca.objects.get(nome_popular=nomeDoenca)
	causas = Causa.objects.filter(doenca=doenca)
	medicamentos = []

	for causa in causas:
		med = Trata.objects.filter(sintoma=causa.sintoma)
		for m in med:
			aux = { 
				'Registro':m.medicamento.registro, 
				'Apresentacao':m.medicamento.apresentacao, 
				'PrincipioAtivo':m.medicamento.principio_ativo, 
				'Nome':m.medicamento.nome_venda, 
				'ClasseTerapeutica':m.medicamento.classe_terapeutica
				}
			medicamentos.append(aux)

	json_data = json.dumps(medicamentos)

	context = {'medicamentos': json_data}

	return render(request, 'estoque/medicamentos.html', context)

# def previsao(request, idRemedio):
# 	medicamento = Medicamentos.objects.get(registro=idRemedio)
# 	trata = Trata.objects.get(medicamento=medicamento)
# 	relaciona = Relaciona.objects(sintoma=trata.sintoma)


# 	return HttpResponse("Should Return prevision")


