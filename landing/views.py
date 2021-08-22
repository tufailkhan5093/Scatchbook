from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "./landing/main.html")

def faq(request):
    return render(request, "./landing/faq.html")

