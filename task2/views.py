from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def func_web(request):
    return render(request, 'func_templates.html')

class class_web(TemplateView):
    template_name = 'class_templates.html'
