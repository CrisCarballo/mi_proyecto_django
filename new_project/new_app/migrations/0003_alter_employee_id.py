# Generated by Django 4.2.4 on 2023-08-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_rename_works_since_employee_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]