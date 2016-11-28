import csv
from estoque.models import Doenca

with open('sintomasSemAcentoInc.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		d = Doenca(row[0])
		d.save()
		
		
Doenca.objects.all() #retorna todas as doencas		