from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')  # No need to include 'templates/' in the path
