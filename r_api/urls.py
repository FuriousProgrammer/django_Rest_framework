from django.urls import path
from .views import artical_list, artical_detail,ArticalAPIView, DetailAPIView, GenericAPIViews

urlpatterns = [
    # path('artical', artical_list),
    path('artical',ArticalAPIView.as_view()),
    # path('detail/<int:pk>', artical_detail)
    path('detail/<int:id>/',DetailAPIView.as_view()),
    path('generic/artical/<int:id>', GenericAPIViews.as_view())
]