# Generated by Django 4.0.1 on 2022-01-12 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oembeddata',
            name='title',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='oembeddata',
            name='url',
            field=models.CharField(max_length=500),
        ),
    ]
