from django.contrib import admin
from admins.models import Book,BorrowedBook
admin.site.register(Book)
admin.site.register(BorrowedBook)
# Register your models here.
