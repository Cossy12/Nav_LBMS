# Generated by Django 4.2.1 on 2023-05-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbms_app', '0002_book_price_fee_alter_student_branch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price_fee',
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='classroom',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]