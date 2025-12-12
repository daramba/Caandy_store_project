# from django.shortcuts import render, get_object_or_404
# from .models import Sweet, Brand, SweetType

# # Главная страница
# def home(request):
#     sweets = Sweet.objects.all()[:12]  # 12 последних сладостей
#     brands = Brand.objects.all()
#     types = SweetType.objects.all()
    
#     context = {
#         'sweets': sweets,
#         'brands': brands,
#         'types': types,
#     }
#     return render(request, 'home.html', context)

# # Страница всех сладостей
# def sweets_list(request):
#     sweets = Sweet.objects.all()
    
#     # Фильтрация по бренду
#     brand_id = request.GET.get('brand')
#     if brand_id:
#         sweets = sweets.filter(brand_id=brand_id)
    
#     # Фильтрация по виду
#     type_id = request.GET.get('type')
#     if type_id:
#         sweets = sweets.filter(type_id=type_id)
    
#     brands = Brand.objects.all()
#     types = SweetType.objects.all()
    
#     context = {
#         'sweets': sweets,
#         'brands': brands,
#         'types': types,
#     }
#     return render(request, 'sweets/list.html', context)

# # Детальная страница сладости
# def sweet_detail(request, sweet_id):
#     sweet = get_object_or_404(Sweet, pk=sweet_id)
#     context = {
#         'sweet': sweet,
#     }
#     return render(request, 'sweets/detail.html', context)

# # Страница о нас
# def about(request):
#     return render(request, 'about.html')

# from django.shortcuts import render, get_object_or_404
# from .models import Sweet, Brand, SweetType, Flavor, Manufacturer  # Добавлены недостающие импорты

# # Главная страница
# def home(request):
#     sweets = Sweet.objects.all()[:12]  # 12 последних сладостей
#     brands = Brand.objects.all()
#     types = SweetType.objects.all()
    
#     context = {
#         'sweets': sweets,
#         'brands': brands,
#         'types': types,
#     }
#     return render(request, 'home.html', context)

# # Страница всех сладостей
# def sweets_list(request):
#     sweets = Sweet.objects.all()
    
#     # Фильтрация по бренду
#     brand_id = request.GET.get('brand')
#     if brand_id:
#         sweets = sweets.filter(brand_id=brand_id)
    
#     # Фильтрация по виду
#     type_id = request.GET.get('type')
#     if type_id:
#         sweets = sweets.filter(type_id=type_id)
    
#     brands = Brand.objects.all()
#     types = SweetType.objects.all()
    
#     # Передаем текущие выбранные фильтры в контекст
#     context = {
#         'sweets': sweets,
#         'brands': brands,
#         'types': types,
#         'selected_brand': brand_id,
#         'selected_type': type_id,
#     }
#     return render(request, 'sweets/list.html', context)
#     return render(request, 'sweets/list.html', context)

# # Детальная страница сладости
# def sweet_detail(request, sweet_id):
#     sweet = get_object_or_404(Sweet, pk=sweet_id)
#     context = {
#         'sweet': sweet,
#     }
#     return render(request, 'sweets/detail.html', context)

# # Страница о нас
# def about(request):
#     return render(request, 'about.html')
#     return render(request, 'about.html')


from django.shortcuts import render, get_object_or_404
from .models import Sweet, Brand, SweetType

# Главная страница
def home(request):
    sweets = Sweet.objects.all()[:12]
    brands = Brand.objects.all()
    types = SweetType.objects.all()
    
    context = {
        'sweets': sweets,
        'brands': brands,
        'types': types,
        'sweets_count': Sweet.objects.count(),
    }
    return render(request, 'home.html', context)

# Страница всех сладостей
def sweets_list(request):
    sweets = Sweet.objects.all()
    
    # Фильтрация по бренду
    brand_id = request.GET.get('brand')
    if brand_id:
        sweets = sweets.filter(brand_id=brand_id)
    
    # Фильтрация по виду
    type_id = request.GET.get('type')
    if type_id:
        sweets = sweets.filter(type_id=type_id)
    
    brands = Brand.objects.all()
    types = SweetType.objects.all()
    
    context = {
        'sweets': sweets,
        'brands': brands,
        'types': types,
        'selected_brand': brand_id,
        'selected_type': type_id,
        'sweets_count': Sweet.objects.count(),
    }
    return render(request, 'sweets/list.html', context)

# Детальная страница сладости
def sweet_detail(request, sweet_id):
    sweet = get_object_or_404(Sweet, pk=sweet_id)
    # Получаем несколько случайных сладостей для "Похожих товаров"
    related_sweets = Sweet.objects.exclude(pk=sweet_id).order_by('?')[:4]
    
    context = {
        'sweet': sweet,
        'related_sweets': related_sweets,
        'sweets_count': Sweet.objects.count(),
    }
    return render(request, 'sweets/detail.html', context)

# Страница о нас
def about(request):
    context = {
        'sweets_count': Sweet.objects.count(),
    }
    return render(request, 'about.html', context)