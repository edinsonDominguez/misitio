from django.contrib import admin

from producto.models import Producto,Categoria,Imagen

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('fecha_registro', 'nombre', 'valor', 'inventario', 'categoria_producto', 'usuario', 'foto1')
    list_filter = ('fecha_registro', 'inventario')
    ordering = ('-fecha_registro',)
    search_fields = ('nombre',)

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user 
        return super().save_model(request, obj, form, change)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)



admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
