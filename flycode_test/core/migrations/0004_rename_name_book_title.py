# Generated by Django 4.2.1 on 2023-06-28 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_title_book_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
