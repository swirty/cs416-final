# Generated by Django 4.1.3 on 2022-11-30 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cosmos', '0002_reaction_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cosmos.post'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default="Hello, Cosmos! I haven't written a bio yet...", max_length=250)),
                ('pro_pic', models.ImageField(default='default-pro-pic.png', null=True, upload_to='')),
                ('banner_pic', models.ImageField(default='default-banner-pic.png', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
