from django.urls import path, re_path
#from appDjango.views.categoria.views import lista_categoria
from appDjango.views.categoria.views import *

app_name = 'appDjango'

urlpatterns = [
    path('categoria/lista/', CategoriaListView.as_view(), name='lista_categoria'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='crear_categoria'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='editar_categoria'),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='eliminar_categoria'),
]
