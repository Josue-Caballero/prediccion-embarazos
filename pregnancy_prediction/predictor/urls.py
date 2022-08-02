
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('api/v0.1/predict-registers/', views.predictFromRegistersView),
    path('api/v0.1/predict-file/', views.predictFromFileView)
]
