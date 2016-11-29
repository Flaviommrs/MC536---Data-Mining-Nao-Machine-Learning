from django.shortcuts import render
from django.http import HttpResponse
import json

from models import Medicamento, Doenca, Causa, Trata, Previsao

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
			aux = [
				m.medicamento.registro, 
				m.medicamento.apresentacao, 
				m.medicamento.principio_ativo, 
				m.medicamento.nome_venda, 
				m.medicamento.classe_terapeutica
				]
			medicamentos.append(aux)

	json_data = json.dumps(medicamentos)

	context = {'medicamentos': json_data}

	return render(request, 'estoque/filtro.html', context)

def previsao(request, registro):

	medicamento = Medicamento.objects.get(registro=registro)
	trata = Trata.objects.get(medicamento=medicamento)

	data = []
	previsoes = Previsao.objects.filter(sintoma=trata.sintoma)

	for previsao in previsoes:
		array = previsao.resultado.split(',')
		resultado = []
		for ponto in array:
			resultado.append(float(ponto))
		aux = [
			previsao.tipo,
			previsao.regiao.nome,
			resultado
		]
		data.append(aux)

	json_data = json.dumps(data)

	context = {'previsao': json_data}


	return render(request, 'estoque/mapa.html', context)


