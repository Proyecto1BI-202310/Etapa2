from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        return render(request, 'home.html', {'message': message})
    return render(request, 'home.html')