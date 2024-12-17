from django.shortcuts import render

# Create your views here.
def index(request):
    
    return render(request,'index.html')
def todo(request):
    return render(request,'todo.html')
def history(request):
    return render(request,'history.html')

