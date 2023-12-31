# Generated by Django 4.2.1 on 2023-12-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_rename_recu_patient_status_remove_patient_adresse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='service',
            field=models.CharField(choices=[('C', 'CHIRURGIEN'), ('CA', 'CARDIOLOGUE'), ('DER', 'DERMATOLOGUE'), ('DEN', 'DENTISTE'), ('O', 'OPHTALMOLOGUE')], max_length=100),
        ),
    ]