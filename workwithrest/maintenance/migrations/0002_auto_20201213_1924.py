# Generated by Django 3.1 on 2020-12-13 17:24

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ['-date_add']},
        ),
        migrations.AlterField(
            model_name='problem',
            name='emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems_emp', to='maintenance.employee'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.fields.CharField, related_name='problems_type', to='maintenance.type'),
        ),
    ]
