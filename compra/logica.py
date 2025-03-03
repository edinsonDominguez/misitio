# esta clase va interactuar con el carro de compras
class Compra:

    def __init__(self, request):
        self.request = request
        self.session = request.session

        compra = self.session.get('compra')    

        if not compra:
            compra = self.session['compra']={}
        
        self.compra = compra 

    # agrega los productos widget carrito
    def agregar(self, producto):
        if(str(producto.id) not in self.compra.keys()):
            self.compra[producto.id]={
                'producto_id' : producto.id,
                'nombre' : producto.nombre,
                'valor' : str(producto.valor),
                'cantidad': 1,
            }
        else:
            for key, value in self.compra.items():
                if key == str(producto.id):
                    value['cantidad'] = value['cantidad']+1
                    value['valor'] = float(value['valor']) + producto.valor
                    break
        self.guardar_compra()

    # agrega todos cambios en la session 
    def guardar_compra(self):
        self.session['compra'] = self.compra
        self.session.modified = True
    
    # elimina el producto del carrito
    def eliminar(self, producto):
        producto.id = str(producto.id)

        if producto.id in self.compra:
            del self.compra[producto.id]
            self.guardar_compra

    # hace la operacion de restar los productos en su cantidad y su valor   
    def restar_producto(self, producto):

        for key, value in self.compra.items():
            if key == str(producto.id):

                value['cantidad'] = value['cantidad']-1
                value['valor'] = float(value['valor']) - producto.valor

                # si el producto es menor a uno elimina el producto del carrito
                if value['cantidad'] < 1:
                    self.eliminar(producto)
                
                break
        
        self.guardar_compra()
    
    # limpia el carrito de compras 
    def limpiar_compra(self):
        self.session['compra']={}
        self.session.modified = True

