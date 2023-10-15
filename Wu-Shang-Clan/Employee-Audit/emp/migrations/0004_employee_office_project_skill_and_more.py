# Generated by Django 4.2.6 on 2023-10-15 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("emp", "0003_crudlog"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("emp_id", models.CharField(max_length=200)),
                ("phone", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=150)),
                ("working", models.BooleanField(default=True)),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="emp.department",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Office",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name="CRUDLog",
            new_name="AuditLog",
        ),
        migrations.CreateModel(
            name="ProjectAssignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp.employee"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp.project"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp.department"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeSkill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp.employee"
                    ),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp.skill"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeOfficeAssignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp.employee"
                    ),
                ),
                (
                    "office",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="emp.office"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="employee",
            name="position",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="emp.position",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="assigned_to",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="emp.employee",
            ),
        ),
        migrations.DeleteModel(
            name="Emp",
        ),
    ]