# Generated by Django 3.1.14 on 2022-01-13 10:27

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('CustumPlugins', '0002_userlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlist',
            name='company_name',
            field=tinymce.models.HTMLField(),
        ),
    ]
