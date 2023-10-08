from django.shortcuts import render,redirect,reverse
from admins.models import Book,BorrowedBook
from admins.forms import bookModelForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
def all_books(request):
    all_books = Book.objects.all()
    books=Book.objects.order_by('id').first()
    return render(request, template_name='student/all_books.html', context={"books": all_books, "book": books})

def show(request, Book_id):
    Booke_obj = Book.objects.get(id=Book_id)
    return render(request, 'student/show.html', {'book': Booke_obj})

def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrower_name = request.user.username  # Assuming the borrower is authenticated
    return_date = datetime.now() + timedelta(days=7)  # Set return date to a week from now
    borrowed_book = BorrowedBook(book=book, borrower_name=borrower_name, return_date=return_date)
    borrowed_book.save()
    url = reverse('student_borrowed_books')
    return redirect(url)

def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.all()
    return render(request, 'student/borrowed_books.html', {'borrowed_books': borrowed_books})

def return_borrowed_book(request,Book_id):
    book = get_object_or_404(BorrowedBook, id=Book_id)
    book.delete()
    url = reverse('student_borrowed_books')
    return redirect(url)

