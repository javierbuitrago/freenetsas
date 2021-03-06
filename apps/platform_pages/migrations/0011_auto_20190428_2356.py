# Generated by Django 2.2 on 2019-04-28 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platform_pages', '0010_publicidad_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='caracteristicas',
            name='font_family',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='caracteristicas',
            name='font_size',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='color_background_caja_description',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='color_background_caja_texto',
            field=models.CharField(default=1, max_length=90),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='icono_plan',
            field=models.CharField(default=1, max_length=9000),
            preserve_default=False,
        ),
    ]
