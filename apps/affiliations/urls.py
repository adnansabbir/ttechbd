from django.urls import path
from . import views

urlpatterns = [
    path('', views.affiliation_list, name='affiliation_list'),
    path('<int:project_id>', views.affiliation, name='affiliation_single')
]