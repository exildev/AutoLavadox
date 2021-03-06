from django.contrib import admin
from exileui.admin import exileui, ExStacked, ExTabular, DateRangeEX
import models
from django.utils.html import format_html
import forms
from django.db import connection
# Register your models here.


class TipoServicioAdmin(admin.ModelAdmin):
    form = forms.AddTipoServicioForm
    list_display = ['id_cierre','inicio','fin','total','comision','accion_reporte']
    list_filter = ['id','inicio','fin',]
    search_fields = ['id','inicio','fin','total']
    list_display_links = ('id_cierre',)

    def id_cierre(self, obj):
        i = 0
        men = ''
        while i < 10 - len(str(obj.pk)):
            men = men + '0'
            i = i+1
        # end ford
        return '%s%d' % (men, obj.pk)
    # end def

    def accion_reporte(self, obj):
        return format_html("<a href='/cierre/factura/tipo/{0}/' class='generar addlink'>Imprimir</a>", obj.id)
    # end def

    def save_model(self, request, obj, form, change):
        cursor = connection.cursor()
        cursor.execute('select cierre_factura_total(\'%s\',\'%s\')'%(str(obj.inicio),str(obj.fin)))
        row = cursor.fetchone()
        r = row[0][0]
        obj.total=r['total']
        obj.comision=r['comosion']
        obj.save()
    # end def

    class Media:
        js = ('/static/cierre/js/cierre.js',)
    # end class

    id_cierre.allow_tags = True
    id_cierre.short_description = 'Cierre Id'
    accion_reporte.allow_tags = True
    accion_reporte.short_description = 'Reporte Dia'
# end class


class FacturaAdmin(admin.ModelAdmin):
    form = forms.AddTipoServicioForm
    list_display = ['id_cierre','inicio','fin','total','comision','accion_reporte']
    list_filter = ['id','inicio','fin',]
    search_fields = ['id','inicio','fin','total']
    list_display_links = ('id_cierre',)

    def id_cierre(self, obj):
        i = 0
        men = ''
        while i < 10 - len(str(obj.pk)):
            men = men + '0'
            i = i+1
        # end ford
        return '%s%d' % (men, obj.pk)
    # end def

    def accion_reporte(self, obj):
        return format_html("<a href='/cierre/factura/{0}/' class='generar addlink'>Imprimir</a>", obj.id)
    # end def

    def save_model(self, request, obj, form, change):
        obj.save()
        cursor = connection.cursor()
        cursor.execute('select cierre_factura_total(\'%s\',\'%s\')'%(str(obj.inicio),str(obj.fin)))
        row = cursor.fetchone()
        r = row[0][0]
        obj.total=r['total']
        obj.comision=r['comosion']
        obj.save()
    # end def

    class Media:
        js = ('/static/cierre/js/cierre.js',)
    # end class

    id_cierre.allow_tags = True
    id_cierre.short_description = 'Cierre Id'
    accion_reporte.allow_tags = True
    accion_reporte.short_description = 'Reporte Dia'
# end class

exileui.register(models.TipoServicio, TipoServicioAdmin)
exileui.register(models.Factura, FacturaAdmin)
