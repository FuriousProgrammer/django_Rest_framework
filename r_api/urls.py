from django.urls import path
from .views import artical_list, artical_detail

urlpatterns = [
    path('artical', artical_list),
    path('detail/<int:pk>', artical_detail)
]