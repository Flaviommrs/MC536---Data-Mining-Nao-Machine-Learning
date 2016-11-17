import csv
with open('medicamentos.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		print row