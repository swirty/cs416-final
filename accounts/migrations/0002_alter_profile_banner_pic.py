# Generated by Django 4.1.3 on 2022-12-15 06:32

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='banner_pic',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default-banner-pic.png', force_format='PNG', keep_meta=False, null=True, quality=100, scale=None, size=[1280, 320], upload_to=''),
        ),
    ]
