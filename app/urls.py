from django.urls import path
from .views import Home,Predict,Result


urlpatterns = [
    path("",Home.as_view(),name = "home"),
    path("predict/",Predict.as_view(),name = "predict"),
    path("result/<int:pk>/", Result.as_view(), name="result"),  
    ]