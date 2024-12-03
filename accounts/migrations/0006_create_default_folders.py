# Generated by Django 5.1.3 on 2024-11-07 17:57

from django.db import migrations

def create_default_folders(apps, schema_editor):
    Folder = apps.get_model('accounts', 'Folder')
    User = apps.get_model('auth', 'User')

    default_folder_names = ["Documents", "Images", "Videos"]
    for user in User.objects.all():
        for folder_name in default_folder_names:
            Folder.objects.get_or_create(name=folder_name, user=user)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_populate_share_link'),  # Replace with your last applied migration
    ]

    operations = [
        migrations.RunPython(create_default_folders),
    ]
