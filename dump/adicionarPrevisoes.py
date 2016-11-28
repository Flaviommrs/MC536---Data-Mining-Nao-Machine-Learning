import csv
from estoque.models import Sintoma, Regiao, Previsao

with open('readaux.txt', 'r') as f:
	myList = f.read().splitlines()
	
for elem in myList:
	with open(elem, 'rb') as f:
		reader = csv.reader(f)
		i = 0
		tipoP = "nao-parametrica"
		nomeSintoma = ""
		for row in reader:
			if i == 0:
				nomeSintoma = row[0]
				print nomeSintoma
			else:
				if row[0] != "Date":
					r = Regiao.objects.get(nome = row[0])
					print r
					j = 0
					aux = ""
					for previsao in row:
						if j!= 0:
							if j == 1:
								aux = aux + previsao
							else:
								aux = aux + "," + previsao
						j = j + 1
					s = Sintoma.objects.get(nome=nomeSintoma)
					p = Previsao(tipo = tipoP, resultado = aux, regiao =r, sintoma = s)
					print parametricap.save()
			i = i + 1		