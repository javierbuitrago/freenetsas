# Generated by Django 2.2 on 2019-04-25 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personalization', '0017_auto_20190425_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalization_page',
            name='link_mape_contact',
            field=models.CharField(default=1, max_length=9000),
            preserve_default=False,
        ),
    ]