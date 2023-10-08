# Generated by Django 4.2.5 on 2023-10-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_remove_borrowedbook_book_image_and_more'),
        ('accounts', '0008_remove_student_borrowed_books_student_height_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='student',
            name='width_field',
        ),
        migrations.AddField(
            model_name='student',
            name='borrowed_books',
            field=models.ManyToManyField(related_name='borrowing_students', to='admins.borrowedbook'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='profile/', width_field=200),
        ),
    ]