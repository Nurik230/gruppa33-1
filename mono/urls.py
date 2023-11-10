from django.urls import path
from . import views

urlpatterns = [
    path('mobile/', views.mobile_list_view),
    path('mobile_detail/<int:id>/', views.mobile_detail_view),
    path('mobile/create/', views.mobile_create_views),
]