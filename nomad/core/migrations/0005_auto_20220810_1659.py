# Generated by Django 3.2.13 on 2022-08-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_feature_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='featurecategory',
            options={'ordering': ('rank', 'name'), 'verbose_name': 'Features category', 'verbose_name_plural': 'Features categories'},
        ),
        migrations.AddField(
            model_name='user',
            name='features',
            field=models.ManyToManyField(related_name='features', to='core.Feature', verbose_name='features'),
        ),
    ]