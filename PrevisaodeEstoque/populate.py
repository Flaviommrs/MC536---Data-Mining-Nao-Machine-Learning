import csv
from django.conf import settings
settings.configure()
from estoque.models import Medicamento

with open('medicamentos.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		print row