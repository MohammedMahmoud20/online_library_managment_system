# Generated by Django 4.2.5 on 2023-10-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_student_height_field_student_width_field_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='2.jpg', upload_to='accounts/static/images'),
        ),
    ]