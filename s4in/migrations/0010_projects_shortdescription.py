# Generated by Django 3.1.2 on 2020-10-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s4in', '0009_auto_20201028_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='shortDescription',
            field=models.TextField(blank=True, max_length=1250, null=True, verbose_name='Kısa Açıklama'),
        ),
    ]
