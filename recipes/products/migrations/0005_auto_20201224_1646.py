# Generated by Django 3.1 on 2020-12-24 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201224_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='group',
        ),
        migrations.RemoveField(
            model_name='recipeingredient',
            name='price',
        ),
        migrations.AddField(
            model_name='recepies',
            name='group',
            field=models.ForeignKey(default=2, limit_choices_to={'razpad': True}, on_delete=django.db.models.deletion.CASCADE, related_name='recepies', to='products.grops'),
        ),
        migrations.AddField(
            model_name='recepies',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
