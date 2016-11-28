from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Medicamento(models.Model):
	registro = models.CharField(max_length = 30,primary_key=True)
	apresentacao = models.CharField(max_length = 300)
	nome_venda = models.CharField(max_length = 20)
	classe_terapeutica = models.CharField(max_length = 20)
	principio_ativo = models.CharField(max_length = 20)
	#laboratorio = models.CharField(max_length = 20)
	#hospitalar = models.CharField(max_length = 20)

	def __str__(self):
		return self.nome_venda

class Doenca(models.Model):
	#nome_cientifico = models.CharField(max_length = 20, primary_key=True)
	nome_popular = models.CharField(max_length = 20, primary_key=True)

	def __str__(self):
		return self.nome_popular

class Sintoma(models.Model):
	nome = models.CharField(max_length= 50, primary_key=True)

	def __str__(self):
		return self.nome

class Regiao(models.Model):
	nome = models.CharField(max_length = 20, primary_key=True)

	def __str__(self):
		return self.nome

class Previsao(models.Model):
	tipo = models.CharField(max_length=20)
	resultado = models.TextField()
	regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, default=None)
	sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return "resultado do tipo: " + self.tipo + " para o sintoma: " + self.sintoma.nome + " na regiao: " + self.regiao.nome

class Trata(models.Model):
	medicamento  = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
	sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE, default=None)

	def __str__(self):
		return self.medicamento.nome_venda + " trata " + self.sintoma.nome

class Causa(models.Model):
	doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
	sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE)

	def __str__(self):
		return self.doenca.nome_popular + " causa " + self.sintoma.nome
