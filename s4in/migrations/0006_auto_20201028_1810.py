# Generated by Django 3.1.2 on 2020-10-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s4in', '0005_auto_20201028_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.TextField(max_length=400, verbose_name='unvan'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address1',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Adres 1'),
        ),
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Adres 2'),
        ),
        migrations.AlterField(
            model_name='advantages',
            name='note',
            field=models.TextField(max_length=75, verbose_name='avantaji'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='title',
            field=models.TextField(max_length=400, verbose_name='unvan'),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='aciklama'),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='hizmet adi'),
        ),
        migrations.AlterField(
            model_name='whyus',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='aciklama'),
        ),
        migrations.AlterField(
            model_name='whyus',
            name='reason',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='hizmet adi'),
        ),
        migrations.AlterField(
            model_name='whyus',
            name='reasonMavi',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mavi kelemeyle cumlenin basina opsiyonel olarak eklenecek'),
        ),
    ]
