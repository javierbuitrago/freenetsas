# Generated by Django 2.2 on 2019-04-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0045_auto_20190425_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='background_color_contact',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='border_contact',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='border_radius_contact',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='font_family_contact',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='font_size_contact',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='text_color_contact',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='footer',
            name='text_contact',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
    ]
