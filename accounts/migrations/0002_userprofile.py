# Generated by Django 2.2 on 2020-07-24 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('websiteUrl', models.URLField(blank=True, null=True)),
                ('facebookUrl', models.URLField(blank=True, null=True)),
                ('twitterUrl', models.URLField(blank=True, null=True)),
                ('telegramUrl', models.URLField(blank=True, null=True)),
                ('linkedinUrl', models.URLField(blank=True, null=True)),
                ('youtubeUrl', models.URLField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
