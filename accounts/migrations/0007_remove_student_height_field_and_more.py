# Generated by Django 4.2.5 on 2023-10-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_admins_height_field_admins_width_field_and_more'),
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
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='profile/', width_field=200),
        ),
    ]
