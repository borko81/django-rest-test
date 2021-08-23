# Generated by Django 3.2.5 on 2021-08-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_country_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountyCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='country',
            name='count',
        ),
    ]
