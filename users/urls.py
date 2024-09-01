from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView
from sitewomen.settings import LOGOUT_REDIRECT_URL

app_name = "users"

urlpatterns = [
    # Авторизация
    path('login/', views.LoginView.as_view(), name='login'),
    
    # Выход
    path('logout/', views.logout_user, name='logout'),
    
    # Смена пароля
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    
    # Сообщение об успешном изменении пароля
    path('password-change/done/', 
         PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), 
         name="password_change_done"),
    
    # Регистрация
    path('register/', views.RegisterUser.as_view(), name='register'),
    
    #Профиль пользователя
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    
    # Восстановление пароля
    path('password-reset/',
         PasswordResetView.as_view(
             template_name="users/password_reset_form.html",
             email_template_name="users/password_reset_email.html",
             success_url=reverse_lazy("users:password_reset_done")
         ),
         name='password_reset'),
    
    # Сообщение об отправке ссылки для восстановления пароля
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"),
         name='password_reset_done'),
    
    # Вход по ссылке для восстановления пароля
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name="users/password_reset_confirm.html",
             success_url=reverse_lazy("users:password_reset_complete")
         ),
         name='password_reset_confirm'),
    
    # Сообщение об успешном восстановлении пароля
    path('password-reset/complete/', 
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), 
         name='password_reset_complete'),
]