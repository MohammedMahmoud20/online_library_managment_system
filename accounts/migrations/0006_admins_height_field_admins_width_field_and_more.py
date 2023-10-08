# Generated by Django 4.2.5 on 2023-10-07 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_admins_image_alter_student_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='admins',
            name='height_field',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='admins',
            name='width_field',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='height_field',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='width_field',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='admins',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/static/images'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/static/images'),
        ),
    ]
