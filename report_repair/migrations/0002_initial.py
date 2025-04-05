# Generated by Django 5.1 on 2024-09-03 06:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("equipment", "0001_initial"),
        ("report_repair", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="employee",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="employee_reports",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="report",
            name="equipment_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reports",
                to="equipment.equipmenttype",
            ),
        ),
        migrations.AddField(
            model_name="report",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user_reports",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="repairoutside",
            name="report",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="outside_repairs",
                to="report_repair.report",
            ),
        ),
        migrations.AddField(
            model_name="reportimage",
            name="report",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="report_repair.report",
            ),
        ),
        migrations.AddField(
            model_name="report",
            name="status",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reports",
                to="report_repair.reportstatus",
            ),
        ),
    ]
