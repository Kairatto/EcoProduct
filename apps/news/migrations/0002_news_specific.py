# Generated by Django 5.0.6 on 2024-06-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='specific',
            field=models.CharField(max_length=5000, null=True, verbose_name='Определите новость, для разных языков'),
        ),
    ]
