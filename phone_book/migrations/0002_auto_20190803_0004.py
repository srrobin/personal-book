# Generated by Django 2.2.3 on 2019-08-02 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonebookmodel',
            old_name='personal',
            new_name='personal_num_new',
        ),
    ]