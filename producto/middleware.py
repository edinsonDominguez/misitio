from django.utils.deprecation import MiddlewareMixin
# queda pendiente por desarrollar 
class ProductoMid(MiddlewareMixin):
    
    def proceso_id_usuario(self, request):

        if request.user.is_authenticated:
            print(f'el nombre del usario es: {request.user.username} ')
