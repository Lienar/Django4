from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def main_page(request):
    return render(request, 'title_page.html')

def store_page(request):
    list = ["Эвердейл", "Мертвый сезон", "Манчкин", "Экипаж", "Simulo", "Мафия"]
    contecxt = {'list': list, }
    return render(request, 'store_page.html', contecxt)

def basket_page(request):
    return render(request, 'basket_page.html')

