# Generated by Django 2.2 on 2019-04-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0029_auto_20190423_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='height_image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='width_image',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
