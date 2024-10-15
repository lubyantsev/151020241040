from django.shortcuts import render
from .forms import UserRegister
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Псевдо-список существующих пользователей
users = {'user1', 'user2', 'user3'}

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif User.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Сохранение нового пользователя
                user = User(username=username, password=make_password(password))
                user.save()
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif User.objects.filter(username=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Сохранение нового пользователя
                user = User(username=username, password=make_password(password))
                user.save()
                return render(request, 'fifth_task/registration_page.html', {'message': f'Приветствуем, {username}!'})

    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', info)