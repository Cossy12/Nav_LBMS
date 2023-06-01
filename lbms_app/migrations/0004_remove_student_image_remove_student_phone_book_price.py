# Generated by Django 4.2.1 on 2023-05-31 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbms_app', '0003_remove_book_price_fee_alter_student_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone',
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]