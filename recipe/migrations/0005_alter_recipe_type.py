# Generated by Django 3.2.8 on 2021-10-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_alter_recipe_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Vegan', 'Vegan'), ('Fish', 'Fish')], default='Vegetarian', max_length=15),
        ),
    ]
