from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from appDjango.models import Categoria
from appDjango.forms import CategoriaForm


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/list.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for l in Categoria.objects.all():
                    data.append(l.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
        
    def get_queryset(self):
        return Categoria.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorias'
        context['create_url'] = reverse_lazy('home:crear_categoria')
        context['list_url'] = reverse_lazy('home:lista_categoria')
        context['entity'] = 'Categorías'
        return context


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/create.html'
    success_url = reverse_lazy('home:lista_categoria')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear una Categoria'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('home:lista_categoria')
        context['action'] = 'add'
        return context
    

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/create.html'
    success_url = reverse_lazy('home:lista_categoria')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Categoria'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('home:lista_categoria')
        context['action'] = 'edit'
        return context
    

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/delete.html'
    success_url = reverse_lazy('home:lista_categoria')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Categoria'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('home:lista_categoria')
        return context
    