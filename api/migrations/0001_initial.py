# Generated by Django 3.2.7 on 2021-09-19 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('DeptId', models.AutoField(primary_key=True, serialize=False)),
                ('DeptName', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeetId', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeetName', models.CharField(max_length=500)),
                ('Dept', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateField()),
            ],
        ),
    ]