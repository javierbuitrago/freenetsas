# Generated by Django 2.2 on 2019-04-26 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalization', '0020_auto_20190426_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalization_page',
            name='background_color_description_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='background_color_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='border_description_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='border_radius_description_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='border_radius_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='border_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='color_text_description_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='color_text_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='description_service',
            field=models.CharField(default=1, max_length=9000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='font_family_description_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='font_family_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='font_size_description_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='font_size_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='text_aling_description_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalization_page',
            name='title_service',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
    ]
