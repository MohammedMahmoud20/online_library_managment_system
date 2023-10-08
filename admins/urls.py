# admins/urls.py
from django.contrib.auth.decorators import login_required
from django.urls import path
from admins import views

urlpatterns = [
    path('books/',views.all_books,name='admin_all_books'),
    path('create/',views.create_book,name='admin_create'),
    path('<int:Book_id>/show/',views.show,name='admins_show'),
    path('edit/<int:Book_id>/', views.edit, name='edit'),
    path('<int:id>/delete',views.delete, name='admins_delete' ),
    path('books/<int:book_id>/borrow/', views.borrow_book, name="borrow_book"),
    path('books/borrowed/', views.borrowed_books, name="borrowed_books"),
    path('search_student/', views.search_student, name='search_student'),
    path('search_student/<int:user_id>/', views.user_details, name='user_details'),
]