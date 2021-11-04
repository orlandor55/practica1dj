from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Habilidades)


class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name'
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    list_filter = ('job',)
#     inlines = [
#         Inline,
#     ]
#    raw_id_fields = ('first_name',)
    readonly_fields = ('job',)
    search_fields = ('first_name','job','departamento',)
#     date_hierarchy = ''
    ordering = ('first_name',)
    filter_horizontal = ('habilidad',)

admin.site.register(Colaborador, ColaboradoresAdmin)

