from registration.views import index, RegisterView
from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'registration'

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='register.html',
                                           success_url=reverse_lazy('registration:index')
                                           ), name='register'),
]
