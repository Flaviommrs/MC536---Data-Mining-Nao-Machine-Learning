from django.contrib import admin

from .models import Medicamento, Termo, Doenca, Sintoma, Regiao

# Register your models here.

admin.site.register(Medicamento)
admin.site.register(Doenca)
admin.site.register(Sintoma)
admin.site.register(Termo)
admin.site.register(Regiao)

