from sistema_django.wsgi import *
from appDjango.models import *
import random

data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

# delete from public.erp_category;
# ALTER SEQUENCE erp_category_id_seq RESTART WITH 1;

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

for i in range(1, 6000):
    nombre = ''.join(random.choices(letters, k=5))
    while Categoria.objects.filter(nombre=nombre).exists():
        nombre = ''.join(random.choices(letters, k=5))
    Categoria(nombre=nombre).save()
    print('Guardado registro {}'.format(i))
