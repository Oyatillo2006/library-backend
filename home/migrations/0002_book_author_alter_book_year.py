# Generated by Django 4.2.5 on 2023-09-13 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='home.author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(),
        ),
    ]