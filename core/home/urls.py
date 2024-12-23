from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('expenses/', views.expenses, name='expenses'),
    path('update_expense/<id>/', views.update_expense, name='update_expense'),
    path('delete_expense/<id>/', views.delete_expense, name='delete_expense'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('pdf/', views.pdf, name='pdf'),
]
