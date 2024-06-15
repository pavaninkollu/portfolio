
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]