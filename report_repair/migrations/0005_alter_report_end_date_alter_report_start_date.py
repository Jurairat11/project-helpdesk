# Generated by Django 5.1 on 2024-09-04 07:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("report_repair", "0004_remove_report_employee_report_staff"),
    ]

    operations = [
        migrations.AlterField(
            model_name="report",
            name="end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="start_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
