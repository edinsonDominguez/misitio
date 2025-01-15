from django.contrib import admin

from producto.models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('fecha_registro', 'nombre', 'valor', 'inventario')
    list_filter = ('fecha_registro', 'inventario')
    ordering = ('valor',)
    search_fields = ('nombre',)


admin.site.register(Producto, ProductoAdmin)
