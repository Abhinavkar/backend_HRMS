# employee_management_app/views.py
from django.core.cache import cache
from django.http import HttpResponse

def set_cache(request):
    cache.set('my_key', 'Hello, Redis!', timeout=60)
    return HttpResponse('Cache set!')

def get_cache(request):
    value = cache.get('my_key')
    return HttpResponse(f'Cache value: {value}')
