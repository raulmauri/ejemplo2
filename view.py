from django.views.generic import TemplateView

class InicioView(TemplateView):
    template_name = "inicio.html"

class FirstView(TemplateView):
    template_name = "first.html"

class SecondView(TemplateView):
    template_name = "second.html"
    
class ThirdView(TemplateView):
    template_name = "third.html"
    