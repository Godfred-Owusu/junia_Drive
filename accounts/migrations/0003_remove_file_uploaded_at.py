# Generated by Django 5.1.3 on 2024-11-07 00:11

# from django.db import migrations


# class Migration(migrations.Migration):

#     dependencies = [
#         ('accounts', '0002_remove_folder_created_at_remove_folder_parent_and_more'),
#     ]

#     operations = [
#         migrations.RemoveField(
#             model_name='file',
#             name='uploaded_at',
#         ),
#     ]

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_folder_created_at_remove_folder_parent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='uploaded_at',
        ),
    ]