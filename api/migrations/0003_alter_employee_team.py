# Generated by Django 4.2.6 on 2023-10-19 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_employee_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.team'),
        ),
    ]