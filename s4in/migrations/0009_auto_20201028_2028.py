# Generated by Django 3.1.2 on 2020-10-28 17:28

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('s4in', '0008_pictures_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainpage',
            options={'verbose_name_plural': 'Anasayfa Yazısı'},
        ),
        migrations.AddField(
            model_name='pictures',
            name='cover',
            field=models.BooleanField(default=False, verbose_name='kapak resim mi?'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Alt Yazi'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=models.TextField(max_length=400, verbose_name='Unvan'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='description',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Alt Yazi'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='title',
            field=models.TextField(max_length=400, verbose_name='Unvan'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='showInMainPage',
            field=models.BooleanField(default=True, verbose_name='Bu Proje Ana Sayfada Gosterilsin Mi?'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('b2b', 'b2b'), ('b2c', 'b2c'), ('depo_otomasyon', 'depo_otomasyon'), ('arac_takip', 'arac_takip')], max_length=100, verbose_name='Tip'),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Aciklama'),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Hizmet adi'),
        ),
        migrations.AlterField(
            model_name='services',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Png Resim Seciniz'),
        ),
        migrations.AlterField(
            model_name='whyus',
            name='reason',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Hizmet adi'),
        ),
    ]
