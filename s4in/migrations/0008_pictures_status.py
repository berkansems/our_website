# Generated by Django 3.1.2 on 2020-10-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s4in', '0007_auto_20201028_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Gosterilsin mi?'),
        ),
    ]
