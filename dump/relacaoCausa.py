import csv
from estoque.models import Doenca, Sintoma, Causa
with open('sintomasSemAcentoInc.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		d = Doenca.objects.get(nome_popular = row[0])
		s = Sintoma.objects.get(nome = row[1])
		c = Causa(doenca=d, sintoma = s)
		c.save()
		

Causa.objects.all() #retorna todas as relacoes do tipo causa				