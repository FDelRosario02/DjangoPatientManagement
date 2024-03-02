# Generated by Django 5.0.2 on 2024-03-02 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_doctor_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='current_medications',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='blood_type',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5),
        ),
    ]