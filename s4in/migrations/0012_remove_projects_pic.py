# Generated by Django 3.1.2 on 2020-10-30 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s4in', '0011_projects_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='pic',
        ),
    ]
