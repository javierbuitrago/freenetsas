# Generated by Django 2.2 on 2019-04-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0050_auto_20190425_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='link_icon1',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='team',
            name='link_icon2',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='team',
            name='link_icon3',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='team',
            name='link_icon4',
            field=models.CharField(max_length=2000),
        ),
    ]
