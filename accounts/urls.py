# from django.urls import path
# from . import views



# urlpatterns = [
#     
#     # path('profile/',views.profile,name='profile'),
#     # path('profile/edit',views.profile_edit,name='profile_edit'),
# ]

from django.urls import path
from .import  views

app_name='accounts'

urlpatterns=[
     path('register/',views.register, name='register'),
     path('admin_register/',views.admin_register.as_view(), name='admin_register'),
     path('student_register/',views.student_register.as_view(), name='student_register'),
     path('login/', views.user_login, name='login'),
     path('logout/', views.user_logout, name='logout'),
     path('pprofile/<int:student_id>/', views.student_profile, name='student_profile'),
     path('users/', views.all_users, name='all_users'),
     path('edit_profile/', views.edit_profile, name='edit_profile'),
]

