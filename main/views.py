from django.shortcuts import render, redirect

from .models import Product
from .forms import ProductForm


def index(request):
    """
    Переход на главную страницу
    :param request: запрос пользователя
    :return: отображение главной страницы
    """
    products = Product.objects.all()
    return render(request, 'main/index.html')

def orders(request):
    """
    Переход на страницу кассира для просмотра предыдущих заказов и фиксации новых.
    :param request: запрос пользователя
    :return: отображение страницы кассира
    """
    products = Product.objects.all()
    return render(request, 'main/user.html',
                  {'title': 'Заказы',
                   'products': products})

def admin(request):
    """
    Переход на страницу администратора
    :param request: запрос пользователя
    :return: отображение страницы администратора
    """
    return render(request, 'main/admin.html')

def create(request):
    """
    Создание заказа, его внесение в базу данных, переход на страницу заказов.
    :param request: запрос пользователя
    :return: отображение страницы заказа
    """
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user')
        else:
            error = "form is not valid"

    form = ProductForm()
    context = {'form': form,
               'error': error}
    return render(request, 'main/create.html', context)

def user_is_active(request):
    """
    В случае, если кассир в системе, переход на страницу заказов
    :param request: запрос пользователя
    :return: отображение страницы кассира
    """
    return render(request, 'main/user.html')
