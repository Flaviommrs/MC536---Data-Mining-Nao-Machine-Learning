from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Medicamento(models.Model):
	registro = models.IntegerField(default=0,primary_key=True)
	apresentacao = models.CharField(max_length = 300)
	nome_venda = models.CharField(max_length = 20)
	classe_terapeutica = models.CharField(max_length = 20)
	principio_ativo = models.CharField(max_length = 20)
	laboratorio = models.CharField(max_length = 20)
	hospitalar = models.CharField(max_length = 20)

	def __str__(self):
		return self.nome_venda

class Doenca(models.Model):
	nome_cientifico = models.CharField(max_length = 20, primary_key=True)
	nome_popular = models.CharField(max_length = 20)

	def __str__(self):
		return self.nome_cientifico

class Sintoma(models.Model):
	nome = models.CharField(max_length= 20, primary_key=True)

	def __str__(self):
		return self.nome

class Termo(models.Model):
	nome = models.CharField(max_length = 20, primary_key=True);

	def __str__(self):
		return self.nome

class Regiao(models.Model):
	nome = models.CharField(max_length = 20, primary_key=True);

	def __str__(self):
		return self.nome

class Trata(models.Model):
	dosagem = models.IntegerField(default=0)
	medicamento  = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
	doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE);

class Causa(models.Model):
	doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
	sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE)

class Refere(models.Model):
	sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE)
	termo = models.ForeignKey(Termo, on_delete=models.CASCADE)

class Busca(models.Model):
	frequencia = models.IntegerField(default=0);
	periodo = models.DurationField();
	termo = models.ForeignKey(Termo, on_delete=models.CASCADE)
	regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

class Incide(models.Model):
	incidencia = models.IntegerField(default=0);
	periodo = models.DurationField();
	doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
	regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)

