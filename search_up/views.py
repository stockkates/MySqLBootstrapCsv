from django.shortcuts import render

# Create your views here.

def index(request):
    user = request.user
    if user.is_superuser:
        return render(request, 'index.html')
    return render(request, 'index.html')