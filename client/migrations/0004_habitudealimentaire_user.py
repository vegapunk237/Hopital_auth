# Generated by Django 4.2.1 on 2023-12-26 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0003_remove_habitudealimentaire_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='habitudealimentaire',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]