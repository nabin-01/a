# Generated by Django 3.1.7 on 2021-04-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='products',
        ),
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
