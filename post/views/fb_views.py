from django.shortcuts import render
from ..forms import LoginForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request = request,
                username=cd['username'],
                password=cd['password']
            )
            if user is not None:
                if user.is_active:
                    login(request=request, user=user)
                    return HttpResponse('Вы вошли успешно в страницу')
            else:
                return HttpResponse('Аккаунт не найден')
        else:
            return HttpResponse('Неправильный ник или пароль ')
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    return render(request=request, template_name='post/login.html', context=context)

@login_required
def dashboard(request):
    context = {
        'section': 'dashboard'
    }
    return render(
        request=request,
        template_name='post/dashboard.html',
        context=context
    )
