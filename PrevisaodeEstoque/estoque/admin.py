from django.contrib import admin

from .models import Medicamento, Doenca, Sintoma, Regiao, Previsao, Causa

# Register your models here.

admin.site.register(Medicamento)
admin.site.register(Doenca)
admin.site.register(Sintoma)
admin.site.register(Regiao)
admin.site.register(Previsao)
admin.site.register(Causa)
