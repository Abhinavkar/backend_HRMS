# Generated by Django 5.1.2 on 2024-10-21 07:16

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100, verbose_name='Role Name')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeTechStackRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.employeedata')),
                ('tech_stack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.techstack')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeRoleRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.employeedata')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.role')),
            ],
        ),
        migrations.DeleteModel(
            name='EmployeeSkillRelation',
        ),
    ]
