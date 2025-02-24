from django.contrib import admin
from django.urls import path

from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TodosView.as_view(), name='home'),
    path('<int:pk>/', views.DelView.as_view(), name='del')
]
