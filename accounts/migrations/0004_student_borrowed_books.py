# Generated by Django 4.2.5 on 2023-10-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0002_remove_borrowedbook_book_image_and_more'),
        ('accounts', '0003_remove_admins_phone_number_admins_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='borrowed_books',
            field=models.ManyToManyField(related_name='borrowing_students', to='admins.borrowedbook'),
        ),
    ]