from django.contrib.auth import login, logout,authenticate
from django.shortcuts import redirect, render,reverse
from django.contrib import messages
from django.views.generic import CreateView
from .forms import adminSignUpForm, studentSignUpForm,UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Admins,Student
from django.contrib.auth.decorators import login_required
from admins.models import Book,BorrowedBook
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
def register(request):
    return render(request, 'registration/sign_up.html')
class admin_register(CreateView):
    model = User
    form_class = adminSignUpForm
    template_name = 'registration/admin_register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        url = reverse('admin_all_books')
        return redirect(url)
class student_register(CreateView):
    model = User
    form_class = studentSignUpForm
    template_name = 'registration/student_register.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        url = reverse('students_all_books')
        return redirect(url)
def user_logout(request):
    logout(request)
    return render(request, 'registration/logged.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if hasattr(user, 'Admins'):
                url = reverse('admin_all_books')
                return redirect(url)
            if hasattr(user, 'Student'):
                url = reverse('students_all_books')
                return redirect(url)
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'registration/login.html')
@login_required
def student_profile(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        borrowed_books = BorrowedBook.objects.all()
        return render(request, 'accounts/profile.html', {'student': student, 'borrowed_books': borrowed_books})
    except Student.DoesNotExist:
        return HttpResponse("User doesn't exist")

@login_required
def all_users(request):
    users = User.objects.all()
    return render(request, 'accounts/all_users.html', {'users': users})

def edit_profile(request):
    student = request.user.student
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student.user.first_name = first_name
        student.user.last_name = last_name
        student.user.save()
        return redirect('accounts:student_profile', student_id=student.id)
    return render(request, 'accounts/edit_profile.html', {'student': student})