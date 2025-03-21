from django.urls import path
from django.views.generic import TemplateView

from .views import TrendingWordsView

app_name = "Apps"

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name = "homepage"),
    path('trending-words/', TrendingWordsView.as_view(), name='trending-words'),
]