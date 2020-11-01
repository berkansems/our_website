# Generated by Django 3.1.2 on 2020-10-28 07:27

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anasayfa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='unvan')),
                ('description', models.CharField(max_length=400, verbose_name='alt yazi')),
            ],
        ),
        migrations.CreateModel(
            name='avantajlar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=75, verbose_name='avantaji')),
            ],
        ),
        migrations.CreateModel(
            name='Hakkimizda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='unvan')),
                ('description', models.CharField(max_length=400, verbose_name='alt yazi')),
            ],
        ),
        migrations.CreateModel(
            name='Hizmetler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='hizmet adi')),
                ('description', models.CharField(max_length=400, verbose_name='aciklama')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='png resim seciniz')),
            ],
        ),
        migrations.CreateModel(
            name='NedenBiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=400, verbose_name='hizmet adi')),
                ('reasonMavi', models.CharField(max_length=400, verbose_name='Mavi kelemeyle cumlenin basina opsiyonel olarak eklenecek')),
                ('description', models.CharField(max_length=400, verbose_name='aciklama')),
            ],
        ),
        migrations.CreateModel(
            name='Sectors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Sektor Adı')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Proje Adı')),
                ('description', models.TextField(blank=True, max_length=1250, null=True, verbose_name='Proje Hakkında')),
                ('type', multiselectfield.db.fields.MultiSelectField(choices=[('b2b', 'b2b'), ('b2c', 'b2c'), ('depo_otomasyon', 'depo_otomasyon'), ('arac_takip', 'arac_takip')], max_length=100, verbose_name='tip')),
                ('link', models.URLField(max_length=100, null=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Select an image file')),
                ('showInMainPage', models.BooleanField(default=True, verbose_name='Ana sayfada gosterilsin mi?')),
                ('sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='s4in.sectors', verbose_name='Sektor')),
            ],
        ),
    ]