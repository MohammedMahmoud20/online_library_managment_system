from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from admins.models import BorrowedBook,Book
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    @classmethod
    def get_specific_user(cls, id):
        return cls.objects.get(id=id)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="accounts/static/images",default='2.jpg')
    height_field = models.IntegerField(null=True, blank=True)
    width_field = models.IntegerField(null=True, blank=True)
    borrowed_books = models.ManyToManyField(BorrowedBook, related_name='borrowing_students')
    def get_image_url(self):
        return f'/media/admins/images{self.image}'
    def __str__(self):
        return str(self.user)
class Admins(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="accounts/static/images",default='2.jpg')
    height_field = models.IntegerField(null=True, blank=True)
    width_field = models.IntegerField(null=True, blank=True)
    def get_image_url(self):
        return f'/media/admins/images{self.image}'
    def __str__(self):
        return str(self.user)
