# Generated by Django 3.1.14 on 2022-01-13 12:26

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('CustumPlugins', '0003_auto_20220113_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInformations',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='custumplugins_admininformations', serialize=False, to='cms.cmsplugin')),
                ('name', models.CharField(default='Admin', max_length=50)),
                ('contact_number', models.IntegerField(null=True)),
                ('about_us', tinymce.models.HTMLField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]