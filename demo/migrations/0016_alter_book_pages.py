# Generated by Django 5.0.2 on 2024-02-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0015_remove_book_unique_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(help_text='Le nombre de pages'),
        ),
    ]
