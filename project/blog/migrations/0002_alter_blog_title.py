# Generated by Django 5.0 on 2023-12-10 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]