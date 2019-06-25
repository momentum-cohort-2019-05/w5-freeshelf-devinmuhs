# Generated by Django 2.2.2 on 2019-06-24 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_auto_20190624_1704'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(help_text='Select a category for this book', to='shelf.Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='url_address',
            field=models.URLField(help_text='Enter the url for this book', unique=True),
        ),
    ]
