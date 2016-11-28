import csv
from estoque.models import Medicamento
with open('medicamentosF.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		m = Medicamento(row[1], row[3],row[2], row[4], row[0])
		m.save()
		
		
		
		
Medicamento.objects.all() #todos os medicamentos adicionados		