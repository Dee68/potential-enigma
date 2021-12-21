from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'blog/index.html', context)

def account_page(request):
    context = {}
    return render(request, 'blog/account.html', context)