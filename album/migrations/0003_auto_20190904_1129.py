# Generated by Django 2.2.3 on 2019-09-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20190903_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='title',
            field=models.TextField(),
        ),
    ]