from django.shortcuts import render,redirect,reverse
from admins.models import Book,BorrowedBook
from admins.forms import bookModelForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import User,Admins,Student
# ...

@staff_member_required
def all_books(request):
    books = Book.objects.all()
    boooks = Book.objects.order_by('id').first()
    return render(request, template_name='admins/book.html', context={"books": books, "book": boooks})

@login_required
def create_book(request):
    if not request.user.is_admin:  # Check if the user is not an admin
        return HttpResponse("You do not have permission to perform this action.")
    else:
     form  = bookModelForm()
     if request.method == 'POST':
         form = bookModelForm(request.POST, request.FILES)
         if form.is_valid():
             form.save()
             url = reverse('admin_all_books')
             return redirect(url)
         return render(request, 'admins/create.html', context={"form": form})
    return render(request, 'admins/create.html', context={"form":form})

@login_required
def edit(request, Book_id):
    if not request.user.is_admin:  # Check if the user is not an admin
        return HttpResponse("You do not have permission to perform this action.")
    else:
     book = get_object_or_404(Book, id=Book_id)
     if request.method == 'POST':
         book.name = request.POST.get('name')
         book.image = request.FILES.get('image')
         book.price = request.POST.get('price')
         book.save()
         bact_to_url = reverse('admin_all_books')
         return redirect(bact_to_url)
    return render(request, 'admins/edit.html', {'book': book})

@login_required
def delete(request, id):
    if not request.user.is_admin:  # Check if the user is not an admin
        return HttpResponse("You do not have permission to perform this action.")
    else:
      book = Book.get_specific_book(id)
      book.delete()
      url = reverse('admin_all_books')
      return redirect(url)

def show(request, Book_id):
    Booke_obj = Book.objects.get(id=Book_id)
    return render(request, 'admins/show.html', {'book': Booke_obj})

@staff_member_required
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.all()
    return render(request, 'admins/borrow_book.html', {'borrowed_books': borrowed_books})

@staff_member_required
def all_users(request):
    users = User.objects.all()
    return render(request, 'accounts/all_users.html', {'users': users})

@staff_member_required
def user_details(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'accounts/profile.html', {'user': user})

@staff_member_required
def search_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            return render(request, 'accounts/profile.html', {'student': student})
        except Student.DoesNotExist:
            return HttpResponse("Student not found.")
    return render(request, 'admins/search_student.html')

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrower_name = request.user.username  # Assuming the borrower is authenticated
    return_date = datetime.now() + timedelta(days=7)  # Set return date to a week from now
    borrowed_book = BorrowedBook(book=book, borrower_name=borrower_name, return_date=return_date)
    borrowed_book.save()
    url = reverse('borrowed_books')
    return redirect(url)
@login_required
def borrowed_books(request):
    borrowed_books = BorrowedBook.objects.all()
    return render(request, 'admins/borrow_book.html', {'borrowed_books': borrowed_books})
# # Create your views here.
# def hello(request):
#     return render(request,template_name='admins/hello.html')
# def all_books(request):
#     books = Book.objects.all()
#     boooks=Book.objects.order_by('id').first()
#     return render(request, template_name='admins/book.html', context={"books": books, "book": boooks})
# @login_required
# def create_book(request):
    # form  = bookModelForm()
    # if request.method == 'POST':
    #     form = bookModelForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         url = reverse('admin_all_books')
    #         return redirect(url)
    #     return render(request, 'admins/create.html', context={"form": form})
    # return render(request, 'admins/create.html', context={"form":form})
# @login_required
# def show(request, Book_id):
#     Booke_obj = Book.objects.get(id=Book_id)
#     return render(request, 'admins/show.html', {'book': Booke_obj})
# @login_required
# def edit(request, Book_id):
    # book = get_object_or_404(Book, id=Book_id)
    # if request.method == 'POST':
    #     book.name = request.POST.get('name')
    #     book.image = request.FILES.get('image')
    #     book.price = request.POST.get('price')
    #     book.save()
    #     bact_to_url = reverse('admin_all_books')
    #     return redirect(bact_to_url)
    # return render(request, 'admins/edit.html', {'book': book})
# @login_required
# def delete(request, id):
    # book = Book.get_specific_book(id)
    # book.delete()
    # url = reverse('admin_all_books')
    # return redirect(url)


# @login_required
# def borrow_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     borrower_name = request.user.username  # Assuming the borrower is authenticated
#     return_date = datetime.now() + timedelta(days=7)  # Set return date to a week from now
#     borrowed_book = BorrowedBook(book=book, borrower_name=borrower_name, return_date=return_date)
#     borrowed_book.save()
#     url = reverse('borrowed_books')
#     return redirect(url)
# @login_required
# def borrowed_books(request):
#     borrowed_books = BorrowedBook.objects.all()
#     return render(request, 'admins/borrow_book.html', {'borrowed_books': borrowed_books})