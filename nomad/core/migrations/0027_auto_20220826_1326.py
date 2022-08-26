# Generated by Django 3.2.13 on 2022-08-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_mission_year_experience_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='siret',
            field=models.CharField(blank=True, help_text='must be 9 characters wide', max_length=9, verbose_name='SIRET number'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='year_experience_required',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Young graduate'), (1, '0 to 3 years of experience'), (2, '4 to 8 years of experience'), (3, 'more than 8 years of experience')], default=0, verbose_name='years of experience required'),
        ),
    ]
