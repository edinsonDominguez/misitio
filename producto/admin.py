from django.contrib import admin

from producto.models import Producto,Categoria,Imagen

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('fecha_registro', 'nombre', 'valor', 'inventario', 'categoria_producto', 'usuario')
    list_filter = ('fecha_registro', 'inventario')
    ordering = ('valor',)
    search_fields = ('nombre',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('foto1', 'foto2', 'foto3', 'foto4', 'foto5', 'foto6',)


admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Imagen, ImagenAdmin)