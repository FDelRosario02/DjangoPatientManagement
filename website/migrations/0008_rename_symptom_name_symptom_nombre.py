# Generated by Django 5.0.2 on 2024-03-03 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_symptom_patient_symptom'),
    ]

    operations = [
        migrations.RenameField(
            model_name='symptom',
            old_name='symptom_name',
            new_name='nombre',
        ),
    ]
