# Generated by Django 5.0.6 on 2024-06-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourpartners',
            name='image',
            field=models.FileField(upload_to='our_partners_images', verbose_name='Лого партнера'),
        ),
    ]
