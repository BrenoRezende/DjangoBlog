from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('criar/', views.new_account_view, name='criar'),
    path('login/', views.login_view, name='login')
]