# Generated by Django 2.2 on 2019-04-25 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0043_auto_20190425_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='slogan',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]