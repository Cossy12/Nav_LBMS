# Generated by Django 4.2.1 on 2023-05-31 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbms_app', '0004_remove_student_image_remove_student_phone_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbook',
            name='book_return',
            field=models.BooleanField(default=False),
        ),
    ]
