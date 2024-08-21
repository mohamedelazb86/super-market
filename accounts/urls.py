from django.urls import path
from .views import signup,activate

urlpatterns = [
    path('signup',signup),
    path('activate/<str:username>',activate),
]
