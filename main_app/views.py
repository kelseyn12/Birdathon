from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello Birds</h1>')

def about(request):
    return render(request, 'about.html')