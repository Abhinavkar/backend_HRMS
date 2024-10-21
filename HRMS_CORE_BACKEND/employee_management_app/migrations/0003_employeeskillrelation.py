# Generated by Django 5.1.2 on 2024-10-21 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0002_role_employeetechstackrelation_employeerolerelation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeSkillRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.employeedata')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.skill')),
            ],
        ),
    ]