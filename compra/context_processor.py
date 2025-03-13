# se guardara la variable de calcular costos 

def imprimir_context(request):
    cantidad = 0
    cantidad = len(request.session['compra'].items())
    # esta es la variable que se imprime
    return {'texto': cantidad}

# esta funcion va a imprimir la suma de lo que el cliente compre
def total_carrito(request):
    valor = 0
    for key, value in request.session['compra'].items():
        valor = valor + float(value['valor'])

    return {'total_carro': valor}