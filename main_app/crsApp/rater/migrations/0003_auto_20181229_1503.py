# Generated by Django 2.1.4 on 2018-12-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rater', '0002_auto_20181229_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_hash',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
