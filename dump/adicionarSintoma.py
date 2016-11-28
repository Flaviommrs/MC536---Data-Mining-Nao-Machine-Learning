import csv
from estoque.models import Sintoma

with open('sintomasSemAcentoInc.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		s = Sintoma(row[1])
		s.save()
		
		
Sintoma.objects.all() #retorna todos os sintomas		