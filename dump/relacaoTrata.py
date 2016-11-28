import csv
from estoque.models import Sintoma, Medicamento, Trata

for s in Sintoma.objects.all():
	m = Medicamento.objects.filter(classe_terapeutica = s.nome)
	for u in m:
		t = Trata(sintoma = s, medicamento = u)
		t.save()
		
		
Trata.objects.all() #retorna todas as relacoes do tipo trata		