from django.shortcuts import render
from .models import Comentario
from django.db.models import Count

def hotel_chart(request):
    # Obtener la cantidad de hoteles con negativo=True y negativo=False
    negativos = Comentario.objects.filter(negativo=True).count()
    no_negativos = Comentario.objects.filter(negativo=False).count()
    
    # Crear los datos para el gráfico
    labels = ['Negativos', 'No negativos']
    values = [negativos, no_negativos]
    
    # Crear un diccionario con los datos del gráfico para pasar al template
    context = {'labels': labels, 'values': values}
    
    return render(request, 'hotel_chart.html', context)

# Create your views here.
def get_Negativos(request):
    objetos_negativos = Comentario.objects.filter(negativo=True)
    context = {'objetos': objetos_negativos}
    return render(request, 'lavista.html', context)

def get_Palabras(request):
    comentarios = Comentario.objects.all()
    palabras = ['asin', 'asco', 'ausencia', 'ausenci', 'car', 'carisim', 'cucarach', 'cucaracha', 'corresponder', 'cuatro', 'deficient', 'decepcion', 'des', 'desear', 'decente', 'lamentable', 'educacion', 'esperar', 'horror', 'horrible', 'horribl', 'junior', 'jabon', 'lament', 'muell', 'pesim', 'pesimo', 'pesimar', 'pasable', 'pasabl', 'pared', 'rot', 'sucio', 'suci', 'sabana', 'saban', 'teni', 'vending', 'diecioch', 'dieciocho', 'cristobal', '360o', 'doscientos']
    negWords = []
    for comentario in comentarios :
        for palabra in comentario.texto.split():
            if palabra in palabras:
                negWords.append(palabra)

    context = {'palabras': negWords}
    return render(request, 'laspalabras.html', context)
