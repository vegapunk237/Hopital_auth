# Generated by Django 4.2.1 on 2023-12-30 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_room_date_room_save_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='service',
            field=models.CharField(choices=[('C', 'CHIRURGIEN'), ('CA', 'CARDIOLOGUE'), ('DER', 'DERMATOLOGUE'), ('DEN', 'DENTISTE'), ('O', 'OPHTALMOLOGUE')], default=0, max_length=100),
            preserve_default=False,
        ),
    ]
