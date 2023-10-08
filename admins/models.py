from django.db import models
from django.urls import reverse
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='admins/images/',default='heat2webp.webp')
    description = models.TextField()
    published_at=models.DateTimeField(auto_now_add=True)
    Borrowed_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    @classmethod
    def get_all_books(cls):
        return cls.objects.all()
    @classmethod
    def get_specific_book(cls,id):
        return cls.objects.get(id=id)

    def get_image_url(self):
        return f'/media/{self.image}'

    def get_edit_url(self):
        return reverse('admin_edit',args=[self.id])

# class BorrowedBook(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     borrower_name = models.CharField(max_length=100,default='mohammed')
#     book_name=models.CharField(max_length=100,null=True)
#     book_image=models.ImageField(upload_to='admins/images/',default='heat2webp.webp')
#     borrow_date = models.DateTimeField(auto_now_add=True)
#     return_date = models.DateTimeField()
class BorrowedBook(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=100)
    return_date = models.DateField()

    def __str__(self):
        return self.book.name
    @classmethod
    def get_all_books(cls):
        return cls.objects.all()
    @classmethod
    def get_specific_book(cls,id):
        return cls.objects.get(id=id)

    def get_image_url(self):
        return f'/media/{self.book_image}'

    def get_edit_url(self):
        return reverse('admin_edit',args=[self.id])