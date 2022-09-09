from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def portfolio(request):

    return render(request, "core/portfolio.html")

