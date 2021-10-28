# Generated by Django 3.2.8 on 2021-10-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_auto_20211025_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Starter', 'Starter'), ('Main', 'Main'), ('Side', 'Side'), ('Dessert', 'Dessert'), ('Bakes', 'Bakes'), ('Salad', 'Salad'), ('Soup', 'Soup')], default='Main', max_length=15),
        ),
    ]