"""
URL Mdoule for converter app
"""
from django.urls import path
from converter.views import HomePage, ConvertView

urlpatterns = [
    path("", HomePage.as_view(), name="home-page"),
    path("getCurr/", ConvertView.as_view(), name="convert-page")
]
