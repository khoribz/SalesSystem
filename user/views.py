from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import AuthUserForm

class LoginUser(LoginView):
    """
    Наследник LoginView, получаем данные логина пользователя
    """
    template_name = 'registration/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('user')
    def get_success_url(self):
        return self.success_url


class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')
