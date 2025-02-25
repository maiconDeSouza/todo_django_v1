from django.contrib import admin
from django.urls import path

from todos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TodosView.as_view(), name='home'),
    path('<int:pk>/update', views.UpView.as_view(), name='up'),
    path('<int:pk>/delete', views.DelView.as_view(), name='del'),
    path('<int:pk>/completed', views.CompletedView.as_view(), name='completed')
]
