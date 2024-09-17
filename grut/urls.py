from django.urls import path
from grut import views

urlpatterns = [
    path('', views.view1),
    path('c/', views.view2),
    path('list/', views.list_view),
    path('<id>/', views.detail_view),
    path('<id>/update', views.update_view),
    path('<id>/delete', views.delete_view),
]
