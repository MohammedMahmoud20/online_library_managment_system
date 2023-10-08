from django.contrib.auth.decorators import login_required
from django.urls import path
from students import views

urlpatterns = [
    path('books/',views.all_books,name="students_all_books"),
    path('students/<int:Book_id>/show/',views.show,name='s_show'),
    path('students/books/<int:book_id>/borrow/', views.borrow_book, name="student_borrow_book"),
    path('students/books/borrowed/', views.borrowed_books, name="student_borrowed_books"),
    path('return/<int:Book_id>/',views.return_borrowed_book, name='return_borrowed_book' ),
]