# Generated by Django 2.2 on 2019-04-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0032_auto_20190424_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='height_image',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='width_image',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
