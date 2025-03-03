from django.contrib.auth.views import LogoutView, LoginView
from  django.urls import path, reverse_lazy
from . import views
from .forms import LoginForm


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path("login/", LoginView.as_view(template_name="login.html", form_class=LoginForm), name="login"),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy("login")), name='logout'),
    path('game/', views.game, name='game'),
    path('submit/', views.quiz_submit, name='quiz_submit'),
    path('ranking/', views.ranking, name='ranking'),
]
