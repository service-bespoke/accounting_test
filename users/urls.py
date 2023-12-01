from django.urls import path
from . import views
app_name = 'users'
urlpatterns = [

    path('register/', views.Register, name='reg'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('select_company/', views.selectCompany, name='login_company'),
    path('logout/', views.Logout_View.as_view(), name='logout'),

    path('dashboard/user/', views.User_All.as_view(), name='user_all'),
    path('dashboard/user/<int:pk>/update/', views.user_update, name='user_update'),
    path('dashboard/user/<int:pk>/change_password/', views.change_password, name='change_password'),
    path('dashboard/user/<int:pk>/user_delete/', views.user_delete, name='user_delete'),
]