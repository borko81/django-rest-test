# Generated by Django 3.1 on 2020-12-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simples',
            name='razpad',
            field=models.BooleanField(default=False),
        ),
    ]
