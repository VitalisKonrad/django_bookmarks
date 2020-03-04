from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,
                              username=cd['username'],
                              password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Успешная авторизация')
            else:
                return HttpResponse('Аккаунт не активен')
        else:
            return HttpResponse('Неверный логин/пароль')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

#обработчик обернут в декоратор для проверки авторизации пользователя/ иначе страница логона
@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})