# Generated by Django 3.2.13 on 2022-08-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Location',
            new_name='WorkLocation',
        ),
        migrations.AlterModelOptions(
            name='worklocation',
            options={'ordering': ('zipcode',), 'verbose_name': 'Work location', 'verbose_name_plural': 'Work locations'},
        ),
    ]