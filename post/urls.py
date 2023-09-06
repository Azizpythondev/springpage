from django.urls import path
from .views import fb_views
from .views import cb_views
from django.contrib.auth import views as auth_views
from django.urls import include
urlpatterns = [
    #детальный образ (django.contrib.auth.urls)
    
    #Предыдуший url входа
    #path('login/', views.user_login, name='login')
    
    # # url-адреса для входа (Django)
    # path('login/', view=cb_views.CustomLoginView.as_view(), name='login'),
    # path('logout/', view=auth_views.LogoutView.as_view(), name='logout'),

    # # url - адреса для смены пароля
    # path('password-change/', view=auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/', view=auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # # url-адреса для сброса пароля
    # path('password-reset/', view=auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', view=auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', view=auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', view=auth_views.PasswordResetCompleteView.as_view(), name='password_reset_done_complete'),

    path(route='', view=include('django.contrib.auth.urls')),
    #Главная страница
    path('', fb_views.dashboard, name='dashboard')
]