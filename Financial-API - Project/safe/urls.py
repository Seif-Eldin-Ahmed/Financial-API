from django.urls import path
from django.views.generic import TemplateView

app_name = 'safe'

urlpatterns = [
    path('', TemplateView.as_view(template_name="safe/index.html"))
]