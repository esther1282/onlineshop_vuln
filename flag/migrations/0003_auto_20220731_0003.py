# Generated by Django 3.2.13 on 2022-07-31 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flag', '0002_flag_input'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flag',
            name='input',
        ),
        migrations.AddField(
            model_name='flag',
            name='data',
            field=models.CharField(blank=True, max_length=255, verbose_name='data'),
        ),
    ]