# Generated by Django 3.2.13 on 2022-07-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20220704_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping',
            field=models.IntegerField(default=3000),
        ),
    ]