# Generated by Django 2.2 on 2019-04-26 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('platform_pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_title', models.CharField(max_length=90)),
                ('description_plan', models.CharField(max_length=9000)),
                ('image_plan', models.ImageField(upload_to='static/img/images_counter/')),
                ('background_color_plan', models.CharField(max_length=90)),
                ('padding_plan', models.CharField(max_length=90)),
                ('border_plan', models.CharField(max_length=90)),
                ('border_radius_plan', models.CharField(max_length=90)),
                ('id_counter_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platform_pages.Counter_page')),
            ],
        ),
    ]
